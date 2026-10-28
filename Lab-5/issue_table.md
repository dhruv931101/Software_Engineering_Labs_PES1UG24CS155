# Lab 5 — Static Code Analysis Issue Table

**Student:** Dhruv Swatantramath  
**SRN:** PES1UG24CS155  
**Assigned repository:** `SETAPESU26/L5_27_address_book`  
**File analyzed:** `address_book.py`

The line numbers below refer to the **original, pre-fix version** of `address_book.py` and its before-reports.

| No. | Tool / finding | Type / severity | Original line(s) | Description | Fix applied |
|---:|---|---|---:|---|---|
| 1 | Pylint `missing-module-docstring` | Code quality | 1 | The module did not have a module-level docstring describing its purpose. | Added a module docstring describing the address-book program. |
| 2 | Pylint `missing-function-docstring` | Code quality | 10, 18, 22, 30, 39, 47, 53, 60, 65, 70 | Functions did not document their purpose. | Added docstrings to the functions. |
| 3 | Pylint `invalid-name` | Naming/style | 10, 18, 22, 30, 39, 47, 53, 60, 65 | Function names such as `addContact` and arguments such as `fullName` did not follow snake_case. | Renamed functions and arguments to snake_case. |
| 4 | Pylint `broad-exception-caught` | Reliability | 34 | `updateCity` caught the overly broad `Exception`, which could hide unrelated programming errors. | Replaced broad exception handling with an explicit check that the contact exists before updating it. |
| 5 | Pylint `consider-using-enumerate` | Code quality | 49 | `printDirectory` iterated over `range(len(names))` instead of using a direct iteration pattern. | Used `enumerate` to obtain the index and contact name together. |
| 6 | Pylint `unspecified-encoding` | Portability | 54 | The CSV text file was opened without explicitly specifying an encoding. | Specified UTF-8 when opening the CSV file. |
| 7 | Bandit `B403` — pickle import | Security / low | 3 | Pickle can be unsafe when handling data from an untrusted source. | Replaced pickle-based backup/restore with JSON-based serialization. |
| 8 | Bandit `B105` — hardcoded password | Security / low | 6 | A password-like string, `contacts-demo`, was hardcoded in the source. | Removed the unused hardcoded password constant. Do not store real credentials in source code. |
| 9 | Bandit `B324` — weak MD5 hash | Security / high | 19 | MD5 is not suitable for security-sensitive hashing; the function used it to generate a short contact identifier. | Replaced MD5 with SHA-256 for identifier generation. The identifier remains a short display identifier, not an authentication token. |
| 10 | Bandit `B301` — unsafe pickle deserialization | Security / medium | 67 | `pickle.load` can execute code when loading maliciously crafted data. | Replaced pickle deserialization with JSON loading. JSON should still be validated against expected data types and fields. |
| 11 | Flake8 `E225` — missing whitespace around operator | Style | 23 | An operator lacked the required surrounding whitespace. | Added the required whitespace. |
| 12 | Flake8 `E303` — too many blank lines | Style | 47 | There were too many consecutive blank lines before a function. | Removed excess blank lines. |
| 13 | Flake8 `E231` — missing whitespace after comma | Style | 84 | A comma was not followed by a space. | Added the required space after the comma. |
| 14 | Flake8 `E501` — line too long | Style | 85 | A line exceeded the configured 79-character limit. | Split/reformatted the long line. |

## Verification results

| Tool | Before | After | Status |
|---|---|---|---|
| Pylint | 5.47/10 | 10.00/10 | Passed; final score exceeds the handout's 9.5 target. |
| Bandit | 4 findings: 1 high, 1 medium, 2 low | No issues identified | Passed. |
| Flake8 | 4 violations | No violations reported | Passed. |
| Program execution | Original test run printed the expected demo output, including invalid-phone and missing-contact messages. | Final program was run successfully; JSON backup/restore equality check returned `True`. | Passed. |

## Notes

- The before line numbers are taken from the original code and the saved before-reports. They may not match line numbers in the updated file.
- The issue table documents findings from all three static-analysis tools. The handout also requires three commits associated with the fixes from Pylint, Bandit, and Flake8; the commit history must be checked separately.
- Reflection questions are omitted as instructed by the student.
