import logging
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))
sys.path.append(str(ROOT / "backend"))

from backend.taxonomy import Category, resolve_category
from backend.category_router import get_contract
from backend.models import Planet


def test_resolve_category_warns_deprecated(caplog):
    with caplog.at_level(logging.WARNING):
        cat = resolve_category("education")
    assert cat is Category.EDUCATION
    assert "Legacy category string" in caplog.text


def test_get_contract_from_taxonomy():
    contract = get_contract(Category.EDUCATION)
    assert contract == {"examiner": Planet.SUN}
