# xlsx2csv-action

This action converts the individual sheets of a single xlsx file into individual csv files. 
If provided with a directory, searches the directory recursively for xlsx files to convert.

Converted files are stored as separate csv files in a directory of the same name as the xlsx file.

## Inputs

## `input_file`

**Required** The xlsx file to convert or the directory to search for xlsx files to convert.

## Example usage

```
uses: daisieh/xlsx2csv-action
with:
    input_file: 'test.xlsx'
```
