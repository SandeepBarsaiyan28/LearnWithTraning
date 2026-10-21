from pathlib import Path


def check_repository(repository_folder: Path) -> dict[str, bool]:
    """Check whether the repository has the expected files and folder."""
    return {
        "README.md": (repository_folder / "README.md").is_file(),
        "test folder": (repository_folder / "test").is_dir(),
        "requirements.txt": (repository_folder / "requirements.txt").is_file(),
    }


def print_report(checks: dict[str, bool]) -> None:
    """Print a simple report from the repository check results."""
    print("Repository Health Check")
    print("-----------------------")

    for item, was_found in checks.items():
        if was_found:
            print(f"PASS: {item} found")
        else:
            print(f"FAIL: {item} is missing")

    if all(checks.values()):
        print("\nResult: Repository looks healthy.")
    else:
        print("\nResult: Some required items are missing.")


if __name__ == "__main__":
    # Check the folder where this Python file is saved.
    repository_folder = Path(__file__).resolve().parent
    print_report(check_repository(repository_folder))
