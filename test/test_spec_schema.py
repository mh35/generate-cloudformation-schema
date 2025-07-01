"""spec_schemaモジュールのテストです."""

import json
import os

from generate_cloudformation_schema.spec_schema import MULTI_SPEC_SCHEMA, SINGLE_SPEC_SCHEMA
from jschon import JSON


def test_multi_schema() -> None:
    """MULTI_SPEC_SCHEMAのテストを行います."""
    json_path = os.path.join(os.path.dirname(__file__), "assets", "test_spec_def_2.json")
    with open(json_path, "r") as fp:
        data = json.load(fp)
    result = MULTI_SPEC_SCHEMA.evaluate(JSON(data))
    assert result.valid

def test_single_schema() -> None:
    """SINGLE_SPEC_SCHEMAのテストを行います."""
    json_path = os.path.join(os.path.dirname(__file__), "assets", "test_spec_def_1.json")
    with open(json_path, "r") as fp:
        data = json.load(fp)
    result = SINGLE_SPEC_SCHEMA.evaluate(JSON(data))
    assert result.valid
