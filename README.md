# data-structure-and-algorithm

## Initialising the project

I used `conda` to manage the virtual environment. So, run the following to start:

```
conda env create -f environment.yml
conda activate dsa
python -m pip install -e .
```

Then, run all tests with 

```
python -m pytest
```

Or, run individual test cases with

```
python -m pytest tests/<test file name>.py
```