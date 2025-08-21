import pytest

from horary_engine.engine import _structure_reasoning


def test_structure_reasoning_parses_stage_and_weight():
    text = "Significators: Querent gains favor (+12%)"
    result = _structure_reasoning([text])
    assert result == [{"stage": "Significators", "rule": "Querent gains favor", "weight": 12}]


def test_structure_reasoning_defaults_when_missing():
    text = "A general observation without extra info"
    result = _structure_reasoning([text])
    assert result == [{"stage": "General", "rule": text, "weight": 0}]
