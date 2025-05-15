"""
MX-Font
Copyright (c) 2021-present NAVER Corp.
MIT license
"""

import argparse
from tqdm import tqdm
from pathlib import Path
import os

from datasets import get_filtered_chars


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root_dir")
    args = parser.parse_args()

    print(args.root_dir)
    ttffiles = list(Path(args.root_dir).rglob("*.ttf"))

    for ttffile in tqdm(ttffiles):
        filename = ttffile.stem
        dirname = ttffile.parent
        avail_chars = get_filtered_chars(ttffile)
        txt_name = dirname / (filename+".txt")
        if os.path.exists(txt_name):
            continue
        with open((txt_name), "w") as f:
            f.write("".join(avail_chars))


if __name__ == "__main__":
    main()
