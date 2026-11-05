# Lab 6 — Code and Branch Coverage

**Student:** Dhruv Swatantramath
**SRN:** PES1UG24CS155
**Course:** Software Engineering

This folder contains a standalone copy of the assigned Traffic Fine Calculator, separate pytest suites for statement and branch coverage, and the coverage analysis. The application source is copied from `SETAPESU26/L6_L7_27_traffic_fine` (`lab6/traffic_fine.py`) without changing its business logic.

## Results

| Measurement | Result |
|---|---:|
| Statement/code coverage (code-coverage run) | 35/35 statements — **100%** |
| Branch coverage (branch run, calculated from JSON) | 26/26 branches — **100%** |
| Combined coverage.py total (branch run) | 61/61 opportunities — **100%** |

The branch run reported zero missing statements, zero partial branches, and an empty `missing_branches` list in `branch_coverage.json`. The figures and commands are explained in [coverage_analysis.md](coverage_analysis.md).

## Run

Install dependencies with `python -m pip install -r requirements.txt`, then run the two independent commands from this directory:

```powershell
python -m coverage erase
python -m coverage run --source=traffic_fine -m pytest -v CodeCoverageTest_PES1UG24CS155_application.py
python -m coverage report -m

python -m coverage erase
python -m coverage run --branch --source=traffic_fine -m pytest -v BranchCoverageTest_PES1UG24CS155_application.py
python -m coverage report -m
python -m coverage json -o branch_coverage.json
```

## Screenshot evidence

The assignment requires `screenshots/code_coverage_terminal.png` and `screenshots/branch_coverage_terminal.png`. They are not included in this upload: the available environment does not provide an allowed way to capture the terminal UI, and no screenshot has been fabricated. The successful test and report output was verified through the executed commands; see `coverage_analysis.md`.
