import { existsSync } from "node:fs";
import { readdir, readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const projectRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const distRoot = path.join(projectRoot, "dist");
const rawBase = process.env.GITHUB_PAGES_BASE ?? "/python-by-tests";
const basePath = rawBase === "/" ? "" : `/${rawBase.replace(/^\/+|\/+$/g, "")}`;

async function findHtmlFiles(directory) {
  const entries = await readdir(directory, { withFileTypes: true });
  const nested = await Promise.all(entries.map(async (entry) => {
    const fullPath = path.join(directory, entry.name);
    if (entry.isDirectory()) return findHtmlFiles(fullPath);
    return entry.name.endsWith(".html") ? [fullPath] : [];
  }));
  return nested.flat();
}

function targetExists(urlPath) {
  const decodedPath = decodeURIComponent(urlPath);
  const candidate = path.join(distRoot, decodedPath.replace(/^\//, ""));
  if (path.extname(decodedPath)) return existsSync(candidate);
  return existsSync(candidate) || existsSync(path.join(candidate, "index.html"));
}

if (!existsSync(distRoot)) throw new Error("dist/ が見つかりません。先に pnpm build を実行してください。");

const failures = [];
const htmlFiles = await findHtmlFiles(distRoot);
for (const htmlFile of htmlFiles) {
  const html = await readFile(htmlFile, "utf8");
  const linkPattern = /(?:href|src)="([^"#?]+)(?:[?#][^"]*)?"/g;
  for (const match of html.matchAll(linkPattern)) {
    const url = match[1];
    if (!url.startsWith("/")) continue;
    if (basePath && !(url === basePath || url.startsWith(`${basePath}/`))) {
      failures.push(`${path.relative(projectRoot, htmlFile)}: ${url} は ${basePath || "/"} 配下ではありません`);
      continue;
    }
    const target = basePath ? url.slice(basePath.length) || "/" : url;
    if (!targetExists(target)) failures.push(`${path.relative(projectRoot, htmlFile)}: ${url} の出力先がありません`);
  }
}

if (failures.length) {
  console.error("GitHub Pagesリンク検査に失敗しました:\n" + failures.map((failure) => `- ${failure}`).join("\n"));
  process.exit(1);
}

console.log(`GitHub Pagesリンク検査に成功しました: ${htmlFiles.length}ページを確認`);
