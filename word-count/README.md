## Install all dependencies
```bash
poetry install
```

## Run tests
To run all tests:
```bash
make tests
```
## Create package
This will create a `tar.gz` and a `.wheel` in `dist/` folder:
```bash
poetry build
```
More: https://python-poetry.org/docs/cli/#build

## Run style checks
```bash
make style-checks
```
This is running the linter and a type checker.

## Word Count Job
This job will count the occurrences of a word within the given text file.

#### Input
Simple `*.txt` file containing text.

#### Output
A single `*.csv` file containing data similar to:
```csv
"word","count"
"a","3"
"an","5"
...
```
#### Run the job
Please make sure to package the code before submitting the spark job (`poetry build`)
```bash
poetry run spark-submit \
    --master local \
    --py-files dist/data_transformations-*.whl \
    jobs/word_count.py \
    <INPUT_FILE_PATH> \
    <OUTPUT_PATH>
```
