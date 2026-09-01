import { readFileSync } from "node:fs";
export type Lesson = { slug: string; section: string; title: string; oneLine: string; version: string; testName: string; sourceFile: string; testFile: string; sourcePath: string; testPath: string; checks: string[]; note: string; tags: string[]; outcome: string; };
export const SOURCE_REPOSITORY = "https://github.com/tonbiattack/python-by-tests";
const lesson = (slug: string, title: string, sourceFile: string, sourcePath: string, testName: string, checks: string[], note: string, outcome: string): Lesson => ({ slug, section: "Python", title, oneLine: title, version: "Python 3.13+", testName, sourceFile, testFile: "test_lessons.py", sourcePath, testPath: "tests/test_lessons.py", checks, note, tags: ["pitfall", "python"], outcome });
export const lessons: Lesson[] = [
  lesson("identity/is-vs-equals", "is と ==: 同一性と値の等価性は別", "identity.py", "src/python_by_tests/identity.py", "isとequalsは別の契約", ["別listはisでfalse", "内容が同じlistは==でtrue"], "Noneとの比較を除き、値比較には==を使います。", "is → false\n== → true"),
  lesson("mutability/default-argument", "mutable default argument: 呼び出し間で値を共有する", "defaults.py", "src/python_by_tests/defaults.py", "mutable default argumentは共有される", ["一回目の追加が二回目にも残る"], "可変の既定値はNoneをsentinelにして関数内で作ります。", "[first, second]"),
  lesson("mutability/shallow-deep-copy", "copy: shallow copyは入れ子を共有しdeepcopyは共有しない", "copies.py", "src/python_by_tests/copies.py", "shallowとdeep copyは入れ子の共有が違う", ["shallow copyは後続変更を反映", "deepcopyは反映しない"], "入れ子の可変データを境界で渡す場合はコピー深さを選びます。", "shallow → after\ndeep → before"),
  lesson("closure/late-binding", "closure: loop変数はlate bindingで最後の値を読む", "closures.py", "src/python_by_tests/closures.py", "closureは最後のloop値を読む", ["全callbackが最後の値2を返す"], "loop値を固定したい場合は既定引数などで早期束縛します。", "[2, 2, 2]"),
  lesson("generator/lazy-single-use", "generator: 遅延評価され、一度消費すると戻らない", "generators.py", "src/python_by_tests/generators.py", "generatorはlazyかつsingle-use", ["生成時には処理しない", "二回目は空"], "generatorは副作用と消費位置を持つため、再利用には新しく作ります。", "calls before → []\nsecond consume → []"),
  lesson("resources/context-manager", "with: __enter__と__exit__でリソース境界を固定する", "resources.py", "src/python_by_tests/resources.py", "context managerはexitを呼ぶ", ["enter、use、exitの順になる"], "ファイルやロックはwithで所有期間を明示します。", "[enter, use, exit]"),
];
export const navigation = [{ label: "Python", items: lessons }];
const read = (path: string) => readFileSync(new URL(`../../examples/${path}`, import.meta.url), "utf8").trim();
export const sourceCode = (lesson: Lesson) => read(lesson.sourcePath);
export const testCode = (lesson: Lesson) => read(lesson.testPath);
