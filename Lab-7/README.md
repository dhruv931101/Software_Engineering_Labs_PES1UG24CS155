# PES University Software Engineering Lab 7

**Student:** Dhruv Swatantramath  
**SRN:** PES1UG24CS155  
**Project:** Traffic Fine  
**Topic:** Fuzzing for Input Validation Bugs

## Overview

This lab uses Hypothesis property-based tests to check three input-processing functions from the Traffic Fine starter. `processor_original.py` preserves the unmodified starter for the baseline run. `processor.py` contains the corrected implementation. `test_processor.py` is one suite that can target either module.

| Function | Fixed behavior | Hypothesis coverage in `test_processor.py` |
|---|---|---|
| `parse_ticket_id(ticket_id)` | Accepts `PREFIX-YYYY-SERIAL`, normalizes the prefix, and rejects malformed identifiers and year zero. | `test_parse_ticket_id_returns_normalized_components`, `test_parse_ticket_id_rejects_zero_year`, `test_parse_ticket_id_rejects_unicode_and_wrong_separators`, `test_all_functions_reject_none` |
| `total_fines(amounts_csv)` | Sums comma-separated non-negative integers, treats blank input as zero, and caps the result at 10,000. | `test_total_fines_sums_nonnegative_amounts_and_caps`, `test_total_fines_treats_empty_and_whitespace_as_zero`, `test_total_fines_rejects_negative_amounts`, `test_total_fines_rejects_unicode_or_malformed_tokens`, `test_all_functions_reject_none` |
| `speed_excess(reading)` | Accepts non-negative `SPEED/LIMIT`, requires a positive limit, and returns zero at or below the limit. | `test_speed_excess_is_nonnegative_and_matches_integer_percentage`, `test_speed_excess_rejects_zero_limit`, `test_speed_excess_rejects_negative_speed`, `test_speed_excess_rejects_malformed_unicode_readings`, `test_all_functions_reject_none` |

## Windows PowerShell setup

Python 3.13.15 was used for the verified runs. From this directory:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

The requirements include Hypothesis and pytest for the lab, plus ReportLab and pypdf for building and checking the report.

## Run the assignment workflow

Run the original application and enter the sample values shown below:

```powershell
python processor_original.py
# Ticket ID: TF-2024-0456
# Fines: 500,1200,300
# Speed/limit: 72/60
```

Run the initial property suite against the preserved original implementation:

```powershell
$env:LAB7_USE_ORIGINAL = "1"
python -m pytest -v --tb=no test_processor.py
Remove-Item Env:LAB7_USE_ORIGINAL
```

Run the fixed application with the same sample inputs, then run all properties against `processor.py`:

```powershell
python processor.py
python -m pytest -v test_processor.py
```

The verified baseline collected 14 cases: 10 failed and 4 passed against the original implementation. The verified final run passed all 14 cases against the fixed implementation. The failures exposed zero-year acceptance, malformed/blank fine handling, negative fines, below-limit negative output, division by zero for a zero limit, negative speed acceptance, and missing type validation.

## Evidence and deliverables

The `screenshots/` directory contains the four captured terminal stages in order:

1. `01_original_application.png`
2. `02_initial_fuzz_failures.png`
3. `03_fixed_application.png`
4. `04_final_passing_tests.png`

For compatibility with the filenames in the attached workflow prompt, the baseline and final-test captures are also available as `02_original_failing_tests.png` and `04_passing_tests.png`. These are byte-for-byte copies of the same genuine captures, not additional runs.

`PES1UG24CS155_Lab7.pdf` is the final report. `PES1UG24CS155_Lab7_FuzzTesting.pdf` is a compatibility-named copy of the same report. Both contain the student details, a function-to-test summary, the verified results, and all four screenshots. Run `python build_lab7_pdf.py` to regenerate both PDFs after changing the screenshots or report content. The builder checks the PDF page count, identity text, and one embedded screenshot on each evidence page.

The other academic source deliverables are `processor.py` and `test_processor.py`. The original source remains available as `processor_original.py` to make the baseline reproducible. There is no separate `test_processor_original.py`; the original implementation is selected by the environment variable shown above.
