# Lab 6 Coverage Analysis — Traffic Fine Calculator

**Student:** Dhruv Swatantramath
**SRN:** PES1UG24CS155
**Course:** Software Engineering
**Lab:** Lab 6 — Code and Branch Coverage Analysis

## Application

`traffic_fine.py` provides `speeding_fine`, `license_action`, and `total_penalty`. It calculates a fine based on speeding amount and zone, determines a licence action from penalty points, and sums fines while rejecting negative amounts and capping the total at 10,000. The assigned source repository is `SETAPESU26/L6_L7_27_traffic_fine`, file `lab6/traffic_fine.py`. Its business logic was preserved.

## Coverage measures

Statement (code) coverage measures executable statements reached during a run. Branch coverage measures the possible control-flow outcomes taken from decisions, including both sides of conditions and loop entry/exit. Statement coverage alone can miss an untested decision outcome.

Coverage.py's combined total in a branch-enabled run treats executed statements and branches as coverage opportunities. It is reported separately below from the independently calculated branch percentage.

## Commands

Code/statement coverage was measured in its own run:

```powershell
coverage erase
coverage run --source=traffic_fine -m pytest -v CodeCoverageTest_PES1UG24CS155_application.py
coverage report -m
```

Branch coverage was measured in a separate run, followed by the required JSON report:

```powershell
coverage erase
coverage run --branch --source=traffic_fine -m pytest -v BranchCoverageTest_PES1UG24CS155_application.py
coverage report -m
coverage json -o branch_coverage.json
```

The executed environment used Python 3.13.15, pytest 9.2.0, and coverage.py 7.17.2.

## Results

### Code/statement coverage run

- Tests passed: **29**.
- `traffic_fine.py`: **35 of 35 statements**, **100% statement/code coverage**.
- Missing statements: **0**.

### Branch coverage run

- Tests passed: **19**.
- Statement coverage in this branch-enabled run: **35 of 35 = 100%**.
- Branches covered: **26 of 26**.
- Independently calculated branch coverage: `(26 / 26) × 100 = 100%`.
- Missing branches: **0**; `branch_coverage.json` has an empty `missing_branches` list.
- Partial branches: **0**.
- Combined coverage.py total: **100%** (61 of 61 statement-plus-branch opportunities).

The JSON totals are the basis for the independent calculation. No lines or branches were excluded, and no coverage configuration was changed to hide code.

## Test cases

The code suite checks speeding below/at/above the limit, all zones, excess speeds at and around 20 and 40, licence point boundaries and licence types, empty/single/multiple fine lists, zero, values below/at/above the cap, and negative fines including after valid fines.

The branch suite independently exercises both outcomes of the speed-limit, zone, excess-speed, licence-point, commercial-licence, repeat-offender, negative-fine, and cap decisions. It also tests an empty list (loop not entered) and a non-empty list (loop entered and terminated).

## Uncovered code and evidence

There are no uncovered statements or branches in either reported run. The assignment requires terminal screenshots named `screenshots/code_coverage_terminal.png` and `screenshots/branch_coverage_terminal.png`. Those files are not included because the available environment exposes no allowed terminal screenshot capture route. The tests and report commands did execute successfully; this limitation is stated instead of fabricating screenshots.
