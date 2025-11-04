"""Command-line entry and small wrapper used by tests.

This module exposes a `download_album()` function that reads user input
and delegates the real work to `src.jmcomic_client.download_album`.
The `main()` function is kept as the CLI entrypoint.
"""
from typing import Optional

from . import jmcomic_client


def download_album() -> None:
    """Prompt user for an album identifier and call the client wrapper.

    This function is used by unit tests (they patch `input` and
    `src.jmcomic_client.download_album`).
    """
    album = input("请输入 album 名称或 ID: ").strip()
    if not album:
        print("未输入 album，取消。")
        return

    try:
        jmcomic_client.download_album(album)
        print("下载已触发（查看 jmcomic 的输出/目录以确认）")
    except Exception as exc:
        print("下载失败：", exc)


def main(argv: Optional[list] = None) -> None:
    """CLI entrypoint retained for console script usage."""
    download_album()


if __name__ == "__main__":
    main()