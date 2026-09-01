import { defineConfig } from "astro/config";

// Design system: パケット追跡の作業台 — GitHub Pages配下でもGoの実行証拠を途切れさせない。
export default defineConfig({
  site: "https://tonbiattack.github.io",
  base: process.env.GITHUB_ACTIONS ? "/python-by-tests" : "/",
  output: "static",
  build: { inlineStylesheets: "always" },
});
