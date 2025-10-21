import argparse
import os
import sys
from file_deleter_by_file_suffix import FileDelBySuf

def parse_args():
    p = argparse.ArgumentParser(description="Delete files by suffix (default: dry-run). Use --execute to actually delete.")
    p.add_argument("path", help="target path (file or directory)")
    p.add_argument("suffixes", nargs="+", help="file suffixes to delete, e.g. .log .tmp or log tmp")
    p.add_argument("--execute", action="store_true", help="actually delete files (default is dry-run)")
    p.add_argument("-y", "--yes", action="store_true", help="skip confirmation when executing")
    return p.parse_args()

def main():
    args = parse_args()
    path = os.path.abspath(args.path)
    if not os.path.exists(path):
        print(f"Path not found: {path}")
        return 2

    deleter = FileDelBySuf()
    deleter.setSuffixs(args.suffixes)
    deleter.setDryRun(not args.execute)

    mode = "EXECUTE" if args.execute else "DRY-RUN"
    print(f"Mode: {mode}. Target: {path}. Suffixes: {args.suffixes}")

    if args.execute and not args.yes:
        ans = input("Proceed to delete files? [y/N]: ")
        if ans.lower() not in ("y", "yes"):
            print("Cancelled")
            return 0

    deleter.fileTraversal(path)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())