import fastapi_class

__version__ = "3.4.0"


def test_version() -> None:
    assert fastapi_class.__version__ == __version__
