"""パースしたスキーマを格納するためのストアです."""

from typing import Literal, Self, TypedDict

from .schema_types import _FieldSchema, _ObjectField
from .spec_types import _PropertyDef


class _SchemaStoreStoreItem(TypedDict):
    """スキーマストアのストアアイテムの型です."""

    original: _PropertyDef
    parsed: _FieldSchema | None


_SCHEMA_PRIMITIVE_TYPE_MAPS: dict[
    Literal["String", "Long", "Integer", "Double", "Boolean", "Timestamp", "Json"],
    Literal["boolean", "integer", "number", "string", "object"]
] = {
    "String": "string",
    "Long": "integer",
    "Integer": "integer",
    "Double": "number",
    "Boolean": "boolean",
    "Timestamp": "string",
    "Json": "object",
}


class SchemaStore:
    """パースしたスキーマのストアです."""

    def __init__(self: Self, property_defs: dict[str, _PropertyDef]) -> None:
        """ストアの初期化を行います.

        Args:
            property_defs[dict]: 元のスキーマのPropertyTypes属性です
        """
        self._store_content: dict[str, dict[str, _SchemaStoreStoreItem]] = {}
        for type_name, def_data in property_defs.items():
            resource_type, type_detail_name = type_name.split(".", 1)
            if resource_type not in self._store_content:
                self._store_content[resource_type] = {}
            self._store_content[resource_type][type_detail_name] = {
                "original": def_data,
                "parsed": None,
            }
        for resource_type, type_stored_content in self._store_content.items():
            for type_detail_name, store_item in type_stored_content.items():
                data: _ObjectField = {
                    "type": "object",
                    "required": [],
                    "properties": {},
                    "$comment": store_item["original"]["Documentation"]
                }
                for prop_name, prop_data in store_item["original"]["Properties"].items():
                    if prop_data.get("Required", False):
                        data["required"].append(prop_name)
                    if "PrimitiveType" in prop_data:
                        primitive_type = prop_data["PrimitiveType"]
                        resolved_type = _SCHEMA_PRIMITIVE_TYPE_MAPS[primitive_type]
                        if resolved_type == "boolean":
                            data["properties"][prop_name] = {
                                "$comment": prop_data["Documentation"],
                                "type": resolved_type,
                            }
                        elif resolved_type == "integer":
                            data["properties"][prop_name] = {
                                "$comment": prop_data["Documentation"],
                                "type": resolved_type,
                            }
                        elif resolved_type == "number":
                            data["properties"][prop_name] = {
                                "$comment": prop_data["Documentation"],
                                "type": resolved_type,
                            }
                        elif resolved_type == "string":
                            data["properties"][prop_name] = {
                                "$comment": prop_data["Documentation"],
                                "type": resolved_type,
                            }
                        else:
                            data["properties"][prop_name] = {
                                "$comment": prop_data["Documentation"],
                                "type": resolved_type,
                            }
                    elif prop_data["Type"] == "List" and "PrimitiveItemType" in prop_data:
                        if prop_data["PrimitiveItemType"] == "Boolean":
                            data["properties"][prop_name] = {
                                "$comment": prop_data["Documentation"],
                                "type": "array",
                                "items": {"type": "boolean"},
                            }
                        elif prop_data["PrimitiveItemType"] == "Integer" or prop_data["PrimitiveItemType"] == "Long":
                            data["properties"][prop_name] = {
                                "$comment": prop_data["Documentation"],
                                "type": "array",
                                "items": {"type": "integer"},
                            }
                        elif prop_data["PrimitiveItemType"] == "Double":
                            data["properties"][prop_name] = {
                                "$comment": prop_data["Documentation"],
                                "type": "array",
                                "items": {"type": "number"},
                            }
                        else:
                            data["properties"][prop_name] = {
                                "$comment": prop_data["Documentation"],
                                "type": "array",
                                "items": {"type": "string"},
                            }
                    elif prop_data["Type"] == "Map" and "PrimitiveItemType" in prop_data:
                        data["properties"][prop_name] = {
                            "$comment": prop_data["Documentation"],
                            "type": "object"
                        }
                        if prop_data["PrimitiveItemType"] == "Boolean":
                            data["properties"][prop_name] = {
                                "$comment": prop_data["Documentation"],
                                "type": "object",
                                "patternProperties": {
                                    ".+": {"type": "boolean"},
                                },
                            }
                        elif prop_data["PrimitiveItemType"] == "Integer" or prop_data["PrimitiveItemType"] == "Long":
                            data["properties"][prop_name] = {
                                "$comment": prop_data["Documentation"],
                                "type": "object",
                                "patternProperties": {
                                    ".+": {"type": "integer"},
                                },
                            }
                        elif prop_data["PrimitiveItemType"] == "Double":
                            data["properties"][prop_name] = {
                                "$comment": prop_data["Documentation"],
                                "type": "object",
                                "patternProperties": {
                                    ".+": {"type": "number"},
                                },
                            }
                        else:
                            data["properties"][prop_name] = {
                                "$comment": prop_data["Documentation"],
                                "type": "object",
                                "patternProperties": {
                                    ".+": {"type": "string"},
                                },
                            }
                    elif prop_data["Type"] == "List" and "ItemType" in prop_data:
                        target_id = '-'.join(type_detail_name.split("::")) + "_" + prop_data["ItemType"]
                        data["properties"][prop_name] = {
                            "$comment": prop_data["Documentation"],
                            "type": "array",
                            "items": {"$ref": "#/$defs/" + target_id},
                        }
                    elif prop_data["Type"] == "Map" and "ItemType" in prop_data:
                        target_id = '-'.join(type_detail_name.split("::")) + "_" + prop_data["ItemType"]
                        data["properties"][prop_name] = {
                            "$comment": prop_data["Documentation"],
                            "type": "object",
                            "patternProperties": {
                                ".+": {"$ref": "#/$defs/" + target_id},
                            }
                        }
                    else:
                        target_id = '-'.join(type_detail_name.split("::")) + "_" + prop_data["Type"]
                        data["properties"][prop_name] = {
                            "$comment": prop_data["Documentation"],
                            "$ref": "#/$defs/" + target_id,
                        }
                self._store_content[resource_type][type_detail_name]["parsed"] = data

    def to_defs(self: Self) -> dict[str, _FieldSchema]:
        """JSON Schemaの$refsフィールドに変換します.

        Returns:
            dict: $defsフィールド
        """
        ret: dict[str, _FieldSchema] = {}
        for resource_type, details in self._store_content.items():
            for detail_name, detail_item in details.items():
                if detail_item["parsed"]:
                    ret["-".join(resource_type.split("::")) + "_" + detail_name] = detail_item["parsed"]
        return ret
