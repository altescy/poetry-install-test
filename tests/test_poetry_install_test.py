import poetry_install_test


def test_version() -> None:
    assert poetry_install_test.__version__ == "0.1.0"
