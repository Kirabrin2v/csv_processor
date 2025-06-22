import os
import sys
from pathlib import Path

import pytest

import main as csv_main


SAMPLE = Path(__file__).parent / "sample.csv"


def _run_cli(monkeypatch, capsys, *argv):
    """Вспомогательный хелпер: подменяет sys.argv, вызывает main(), возвращает stdout."""
    monkeypatch.setattr(sys, "argv", ["csv_filter.main", *map(str, argv)])
    csv_main.main()
    captured = capsys.readouterr()
    return captured.out


def test_main_where(monkeypatch, capsys):
    out = _run_cli(
        monkeypatch,
        capsys,
        SAMPLE,
        "--where",
        "brand=xiaomi",
    )

    assert "+" in out
    assert out.lower().count("xiaomi") == 3


def test_main_aggregate(monkeypatch, capsys):
    out = _run_cli(
        monkeypatch,
        capsys,
        SAMPLE,
        "--aggregate",
        "price=avg",
    )

    assert "+" in out
    assert "602" in out or "602.0" in out

