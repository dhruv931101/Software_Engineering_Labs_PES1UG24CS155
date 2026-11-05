# Lab 6 Code Coverage Analysis — Traffic Fine Calculator

**Student:** Dhruv Swatantramath  
**SRN:** PES1UG24CS155  
**Course:** Software Engineering  
**Lab:** Lab 6 — Code and Branch Coverage Analysis

## Application

`traffic_fine.py` contains `speeding_fine`, `license_action`, and `total_penalty`. It calculates a speeding fine by zone and excess speed, decides a licence action from penalty points, and totals nonnegative fines up to a 10,000 cap. The assigned source repository is `SETAPESU26/L6_L7_27_traffic_fine`, file `lab6/traffic_fine.py`. Its business logic was preserved.

## Code/statement coverage

Statement coverage measures executable statements reached during a test run. In the independent code-coverage run, **29 tests passed** and `traffic_fine.py` had **35/35 statements covered (100%)**, with no missing lines.

Command:

```powershell
coverage erase
coverage run --source=traffic_fine -m pytest -v CodeCoverageTest_PES1UG24CS155_application.py
coverage report -m
```

The branch coverage suite and JSON-based branch calculation will be added in the second commit.
