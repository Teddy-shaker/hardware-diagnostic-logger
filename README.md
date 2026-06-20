# Hardware Diagnostic Logger

## Overview

Hardware Diagnostic Logger is a small Python project that reads device data from
a CSV file, creates `Device` objects, runs diagnostic checks, and generates text
and CSV reports showing whether each device passed, failed, or needs attention.

The project is designed to demonstrate file input/output, classes, public and
private members, containers, conditionals, loops, exception handling, and unit
testing.

## Architecture

![Architecture Diagram](/diagrams/Hardware%20Logger%20Project.drawio.png)

## Features

- Reads device data from `data/devices.csv`
- Creates `Device` objects from CSV rows
- Runs voltage, temperature, and current diagnostics
- Assigns each device a `PASS`, `WARNING`, or `FAIL` status
- Generates `reports/diagnostic_report.txt`
- Generates `reports/diagnostic_report.csv`
- Includes two unit tests for public class methods

## Project Structure

```text
hardware-diagnostic-logger/
├── main.py
├── device.py
├── data/
│   └── devices.csv
├── reports/
│   ├── diagnostic_report.txt
│   └── diagnostic_report.csv
├── tests/
│   └── test_device.py
└── diagrams/
    ├── Hardware Logger Project.drawio
    └── Hardware Logger Project.drawio.png
```

## Main Files

- `main.py`: Loads devices from CSV, runs diagnostics, and writes the reports.
- `device.py`: Defines the `Device` class and diagnostic methods.
- `data/devices.csv`: Input file containing device data.
- `reports/diagnostic_report.txt`: Generated text output report.
- `reports/diagnostic_report.csv`: Generated CSV output report.
- `tests/test_device.py`: Unit tests for the `Device` class.

## How To Run

From the project folder:

```bash
cd /Users/teddy/Desktop/hardware-diagnostic-logger
python3 -B main.py
```

The program will read:

```text
data/devices.csv
```

and generate:

```text
reports/diagnostic_report.txt
reports/diagnostic_report.csv
```

## How To Run Tests

Run the test file directly:

```bash
python3 -B tests/test_device.py
```

Or run test discovery:

```bash
python3 -B -m unittest discover -s tests -v
```

## CSV Format

The input CSV must include these columns:

```csv
device_name,device_type,voltage,temperature,current
```

Example:

```csv
Controller-A,Microcontroller,3.3,42.5,1.1
```

## CSV Report Format

The generated CSV report includes these columns:

```csv
name,device_type,status,reason
```

Example output row:

```csv
Controller-A,Microcontroller,PASS,All diagnostic checks passed.
```

## Diagnostic Rules

- Voltage must be between `3.0` and `5.0`.
- Temperature below `70.0` is `PASS`.
- Temperature from `70.0` to below `85.0` is `WARNING`.
- Temperature `85.0` or higher is `FAIL`.
- Current above `2.5` creates a `WARNING`.

## Requirement Coverage

This project includes:

- File reading and writing
- Text and CSV report generation
- User-defined functions
- Loops and conditional logic
- `try` / `except` / `else`
- List, tuple, set, and dictionary usage
- A separate imported `Device` class
- Public and private class attributes
- Public and private methods
- `__init__`, `__str__`, and `__eq__` magic methods
- Two unit tests using `assert` statements
