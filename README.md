# copier-python-pytest

uvで作成したPythonプロジェクトにpytest環境とCLI機能を追加するCopierテンプレートです。

## クイックスタート

```bash
# 1. プロジェクト作成
uv init --lib my_awesome_project

# 2. テンプレート適用
copier copy gh:atu4403/copier-python-pytest my_awesome_project --trust
# ファイル競合時は以下を選択：
# - README.md → Yes（テンプレートで上書き）
# - .gitignore → Yes（テンプレートで上書き）

# 3. プロジェクトに移動
cd my_awesome_project

# 4. CLI設定追加（CLI機能を有効にした場合）
echo '[project.scripts]' >> pyproject.toml
echo 'mycmd = "my_awesome_project.cli:main"' >> pyproject.toml
uv sync

# 5. 開発開始
source .venv/bin/activate
pytest                    # テスト実行
mycmd --help             # CLI確認（CLI有効時）
```

## プロジェクト更新

```bash
cd my_awesome_project
copier update
```

---

## 詳細説明

## 初回適用時のファイル競合について

テンプレート適用時、以下のファイルでuvが作成したファイルとの競合が発生します：

- **README.md** → `Yes`を選択（プロジェクト向けREADMEに置き換え）
- **.gitignore** → `Yes`を選択（Python開発用.gitignoreに置き換え）

**uvが作成したpyproject.tomlは競合せず、そのまま保持されます。**

- ✅ **pytest テストフレームワーク**の完全セットアップ
- ✅ **Click CLI フレームワーク**のサポート（オプション）
- ✅ **uv**との完全互換性
- ✅ プロジェクト更新機能（`copier update`）

### 前提条件

- [uv](https://docs.astral.sh/uv/) がインストールされていること
- [copier](https://copier.readthedocs.io/) がインストールされていること

```bash
# copierのインストール
uv tool install copier
```

### 使用方法

#### 1. uvでプロジェクトを初期化

```bash
uv init --lib my_awesome_project
```

#### 2. テンプレートを適用

```bash
copier copy gh:atu4403/copier-python-pytest my_awesome_project --trust
```

**📋 ファイル競合時の対応:**

テンプレート適用時に以下のような質問が表示されます：

```
conflict  README.md
? Overwrite README.md? Yes  ← Yesを選択（テンプレート版を使用）

conflict  .gitignore  
? Overwrite .gitignore? Yes  ← Yesを選択（テンプレート版を使用）
```

**💡 テンプレート適用時の質問:**

1. プロジェクトの基本情報（プロジェクト説明、作者名、メールアドレス、GitHubユーザー名）
2. CLI機能の有無とコマンド名
3. **ファイル競合の確認**（上記の通りYesを選択）

### 特徴

#### 3. プロジェクトディレクトリに移動

```bash
cd my_awesome_project
```

#### 4. CLI設定の追加（CLI機能を有効にした場合）

`pyproject.toml`に以下を追加してください：

```toml
[project.scripts]
mycmd = "my_awesome_project.cli:main"
```

**重要**: 設定追加後は依存関係を同期してください：

```bash
uv sync
```

#### 5. 開発開始

```bash
# 仮想環境をアクティベート
source .venv/bin/activate

# テスト実行
pytest

# CLI機能をテスト（有効にした場合）
mycmd --help
```

### 作成されるファイル

```
my_awesome_project/
├── pytest.ini              # pytest設定
├── tests/                   # テストディレクトリ
│   ├── __init__.py
│   ├── conftest.py          # pytest共通設定
│   └── test_example.py      # サンプルテスト
├── src/my_awesome_project/
│   ├── cli.py              # CLIエントリーポイント（CLI有効時）
│   └── commands/           # CLIコマンド（CLI有効時）
│       └── hello.py
├── LICENSE                 # MITライセンス
├── CHANGELOG.md           # 変更履歴
└── .copier-answers.yml    # テンプレート設定
```

### プロジェクトの更新

テンプレートが更新された場合、既存のプロジェクトを最新版に更新できます：

```bash
cd my_awesome_project
copier update
```

これにより：
- ✅ pytest設定やテストファイルが最新版に更新
- ✅ README.mdやpyproject.tomlなどのカスタマイズ済みファイルは保護
- ✅ 新機能が自動的に追加

### 開発ワークフロー

#### テストの実行

```bash
# 全テスト実行
pytest

# 詳細表示
pytest -v

# カバレッジ付き（将来のバージョンで対応予定）
pytest --cov=my_awesome_project
```

#### 依存関係の管理

```bash
# 新しいパッケージを追加
uv add requests

# 開発用パッケージを追加
uv add --dev black

# 依存関係を同期
uv sync
```

#### CLI開発（CLI機能有効時）

新しいコマンドを追加する場合：

1. `src/my_awesome_project/commands/`に新しいファイルを作成
2. `src/my_awesome_project/cli.py`にコマンドを登録
3. `uv sync`で依存関係を更新

## ライセンス

このテンプレートはMITライセンスの下で公開されています。

## 貢献

Issue報告やPull Requestを歓迎します！

---

*このテンプレートを使用して作成されたプロジェクトには、このREADMEは含まれません。プロジェクト固有のREADMEが生成されます。*
