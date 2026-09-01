# Learning Path

Python by Tests は、解説だけを先に読む教材ではありません。各記事で **Source → pytest → 観測結果** の順に読み、実行結果を予測してからテストを動かします。

## 1. 同一性と参照共有

- `is` と `==`
- `None` の判定
- list multiplication による入れ子の参照共有
- shallow copy と deep copy
- mutable default argument

Pythonで「同じに見える値」と「同じobject」がずれる場面を先に押さえます。

## 2. 評価タイミングと消費

- closure の late binding
- iterator の消費
- generator の遅延評価と一度きりの消費

値がいつ束縛・評価・消費されるかを、短いテストで観測します。

## 3. 失敗を追跡し、境界を閉じる

- exception chaining
- context manager
- timezone-aware / naive datetime

例外の原因、リソースの解放、日時の比較可能性を、境界の契約として扱います。

## 4. object modelと型の契約

- class attribute と instance attribute
- `__eq__` / `__hash__`
- dataclass
- type hints とruntime
- Protocol

classの属性解決と、静的型検査・runtimeの役割の違いを区別します。

## 実行

```bash
python -m pytest
pnpm build
```
