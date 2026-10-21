from contextlib import redirect_stdout
from io import StringIO
import tempfile
import unittest
from pathlib import Path

from app import check_repository, print_report


class CheckRepositoryTests(unittest.TestCase):
    def test_finds_all_required_items(self):
        with tempfile.TemporaryDirectory() as temporary_folder:
            repository_folder = Path(temporary_folder)
            (repository_folder / "README.md").touch()
            (repository_folder / "test").mkdir()
            (repository_folder / "requirements.txt").touch()

            checks = check_repository(repository_folder)

        self.assertTrue(all(checks.values()))

    def test_reports_missing_items(self):
        with tempfile.TemporaryDirectory() as temporary_folder:
            checks = check_repository(Path(temporary_folder))

        self.assertEqual(
            checks,
            {
                "README.md": False,
                "test folder": False,
                "requirements.txt": False,
            },
        )

    def test_prints_healthy_report_when_every_item_is_found(self):
        output = StringIO()
        checks = {
            "README.md": True,
            "test folder": True,
            "requirements.txt": True,
        }

        with redirect_stdout(output):
            print_report(checks)

        self.assertIn("PASS: README.md found", output.getvalue())
        self.assertIn("Result: Repository looks healthy.", output.getvalue())


if __name__ == "__main__":
    unittest.main()
