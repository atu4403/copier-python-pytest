# 変更履歴

このプロジェクトの主要な変更はすべてこのファイルに記録されます。

形式は [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) に基づき、
バージョニングは [Semantic Versioning](https://semver.org/spec/v2.0.0.html) に準拠しています。

## [Unreleased]

## [0.1.1] - 2025-06-11

### 修正 / Fixed
- READMEのコマンド例に不足していた `--trust` フラグを追加
- 信頼性検証エラーを引き起こすコマンド例を修正

## [0.1.0] - 2025-06-11

### 追加 / Added
- copier-python-pytest テンプレートの初回リリース
- conftest.py と pytest.ini を含む pytest 環境のセットアップ
- Click フレームワークによるオプションのCLIサポート
- uv との互換性と統合
- uv タスクによる自動依存関係管理
- `copier update` によるテンプレート更新サポート
- クイックスタートガイド付きの包括的なREADME
- MIT ライセンス
- テンプレートテスト用の GitHub Actions ワークフロー

### 機能 / Features
- ライブラリ型とCLI型の両プロジェクトタイプをサポート
- テストインフラを追加しながら uv 生成の pyproject.toml を保持
- スマートなファイル競合解決ガイダンス
- テンプレートのバージョニングと更新機能
