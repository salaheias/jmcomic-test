"""Compatibility wrapper around the third-party `jmcomic` package.

This module isolates real jmcomic usage so unit tests can mock
`src.jmcomic_client.download_album` without importing the actual package.

The wrapper tries a few common API shapes to be tolerant across jmcomic
versions. If `jmcomic` is not installed, it raises ImportError.
"""
from typing import Optional


def download_album(album: str, dest: Optional[str] = None) -> None:
    """Attempt to download an album using the installed `jmcomic` package.

    The function will try a few possible APIs:
    - module-level `download_album(album, dest=...)`
    - `jmcomic.Client()` instance methods like `download_album` or `download`

    Raises RuntimeError if it cannot find a usable API.
    """
    try:
        import jmcomic
    except Exception as e:
        raise ImportError("请先安装 jmcomic：pip install jmcomic") from e

    # 1) try module-level function
    if hasattr(jmcomic, "download_album"):
        fn = getattr(jmcomic, "download_album")
        try:
            if dest is None:
                return fn(album)
            return fn(album, dest=dest)
        except TypeError:
            return fn(album)

    # 2) try Client class
    if hasattr(jmcomic, "Client"):
        Client = getattr(jmcomic, "Client")
        client = Client()
        if hasattr(client, "download_album"):
            fn = getattr(client, "download_album")
            try:
                if dest is None:
                    return fn(album)
                return fn(album, dest=dest)
            except TypeError:
                return fn(album)
        if hasattr(client, "download"):
            fn = getattr(client, "download")
            try:
                if dest is None:
                    return fn(album)
                return fn(album, dest)
            except TypeError:
                return fn(album)

    raise RuntimeError("无法识别 jmcomic 的 API，请检查该包的文档或源码。")
class JMComicClient:
    def __init__(self):
        import jmcomic

    def download_album(self, album_id):
        try:
            album = jmcomic.get_album(album_id)
            if album:
                album.download()
                return True
            else:
                return False
        except Exception as e:
            print(f"Error downloading album: {e}")
            return False