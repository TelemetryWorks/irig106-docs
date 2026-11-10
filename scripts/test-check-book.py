#!/usr/bin/env python3
"""Regression for locale-independent reads; requires a populated book/ build."""

from contextlib import redirect_stdout
import runpy
from io import StringIO
from pathlib import Path
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
CHECKER = runpy.run_path(str(ROOT / "scripts/check-book.py"))
ORIGINAL_OPEN = Path.open


def ascii_default(path, mode="r", buffering=-1, encoding=None, errors=None, newline=None):
    # Path.read_text can pass "locale" for an omitted encoding on Python 3.11+.
    if "b" not in mode and encoding in (None, "locale"):
        encoding = "ascii"
    return ORIGINAL_OPEN(path, mode, buffering, encoding, errors, newline)


class EncodingRegression(unittest.TestCase):
    def test_mock_rejects_implicit_encoding(self):
        with patch.object(Path, "open", ascii_default):
            with self.assertRaises(UnicodeDecodeError):
                (ROOT / "src/introduction.md").read_text()

    def test_actual_book_passes_with_ascii_default(self):
        with patch.object(Path, "open", ascii_default), redirect_stdout(StringIO()):
            CHECKER["check"](ROOT, ROOT / "book")


if __name__ == "__main__":
    unittest.main()
