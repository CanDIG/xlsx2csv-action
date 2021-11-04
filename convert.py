import argparse
import os
import re
import shutil
from xlsx2csv import Xlsx2csv


def main():
    parser = argparse.ArgumentParser(description="Convert all xlsx files in a directory (or a single xlsx file) to individual csv files")

    parser.add_argument("input", help="directory or file")

    args = parser.parse_args()
    if os.path.isfile(args.input):
        file_match = re.match("(.+)\.xlsx$", args.input)
        if file_match is not None:
            output_dir = f"{os.environ.get('GITHUB_WORKSPACE')}/{file_match.group(1)}"
            if os.path.exists(output_dir):
                shutil.rmtree(output_dir)
            Xlsx2csv(args.input, outputencoding="utf-8").convert(output_dir, sheetid=0)
    else:
        dirlist = [args.input]
        files = []
        while len(dirlist) > 0:
            for (dirpath, dirnames, filenames) in os.walk(dirlist.pop()):
                dirlist.extend(dirnames)
                files.extend(map(lambda n: os.path.join(*n), zip([dirpath] * len(filenames), filenames)))
        for file in files:
            file_match = re.match("(.+)\.xlsx$", file)
            if file_match is not None:
                output_dir = f"{os.environ.get('GITHUB_WORKSPACE')}/{file_match.group(1)}"
                Xlsx2csv(file, outputencoding="utf-8").convert(output_dir, sheetid=0)


if __name__ == "__main__":
    main()
