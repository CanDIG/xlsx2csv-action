import argparse
import os
from xlsx2csv import Xlsx2csv

def main():
    parser = argparse.ArgumentParser(description="Convert an xlsx file's sheets to individual csv files")

    parser.add_argument("input_file", help="xlsx file to convert")
    parser.add_argument("output_dir", help="name of directory for output")

    args = parser.parse_args()
    input_file = args.input_file
    output_dir = f"{os.environ.get('GITHUB_WORKSPACE')}/{args.output_dir}"
    Xlsx2csv(input_file, outputencoding="utf-8").convert(output_dir, sheetid=0)


if __name__ == "__main__":
    main()
