# Number Analysis CLI Tool

A minimal, terminal-based Python application that collects real numbers from user input, validates them, saves them permanently into unique timestamped files, reads them back, sorts them using a custom algorithm, and computes statistical metrics from scratch.

---

## Features

- **Input Validation:** Prompts the user continuously, warning and re-prompting if non-numeric data is entered (unless the exit command is given).
- **Controlled Termination:** Stops entry when the user types `DONE`.
- **Permanent Timestamped Storage:** Automatically creates an `outcomes/` directory and saves each run into a uniquely named file based on the exact creation timestamp (`YYYY-MM-DD_HH-MM-SS.txt`) to prevent data loss.
- **Custom Sorting:** Implements a custom **Bubble Sort** algorithm from scratch (descending order: greatest to smallest) without relying on Python's built-in `sort()` or `sorted()` functions.
- **Custom Statistics:** Computes the **Arithmetic Mean** and **Sample Standard Deviation** manually using custom loops.

---

## File Structure

```text
project-folder/
│
├── challenge.py         # Main Python script
├── README.md            # Documentation file
└── outcomes/            # Automatically generated folder
    ├── 2026-06-06_12-30-00.txt # Unique timestamped output file per run
    └── 2026-06-06_14-15-22.txt # Another run's saved results
```
