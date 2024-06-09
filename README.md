# CSV CHANGER
### This is a CLI tool to change measurement comments in .csv files by values from a source .txt file

## Format of source TXT file:
- 2nd line and following must have the expected values
- If there is only one value, the line must end with ";"

Example:
```
SOME FIRST LINE
**0.123;0.745;**1.745
1.976;0.345;2.445;
0.453;
0.697;1.863
```

## Format of CSV files to be changed:
- The name must have an identifier in ascending order like "csv_file_0001.csv", "csv_file_0002.csv"
- The first line should be a comment - be sure, as this line will be replaced!

Example:
```
;This first line has the comment to be replaced;
OTHER LINE
ANOTHER LINE
```

### On this basis the tool will sort all csv files by their name and will rewrite the first line according to the order of values from the source file

## Install

Use must have Python installed [Python Install](https://www.python.org/downloads/)\
Then execute this command anywhere in you preferred terminal:
```
pip install git+https://github.com/ken0876/csv
```
# :beaver: Bober Kurwa