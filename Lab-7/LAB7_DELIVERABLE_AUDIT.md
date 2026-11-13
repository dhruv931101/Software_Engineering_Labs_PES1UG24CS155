# Lab 7 Deliverable Audit

**Student:** Dhruv Swatantramath  
**SRN:** PES1UG24CS155  
**Project:** Traffic Fine  
**Required directory:** `Software_Engineering_Labs_PES1UG24CS155/Lab-7/`  
**Audit date:** 2026-11-13

This audit separates the requirements in the supplied assignment handout and roster from the user's additional file-name, directory, and verification requirements. The handout calls for the original-app run, an initial failing Hypothesis run, a fixed-app run, a passing test run, screenshots, and three academic deliverables. The roster maps this SRN and student to the Traffic Fine project. The exact `Lab-7` name, four screenshot names, audit file, and Git workflow are user-specified additions.

| Requirement | File or location | Status | Verification |
|---|---|---|---|
| Submission directory is named exactly `Lab-7` | `Software_Engineering_Labs_PES1UG24CS155/Lab-7/` | Verified | Inspected the folder name in the workspace. |
| Python is available and environment created | `.venv/` in `Lab-7/` | Verified | `python --version` and `py --version` reported Python 3.13.15. Created a venv from that installed interpreter and ran commands through `.venv\Scripts\python.exe`. |
| Required packages are installed | `requirements.txt`; `.venv/` | Verified | `pip install -r requirements.txt` completed. The pytest output reports pytest 9.2.0 and Hypothesis 6.170.15. ReportLab 5.1.0 and pypdf 7.0.1 were installed for PDF creation and verification. |
| Hypothesis and pytest listed | `requirements.txt` | Verified | Both dependencies are explicitly listed. ReportLab and pypdf are included for the reproducible PDF builder and its structural checks. |
| Original buggy application preserved | `processor_original.py` | Verified | Inspected starter source and ran it with the sample inputs before and after preserving the original file. |
| Fixed application is a separate executable source file | `processor.py` | Verified | Ran `processor.py` interactively; it produced `('TF', 2024, 456)`, total fines `2000`, and speed excess `20` for the sample values. |
| Updated Hypothesis tests are a separate source file | `test_processor.py` | Verified | Pytest collected and executed 14 test cases against both implementations. |
| Optional separate original test module | `test_processor_original.py` | Not present; not required | Inspected the directory. `test_processor.py` selects the original source using `LAB7_USE_ORIGINAL=1`, so there is no duplicate test module. |
| All tested functions explicitly named and mapped to Hypothesis coverage | `README.md`; `test_processor.py`; PDF page 1 | Verified | The three functions are `parse_ticket_id`, `total_fines`, and `speed_excess`. README and PDF map each to their individual properties and shared None-type test. |
| Genuine original application capture | `screenshots/01_original_application.png` | Verified | Captured from the VS Code PowerShell terminal after running `processor_original.py`; image shows command, inputs, and output. |
| Genuine initial failing tests against original implementation | `screenshots/02_initial_fuzz_failures.png` | Verified | `LAB7_USE_ORIGINAL=1` selected `processor_original.py`. Pytest genuinely reported **10 failed, 4 passed** out of 14. The terminal capture shows the command, test names, failure details, and summary. |
| Initial failures expose original defects | `processor_original.py`; `test_processor.py`; screenshot 02 | Verified | Failures include zero-year acceptance, malformed/blank fine handling, negative-fine acceptance, negative below-limit speed output, zero-limit division, negative speed, and missing type validation. |
| Genuine fixed application capture | `screenshots/03_fixed_application.png` | Verified | Captured from the VS Code PowerShell terminal after running `processor.py`; image shows command, inputs, and output. |
| Final Hypothesis suite passes against fixed app and covers all three functions | `test_processor.py`; `screenshots/04_final_passing_tests.png` | Verified | Cleared `LAB7_USE_ORIGINAL`, ran pytest against `processor.py`; all **14 passed**. The output includes properties for each function. |
| Four required genuine screenshots exist | `screenshots/` | Verified | The four required PNG files exist and were visually checked. The PDF contains one screenshot on each of pages 2–5. |
| Screenshot aliases in the attached workflow prompt | `screenshots/02_original_failing_tests.png`; `screenshots/04_passing_tests.png` | Verified | Each is a byte-for-byte copy of the corresponding genuine baseline/final test capture listed above, to satisfy both filename sets. |
| Final PDF under the current assignment filename | `PES1UG24CS155_Lab7.pdf` | Verified | Generated from the four captures. pypdf confirmed 5 pages, the required student name/SRN/project/title text, and one embedded screenshot on each evidence page. All five pages were rendered and visually inspected. |
| Compatibility PDF filename from the original checklist | `PES1UG24CS155_Lab7_FuzzTesting.pdf` | Verified | Updated as a byte-for-byte copy of `PES1UG24CS155_Lab7.pdf`; it contains the same final pages and evidence. |
| PDF generator | `build_lab7_pdf.py` | Verified | No generator was present during inspection, so this reproducible builder was added. It embeds the four PNGs and checks the PDF page count, identity text, and screenshot count. |
| PDF readability and correct student details | Both final PDF filenames | Verified | Rendered all 5 pages at 1.5 scale. Cover layout, identity fields, test summary, captions, and terminal screenshots are visible and readable when viewed at page size or zoomed. |
| README documents setup, commands, test mapping, results, and deliverables | `README.md` | Verified | Reviewed the updated PowerShell instructions and mapped all three functions to test names. It reports only the observed 10/4 baseline and 14-pass final run. |
| Academic source files are separate and executable | `processor.py`; `test_processor.py` | Verified | Both exist as separate Python files; the app ran and pytest imported and executed the suite. |
| Labs 1–6 left untouched | `Software_Engineering_Labs_PES1UG24CS155/Lab-1/` through `Lab-6/` | Verified | All edits for this task were kept inside the existing `Lab-7` folder. |
| Git checkout sync, branch, commit, push, and pull request | Actual checkout named in the user's request | Pending | Academic files above are verified; repo synchronization is tracked separately from the official lab deliverables and must be audited before final completion. |

## Verified result

The application, initial fuzz failures, fixed application, and final passing Hypothesis run have all been executed and captured. The final report contains the four genuine terminal screenshots. The mandatory academic files are present in this exact folder. Git status is marked pending until the separate repository workflow is inspected and completed; Git history is not a substitute for these files.

## Reproduction

Run from the `Lab-7` directory in PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python processor_original.py
$env:LAB7_USE_ORIGINAL = "1"
python -m pytest -v --tb=no test_processor.py
Remove-Item Env:LAB7_USE_ORIGINAL
python processor.py
python -m pytest -v test_processor.py
python build_lab7_pdf.py
```

`build_lab7_pdf.py` regenerates both PDF filenames listed above. The local `.venv`, pytest cache, PDF render previews, and bytecode caches are development artifacts and must not be copied into the Git submission.
