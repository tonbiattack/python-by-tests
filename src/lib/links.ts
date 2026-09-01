/** GitHub Pagesのプロジェクトサブパスとローカル開発の双方で正しい内部URLを返す。 */
const base = import.meta.env.BASE_URL.endsWith("/") ? import.meta.env.BASE_URL : `${import.meta.env.BASE_URL}/`;
export const withBase = (path = "") => `${base}${path.replace(/^\//, "")}`;
