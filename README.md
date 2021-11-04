# xlsx2csv-action

This action converts the individual sheets of a single xlsx file into individual csv files.

## Inputs

## `input_file`

**Required** The xlsx file to convert.

## `output_dir`

**Required** The directory for the outputted csv files.

## Example usage

uses: daisieh/xlsx2csv-action
with:
    input_file: 'test.xlsx'
    output_dir: 'untitled'