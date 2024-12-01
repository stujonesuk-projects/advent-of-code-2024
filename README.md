# Advent of Code 2024

## Input Files
Drop input files into `./input/` named `day01`, `day02`, `day03` etc...

## Sample Inputs
Drop sample input files into `./sample-input/` named `day01`, `day02`, `day03` etc...

If there are different sample inputs for Part 1 and Part 2 on a given day, suffix the filename with `-1` or `-2`

## Running Solutions
Run `./aoc` with the following parameters:

* `--day` or `-d` - the number of the day to run - if ommitted, will try to run days 1-25 inclusive.
* `--part` or `-p` - the part number to run - if ommitted, will try to run both parts on the included days.
* `--sample` or `-s` - run with sample inputs - if ommitted will run with real inputs.

## Solution Files
Are stored in `./solutions/dayXX/` where `XX` is the day number, zero-padded.

* `part-one.py` - the solution to Part One on Day `XX`
* `part-two.py` - the solution to Part Two on Day `XX`

Solution files contain a solution function `answer` which takes a list of strings contained in the input file, and returns the answer.

The `aoc` solution runner locates the relevant input files, reads them line-by-line, and passes the lines to the solution function.
