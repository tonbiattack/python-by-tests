# Python by Tests 教材拡張ガイド

## 目的

Python by Tests は、Python の文法を網羅する入門教材ではありません。

目的は、**Python の言語仕様・標準ライブラリ・代表的な機能の挙動を、実行可能なテストから理解すること**です。

特に Python は、動的型付け、ミュータブルなオブジェクト、参照共有、特殊メソッド、イテレータ、ジェネレータ、デコレータ、async/await など、コードを読むだけでは誤解しやすい要素が多くあります。

「知識として説明できる」だけでなく、**テスト結果を見たことで挙動を具体的に予測できるようになるか**を教材追加の判断基準にします。

---

## 教材テーマの分類

各テーマは、原則として次のいずれかに分類してください。

### Pitfall

間違えやすい、または直感と実際の挙動がずれやすいテーマです。

例:

- mutable default argument
- `is` と `==`
- shallow copy と deep copy
- closure の late binding
- list multiplication による参照共有
- class attribute と instance attribute
- mutable object の hashability

### Behavior

Python の重要な実行時挙動や標準 API の契約を確認するテーマです。

例:

- list / tuple の可変性
- dict の insertion order
- iterator の消費
- generator の遅延評価
- context manager の enter / exit
- exception chaining
- `__eq__` / `__hash__`
- dataclass の生成されるメソッド

### Concept

Python の重要概念を、テストによって観測できる形で理解するテーマです。

例:

- object identity
- duck typing
- protocol
- descriptor
- decorator
- iterator / iterable
- generator
- context manager
- coroutine
- async / await
- type hints と runtime の関係

---

## 追加してよいテーマの判断基準

次のうち一つ以上に該当するテーマを優先してください。

1. 実行結果を初見で予測しにくい
2. 実務でバグやレビュー指摘につながりやすい
3. Python の設計思想や言語仕様の理解につながる
4. テストで確認すると説明だけより理解しやすい
5. 他言語経験者が誤解しやすい
6. 同じように見える API や構文で挙動が異なる
7. 型チェック時と runtime で意味が異なる

---

## 追加しないテーマ

以下は原則として対象外です。

- 単純すぎる構文確認
- Python 入門書で最初に扱うだけの内容
- テストしても理解がほぼ深まらない内容
- 外部フレームワーク固有の使い方だけを説明する内容
- ライブラリ API の単なる使用例
- テーマ数を増やすためだけの細分化

例えば、次のような内容だけでは教材にしません。

```python
x = 1 + 2
assert x == 3
```

```python
if True:
    value = 1
```

```python
items = []
items.append("a")
assert items == ["a"]
```

ただし、同じ API でも参照共有、評価タイミング、境界値、例外、特殊メソッドとの関係など、Python 固有の契約を観測できる場合は教材対象になり得ます。

---

## Python版で特に重視する軸

### 1. Identity / Equality

優先度: A

候補:

- `is` と `==`
- object identity
- `__eq__`
- `__hash__`
- hashable / unhashable
- `None` 比較
- small integer / string interning を教材化する場合の注意

interning は実装詳細への依存が強いため、Python 言語仕様として保証される挙動と CPython 固有の最適化を混同しないでください。

### 2. Mutability / Reference Sharing

優先度: A

候補:

- mutable default argument
- list の参照共有
- list multiplication
- shallow copy
- deep copy
- tuple 内部に mutable object を持つ場合
- function argument と object mutation
- class attribute / instance attribute

Python の学習で特に誤解されやすいため、重点カテゴリとします。

### 3. Collections

優先度: A

候補:

- list / tuple
- dict
- set / frozenset
- dict insertion order
- dict key の hashability
- set の重複排除
- unpacking
- starred expression
- slicing
- negative index

単純な append / get の使い方ではなく、可変性・参照・順序・hash 契約を中心にしてください。

### 4. Functions / Scope / Closure

優先度: A

候補:

- LEGB scope
- closure
- late binding
- default argument の評価タイミング
- `nonlocal`
- `global`
- first-class function
- decorator
- callable object

特に「いつ値が評価されるか」をテストで見せられるテーマを優先します。

### 5. Iterator / Generator

優先度: A

候補:

- iterable と iterator
- iterator の一度きりの消費
- `iter()` / `next()`
- generator の遅延評価
- `yield`
- `yield from`
- generator expression
- list comprehension との評価タイミングの違い

Python らしさが強く、テスト教材との相性が非常に良いため優先してください。

### 6. Exception / Resource Management

優先度: A

候補:

- `try` / `except` / `else` / `finally`
- exception chaining
- `raise ... from ...`
- custom exception
- context manager
- `with`
- `__enter__` / `__exit__`
- `contextlib`

例外型だけでなく、実行順序、cause/context、リソース解放を観測してください。

### 7. Object Model

優先度: B

候補:

- class attribute / instance attribute
- inheritance
- method resolution order
- `super()`
- `classmethod`
- `staticmethod`
- property
- descriptor
- `__getattr__`
- `__getattribute__`
- `__slots__`
- dataclass

特殊メソッドを網羅するのではなく、Python の object model の理解につながるものを選んでください。

### 8. Type System

優先度: A

候補:

- type hints は runtime で強制されない
- `Any`
- `Optional`
- `Union` / `|`
- narrowing
- `Protocol`
- structural typing
- generic
- `TypeVar`
- runtime-checkable protocol

