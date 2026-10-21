# Repository Health Checker

A small, beginner-friendly Python program that checks whether its project
folder contains the expected files and folder:

- `README.md`
- a `test` folder
- `requirements.txt`

It prints a pass or fail message for each item and a short overall health
result. The checker uses only Python's standard library, so it has no external
package dependencies.

## Requirements

- Python 3.9 or newer

## Setup

Clone or download this project, then open a terminal in the project folder.
There are no third-party packages to install. If you use a virtual environment,
create and activate it with:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows, activate it with:

```powershell
.venv\Scripts\Activate.ps1
```

## Usage

Run the health checker from the project folder:

```bash
python3 app.py
```

On Windows, you can use:

```powershell
python app.py
```

The checker evaluates the folder containing `app.py`. It reports missing
items as failures and prints an overall result at the end.

## Tests

Run the automated tests with Python's built-in `unittest` framework:

```bash
python3 -m unittest discover -s test -v
```

The tests check both detection of required items and the printed health report.
