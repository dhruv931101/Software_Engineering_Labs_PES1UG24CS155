# Lab 6 — Code Coverage

**Student:** Dhruv Swatantramath  
**SRN:** PES1UG24CS155  
**Course:** Software Engineering

This standalone submission contains the assigned Traffic Fine Calculator source, a dedicated pytest suite for code/statement coverage, and its analysis. The source is copied from `SETAPESU26/L6_L7_27_traffic_fine` (`lab6/traffic_fine.py`) without business-logic changes.

## Code coverage result

The separate code coverage run passed **29 tests** and covered **35/35 statements (100%)** in `traffic_fine.py`. The command and coverage definition are in [coverage_analysis.md](coverage_analysis.md).

## Run

```powershell
python -m pip install -r requirements.txt
python -m coverage erase
python -m coverage run --source=traffic_fine -m pytest -v CodeCoverageTest_PES1UG24CS155_application.py
python -m coverage report -m
```

The branch coverage suite and its independently calculated result are added in the following branch-coverage commit.
