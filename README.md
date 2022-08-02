# Calculate vested shares

This package calculates vested shares for an organization.
The main file is vesting_program.py file. It takes 3 arguments
- Arg1: filepath
- Arg2: date (YYYY-MM-DD)
- Arg3: precision (optional field)


### Usage
```
./vesting_program.py --help
```

## Running script
open terminal and cd into the project directory
```
./vesting_program.py filepath/filename.csv date
```

I have included a few test files to run the program with.

- run `./vesting_program.py tests/example1.csv 2021-01-01` to test example1.csv file

Please replace example1.csv with other files you would like to test from.


If you would like to write the data to a new csv output file then please uncomment the last two lines of vesting_program.py file.

```
f = File()
f.write_data_to_csv(vested_share_data)
```

## To run tests
I have also added a few test cases to to test different functions and inputs of the program
- run `./test.py -b`


## To get doc strings of all classes and methods
- run `./doc_strings.py`



## Sub modules
I have created 3 sub modules: helper, validator and default

### helper module
- It has classes and methods to help with file class like opening, reading data, writing data to another file and closing.

- It also has helper classes to calculate toatal share based on some share event.

- It helps generating precise number without rounding off



### validator module
- This submodule helps with input parameters and rows of the input file


### default module
- Generates default values of vested shares.

