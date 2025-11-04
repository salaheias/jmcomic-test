# jmcomic-downloader

Simple CLI wrapper around the `jmcomic` PyPI package. It provides:

- `src/jmcomic_client.py`: compatibility wrapper calling the real `jmcomic` API.
- `src/main.py`: small CLI and `download_album()` helper used by unit tests.

Usage:

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the CLI:

```bash
python -m src.main
```

Or import `download_album` from `src.main` in tests and mock `src.jmcomic_client.download_album`.
# jmcomic-downloader

## 项目简介
jmcomic-downloader 是一个用于下载漫画相册的 Python 应用程序，利用 `jmcomic` 库实现相册的下载功能。

## 目录结构
```
jmcomic-downloader
├── src
│   ├── main.py          # 应用程序入口，接收用户输入并下载相册
│   ├── jmcomic_client.py # 封装与 jmcomic 库的交互逻辑
│   └── __init__.py      # 将 src 目录标记为一个包
├── tests
│   └── test_main.py     # 对 main.py 的单元测试
├── requirements.txt      # 项目所需的依赖项
├── pyproject.toml       # 项目的配置文件
├── .gitignore            # 版本控制中应忽略的文件和目录
└── README.md             # 项目文档
```

## 安装依赖
在项目根目录下运行以下命令以安装所需的依赖项：
```
pip install -r requirements.txt
```

## 使用方法
1. 运行应用程序：
   ```
   python src/main.py
   ```
2. 按照提示输入相册信息，程序将自动下载相册。

## 贡献
欢迎提交问题和贡献代码！请遵循项目的贡献指南。

## 许可证
该项目遵循 MIT 许可证。