Python版では、**型注釈と実行時の挙動を明確に分けること**を重要な教材テーマとします。

mypy や pyright の結果を扱う場合は、Python runtime のテストと静的型検査を別の観測結果として表現してください。

### 9. Async / Concurrency

優先度: B

候補:

- coroutine
- async function
- `await`
- `asyncio.create_task`
- `asyncio.gather`
- cancellation
- async context manager
- async iterator
- threading
- multiprocessing
- GIL

GIL については「Python ではスレッドが並列実行されない」といった過度な単純化を避けてください。

CPU-bound / I/O-bound、CPython 実装、C extension が GIL を解放する場合などを区別し、テストで安定して証明できない主張を教材の断定表現にしないでください。

### 10. Standard Library

優先度: B

標準ライブラリは Python の言語理解や実務バグ防止に直結するものを優先します。

候補:

- `datetime`
- timezone-aware / naive datetime
- `decimal.Decimal`
- `pathlib`
- `collections.defaultdict`
- `collections.Counter`
- `functools.lru_cache`
- `functools.partial`
- `itertools`
- `copy`
- `dataclasses`

API カタログにはしないでください。

---

## テスト方針

標準の `unittest` でも実現できますが、このプロジェクトでは教材としての可読性を優先し、基本的には **pytest** の利用を推奨します。

各教材は、可能な限り次の構造を持たせてください。

- 最小限の Source
- 挙動を固定する Test
- 明確な期待値
- 必要に応じた例外確認
- なぜその結果になるか
- 実務でどこに注意するか

例外確認では `pytest.raises` を利用できます。

テストは以下を満たしてください。

- deterministic である
- 外部ネットワークへ依存しない
- 実時刻へ依存しない
- ランダムな成功を前提にしない
- OS差を無意味に持ち込まない
- CPython の偶然の実装詳細を Python の言語仕様として扱わない

---

## 推奨プロジェクト構成

既存 by-tests シリーズとの統一感を優先してください。

```text
.
├── examples/
│   ├── src/                  # Source として表示する Python コード
│   └── tests/                # pytest で実行するテスト
├── src/
│   ├── components/
│   ├── data/lessons.ts
│   └── pages/
├── docs/
│   └── EXPANSION_GUIDE.md
├── .github/workflows/
├── LEARNING_PATH.md
├── CONTRIBUTING.md
├── pyproject.toml
└── README.md
```

Java / Go / TypeScript 版の UI と設計を参考にして構いませんが、Python の教材内容まで機械的に移植しないでください。

---

## 推奨ツール

実装時点の安定版を確認した上で選定してください。

候補:

- Python 3.13 以降
- pytest
- Ruff
- mypy または pyright
- Astro
- GitHub Actions
- GitHub Pages

ツールを増やすこと自体を目的にしないでください。

最低限、次の品質ゲートを想定します。

```text
format / lint
↓
type check（型教材を扱う場合）
↓
pytest
↓
Astro check
↓
static build
↓
link verification
```

---

## 他の by-tests シリーズとの関係

Java / Go / TypeScript のテーマを Python に機械的に移植しないでください。

重要なのは、**Python で理解する価値が高い挙動を Python らしいコードで確認すること**です。

一方で、次のような比較可能な設計上の問いは各言語版に対応テーマがあっても構いません。

- equality
- identity / reference
- collection
- null / nil / None
- error handling
- mutability
- async / concurrency
- type system
- resource management

例えば Java の `equals`、TypeScript の `===`、Python の `is` / `==` は単純な移植ではなく、「同一性と等価性をどう表現するか」という共通の問いとして扱います。

---

## 初期追加テーマの優先順位

最初から大量に追加しないでください。

まずは次のテーマを優先します。

### Priority A

1. `is` と `==`
2. mutable default argument
3. shallow copy と deep copy
4. list multiplication と参照共有
5. `None` の扱い
6. closure の late binding
7. iterator の消費
8. generator の遅延評価
9. exception chaining
10. context manager
11. class attribute と instance attribute
12. `__eq__` / `__hash__`
13. dataclass
14. type hints は runtime で強制されない
15. `Protocol` / structural typing
16. timezone-aware / naive datetime

### Priority B

- decorator
- property
- MRO / `super()`
- descriptor
- `__slots__`
- `functools.lru_cache`
- `asyncio.gather`
- cancellation
- async iterator
- GIL / threading
- multiprocessing
- Decimal

Priority A を実装した後に、既存テーマの密度とカテゴリバランスを確認してから Priority B を追加してください。

---

## 実装時の指示

新しいテーマを追加するときは、次の順序で進めてください。

1. 既存教材に同じ問いがないか確認する
2. このテーマを一文で説明する
3. Pitfall / Behavior / Concept のどれかを決める
4. テストで観測する具体的な結果を決める
5. 最小の Source を作る
6. pytest で挙動を固定する
7. 教材サイトへ Source / Test / 説明を追加する
8. CI ですべての品質ゲートを通す

テーマ追加PRでは、Source だけ、Test だけ、説明だけを追加しないでください。

表示されるコードと実行されるコードが一致する構造を維持してください。

---

## 最終判断基準

テーマを追加する前に、必ず次の問いを確認してください。

> このテストを見ることで、Python の理解が一段深くなるか？

答えが「単に文法を一つ覚えられるだけ」であれば追加しません。

答えが「挙動を予測できるようになる」「バグを避けられる」「Python の設計思想が分かる」であれば、教材として追加する価値があります。
