# FileDeleterByFileSuffix

中文（Chinese）
---------------

运行环境
- Python: 3.13.5（建议使用该版本以避免兼容性问题）
- 操作系统: Windows（示例命令基于 PowerShell）

简介
- 一个按文件后缀删除文件的小工具。默认以 dry-run 模式运行（仅列出将要删除的文件），只有在命令行加上 `--execute` 时才真正删除文件。

主要特性
- 必填目标路径（文件或目录）。
- 支持传入一个或多个后缀（位置参数），后缀可带或不带前导点（例如 `.log` 或 `log`）。
- 大小写敏感（`LOG` 与 `log` 被视为不同后缀）。
- 支持复合后缀（例如 `tar.gz`），复合后缀需作为单个参数传入（例：`tar.gz` 或 `.tar.gz`）。
- 默认安全：未指定 `--execute` 时为 dry-run，仅打印不会删除。
- 可使用 `-y/--yes` 跳过交互确认（用于自动化脚本）。

安装与运行（Windows）
- 直接以 Python 运行仓库中的 main.py：
  - 列出将被删除的文件（dry-run，默认）：
    ```powershell
    python main.py C:\path\to\target .log .tmp
    ```
  - 实际删除（需确认或用 -y 跳过）：
    ```powershell
    python main.py C:\path\to\target .log .tmp --execute
    python main.py C:\path\to\target .log .tmp --execute -y
    ```
- 复合后缀示例（删除 `.tar.gz` 文件）：
  ```powershell
  python main.py C:\path .tar.gz --execute
  ```

注意事项
- 默认行为为 dry-run，请确认输出无误后再加 `--execute`。
- 复合后缀应作为单个参数传入（例如 `tar.gz` 或 `.tar.gz`），否则可能无法匹配。
- 程序对后缀匹配保持大小写敏感，如需不敏感请在代码中做小写规范化。
- 在自动化场景使用 `-y` 时请小心：该选项会跳过删除确认。

English
-------

Environment
- Python: 3.13.5 (recommended)
- OS: Windows (example commands use PowerShell)

Overview
- A small tool to delete files by suffix. Runs in dry-run mode by default (only lists files to be deleted). Files are actually removed only when `--execute` is supplied.

Key features
- Path (file or directory) is required.
- Provide one or more suffixes as positional arguments (with or without leading dot, e.g. `.log` or `log`).
- Case-sensitive suffix matching (`LOG` ≠ `log`).
- Supports composite suffixes (e.g. `tar.gz`) — pass composite suffix as a single argument.
- Safe default: dry-run unless `--execute` is present.
- Use `-y/--yes` to skip interactive confirmation (useful for scripts/CI).

Usage (Windows examples)
- Dry-run (default):
  ```powershell
  python main.py C:\path\to\target .log .tmp
  ```
- Execute (actually delete):
  ```powershell
  python main.py C:\path\to\target .log .tmp --execute
  python main.py C:\path\to\target .log .tmp --execute -y
  ```
- Composite suffix example (delete `.tar.gz`):
  ```powershell
  python main.py C:\path .tar.gz --execute
  ```

Notes
- Default is dry-run. Verify output before using `--execute`.
- Composite suffixes should be passed as a single argument (e.g. `tar.gz` or `.tar.gz`) to match correctly.
- Matching is case-sensitive; normalize to lower-case in code if you want case-insensitive behavior.
- Be careful when using `-y` in automated runs since it skips confirmation.

License / 许可证
- 本项目使用 MIT 许可证，详情请参见仓库中的 LICENSE 文件。
- 版权：Copyright (c) 2025 github:Apprentice-Geo

- This project is licensed under the MIT License — see the LICENSE file in the repository for details.
- Copyright (c) 2025 github:Apprentice-Geo