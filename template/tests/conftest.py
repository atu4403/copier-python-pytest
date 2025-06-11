"""pytest設定

このファイルには以下が含まれています:
- プロジェクト全体で使用する基本的なフィクスチャ
- pytest の設定とカスタムマーカー
- テスト実行オプションの定義

新しいフィクスチャが必要な場合は、このファイルまたは
個別のテストファイル内に定義してください。
"""

import pytest


def pytest_addoption(parser):
    """pytestコマンドラインオプションを追加"""
    parser.addoption("--run-slow", action="store_true", help="時間のかかるテストも実行する")


def pytest_collection_modifyitems(config, items):
    """テスト収集時の処理をカスタマイズ"""
    if not config.getoption("--run-slow"):
        skip_slow = pytest.mark.skip(reason="--run-slow オプションが必要です")
        for item in items:
            if "slow" in item.keywords:
                item.add_marker(skip_slow)


def pytest_configure(config):
    """pytest設定のカスタマイズ"""
    # カスタムマーカーを登録
    config.addinivalue_line("markers", "slow: 時間のかかるテストをマークする")
    config.addinivalue_line("markers", "integration: 結合テストをマークする")
    config.addinivalue_line("markers", "unit: 単体テストをマークする")


@pytest.fixture
def mock_client(mocker):
    """APIクライアントのモックを提供する

    テスト用の基本的なAPIモックです。
    必要に応じて戻り値を設定してください。

    Args:
        mocker: pytest-mockのmockerフィクスチャ

    Returns:
        Mock: APIクライアントのモック

    Example:
        def test_api_call(mock_client):
            mock_client.get.return_value = {"status": "ok"}
            result = mock_client.get("/api/test")
            assert result["status"] == "ok"
    """
    mock = mocker.Mock()
    mock.get.return_value = {"status": "success"}
    mock.post.return_value = {"id": 1, "created": True}
    return mock
