import { defineConfig } from "astro/config";

// GitHub Pages配下でもPythonの実行証拠へのリンクを途切れさせない。
export default defineConfig({
  site: "https://tonbiattack.github.io",
  base: process.env.GITHUB_ACTIONS ? "/python-by-tests" : "/",
  output: "static",
  build: { inlineStylesheets: "always" },
});
