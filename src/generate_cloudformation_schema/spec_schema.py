"""リソース仕様のJSONスキーマです."""

from jschon import create_catalog, JSONSchema

create_catalog("2020-12")

MULTI_SPEC_SCHEMA = JSONSchema(
    {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "required": ["ResourceSpecificationVersion", "ResourceTypes"],
        "$defs": {
            "PrimitivePropertySpec": {
                "type": "object",
                "required": [
                    "Documentation",
                    "PrimitiveType",
                    "Required",
                    "UpdateType",
                ],
                "additionalProperties": False,
                "properties": {
                    "Documentation": {"type": "string", "format": "uri"},
                    "PrimitiveType": {
                        "enum": [
                            "String",
                            "Long",
                            "Integer",
                            "Double",
                            "Boolean",
                            "Timestamp",
                            "Json",
                        ]
                    },
                    "Required": {"type": "boolean"},
                    "UpdateType": {
                        "enum": ["Mutable", "Immutable", "Conditional"]
                    },
                },
            },
            "PrimitiveArrayPropertySpec": {
                "type": "object",
                "required": [
                    "Documentation",
                    "Type",
                    "Required",
                    "UpdateType",
                    "DuplicatesAllowed",
                    "PrimitiveItemType",
                ],
                "additionalProperties": False,
                "properties": {
                    "Documentation": {"type": "string", "format": "uri"},
                    "Type": {"const": "List"},
                    "Required": {"type": "boolean"},
                    "UpdateType": {
                        "enum": ["Mutable", "Immutable", "Conditional"]
                    },
                    "DuplicatesAllowed": {"type": "boolean"},
                    "PrimitiveItemType": {
                        "enum": [
                            "String",
                            "Long",
                            "Integer",
                            "Double",
                            "Boolean",
                            "Timestamp",
                        ],
                    },
                },
            },
            "PrimitiveMapPropertySpec": {
                "type": "object",
                "required": [
                    "Documentation",
                    "Type",
                    "Required",
                    "UpdateType",
                    "PrimitiveItemType",
                ],
                "additionalProperties": False,
                "properties": {
                    "Documentation": {"type": "string", "format": "uri"},
                    "Type": {"const": "Map"},
                    "Required": {"type": "boolean"},
                    "UpdateType": {
                        "enum": ["Mutable", "Immutable", "Conditional"]
                    },
                    "PrimitiveItemType": {
                        "enum": [
                            "String",
                            "Long",
                            "Integer",
                            "Double",
                            "Boolean",
                            "Timestamp",
                        ],
                    },
                },
            },
            "ComplexTypePropertySpec": {
                "type": "object",
                "required": [
                    "Documentation",
                    "Type",
                    "Required",
                    "UpdateType",
                ],
                "additionalProperties": False,
                "properties": {
                    "Documentation": {"type": "string", "format": "uri"},
                    "Type": {
                        "type": "string",
                        "format": "^(?!(List|Map)$).+$",
                    },
                    "Required": {"type": "boolean"},
                    "UpdateType": {
                        "enum": ["Mutable", "Immutable", "Conditional"]
                    },
                },
            },
            "ComplexArrayPropertySpec": {
                "type": "object",
                "required": [
                    "Documentation",
                    "Type",
                    "Required",
                    "UpdateType",
                    "DuplicatesAllowed",
                    "ItemType",
                ],
                "additionalProperties": False,
                "properties": {
                    "Documentation": {"type": "string", "format": "uri"},
                    "Type": {"const": "List"},
                    "Required": {"type": "boolean"},
                    "UpdateType": {
                        "enum": ["Mutable", "Immutable", "Conditional"]
                    },
                    "DuplicatesAllowed": {"type": "boolean"},
                    "ItemType": {"type": "string"},
                },
            },
            "ComplexMapPropertySpec": {
                "type": "object",
                "required": [
                    "Documentation",
                    "Type",
                    "Required",
                    "UpdateType",
                    "ItemType",
                ],
                "additionalProperties": False,
                "properties": {
                    "Documentation": {"type": "string", "format": "uri"},
                    "Type": {"const": "Map"},
                    "Required": {"type": "boolean"},
                    "UpdateType": {
                        "enum": ["Mutable", "Immutable", "Conditional"]
                    },
                    "ItemType": {"type": "string"},
                },
            },
            "PrimitiveResourceAttributeSpec": {
                "type": "object",
                "required": ["PrimitiveType"],
                "additionalProperties": False,
                "properties": {
                    "PrimitiveType": {
                        "enum": [
                            "String",
                            "Long",
                            "Integer",
                            "Double",
                            "Boolean",
                            "Timestamp",
                            "Json",
                        ]
                    },
                },
            },
            "PrimitiveArrayResourceAttributeSpec": {
                "type": "object",
                "required": ["Type", "PrimitiveItemType"],
                "additionalProperties": False,
                "properties": {
                    "Type": {"const": "List"},
                    "PrimitiveItemType": {
                        "enum": [
                            "String",
                            "Long",
                            "Integer",
                            "Double",
                            "Boolean",
                            "Timestamp",
                        ]
                    },
                },
            },
            "ComplexResourceAttributeSpec": {
                "type": "object",
                "required": ["Type"],
                "additionalProperties": False,
                "properties": {
                    "Type": {"type": "string", "format": "^(?!List$).+$"},
                },
            },
            "ComplexArrayResourceAttributeSpec": {
                "type": "object",
                "required": ["Type", "ItemType"],
                "additionalProperties": False,
                "properties": {
                    "Type": {"const": "List"},
                    "ItemType": {"type": "string"},
                },
            },
            "ResourceSpec": {
                "type": "object",
                "required": ["Documentation", "Properties"],
                "properties": {
                    "Attributes": {
                        "type": "object",
                        "patternProperties": {
                            "^.+$": {
                                "oneOf": [
                                    {
                                        "$ref": "#/$defs/PrimitiveResourceAttributeSpec"
                                    },
                                    {
                                        "$ref": "#/$defs/PrimitiveArrayResourceAttributeSpec"
                                    },
                                    {
                                        "$ref": "#/$defs/ComplexResourceAttributeSpec"
                                    },
                                    {
                                        "$ref": "#/$defs/ComplexArrayResourceAttributeSpec"
                                    },
                                ],
                            }
                        },
                    },
                    "Documentation": {"type": "string", "format": "uri"},
                    "AdditionalProperties": {"type": "boolean"},
                    "Properties": {
                        "type": "object",
                        "patternProperties": {
                            "^.+$": {
                                "oneOf": [
                                    {"$ref": "#/$defs/PrimitivePropertySpec"},
                                    {
                                        "$ref": "#/$defs/PrimitiveArrayPropertySpec"
                                    },
                                    {
                                        "$ref": "#/$defs/PrimitiveMapPropertySpec"
                                    },
                                    {
                                        "$ref": "#/$defs/ComplexTypePropertySpec"
                                    },
                                    {
                                        "$ref": "#/$defs/ComplexArrayPropertySpec"
                                    },
                                    {"$ref": "#/$defs/ComplexMapPropertySpec"},
                                ],
                            },
                        },
                    },
                },
            },
        },
        "properties": {
            "ResourceSpecificationVersion": {
                "type": "string",
                "pattern": "^[0-9]+\\.[0-9]+\\.[0-9]+$",
            },
            "PropertyTypes": {
                "type": "object",
                "patternProperties": {
                    "^[A-Za-z0-9]+::[A-Za-z0-9]+::[A-Za-z0-9]+\\.[A-Za-z0-9]+$": {
                        "type": "object",
                        "required": ["Documentation", "Properties"],
                        "additionalProperties": False,
                        "properties": {
                            "Documentation": {
                                "type": "string",
                                "format": "uri",
                            },
                            "Properties": {
                                "type": "object",
                                "patternProperties": {
                                    "^.+$": {
                                        "oneOf": [
                                            {
                                                "$ref": "#/$defs/PrimitivePropertySpec"
                                            },
                                            {
                                                "$ref": "#/$defs/PrimitiveArrayPropertySpec"
                                            },
                                            {
                                                "$ref": "#/$defs/PrimitiveMapPropertySpec"
                                            },
                                            {
                                                "$ref": "#/$defs/ComplexTypePropertySpec"
                                            },
                                            {
                                                "$ref": "#/$defs/ComplexArrayPropertySpec"
                                            },
                                            {
                                                "$ref": "#/$defs/ComplexMapPropertySpec"
                                            },
                                        ],
                                    },
                                },
                            },
                        },
                    },
                },
            },
            "ResourceTypes": {
                "type": "object",
                "patternProperties": {
                    "^[A-Za-z0-9]+::[A-Za-z0-9]+::[A-Za-z0-9]+$": {
                        "$ref": "#/$defs/ResourceSpec"
                    },
                },
            },
        },
    }
)

SINGLE_SPEC_SCHEMA = JSONSchema(
    {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "required": ["ResourceSpecificationVersion", "ResourceType"],
        "$defs": {
            "PrimitivePropertySpec": {
                "type": "object",
                "required": [
                    "Documentation",
                    "PrimitiveType",
                    "Required",
                    "UpdateType",
                ],
                "additionalProperties": False,
                "properties": {
                    "Documentation": {"type": "string", "format": "uri"},
                    "PrimitiveType": {
                        "enum": [
                            "String",
                            "Long",
                            "Integer",
                            "Double",
                            "Boolean",
                            "Timestamp",
                            "Json",
                        ]
                    },
                    "Required": {"type": "boolean"},
                    "UpdateType": {
                        "enum": ["Mutable", "Immutable", "Conditional"]
                    },
                },
            },
            "PrimitiveArrayPropertySpec": {
                "type": "object",
                "required": [
                    "Documentation",
                    "Type",
                    "Required",
                    "UpdateType",
                    "DuplicatesAllowed",
                    "PrimitiveItemType",
                ],
                "additionalProperties": False,
                "properties": {
                    "Documentation": {"type": "string", "format": "uri"},
                    "Type": {"const": "List"},
                    "Required": {"type": "boolean"},
                    "UpdateType": {
                        "enum": ["Mutable", "Immutable", "Conditional"]
                    },
                    "DuplicatesAllowed": {"type": "boolean"},
                    "PrimitiveItemType": {
                        "enum": [
                            "String",
                            "Long",
                            "Integer",
                            "Double",
                            "Boolean",
                            "Timestamp",
                        ],
                    },
                },
            },
            "PrimitiveMapPropertySpec": {
                "type": "object",
                "required": [
                    "Documentation",
                    "Type",
                    "Required",
                    "UpdateType",
                    "PrimitiveItemType",
                ],
                "additionalProperties": False,
                "properties": {
                    "Documentation": {"type": "string", "format": "uri"},
                    "Type": {"const": "Map"},
                    "Required": {"type": "boolean"},
                    "UpdateType": {
                        "enum": ["Mutable", "Immutable", "Conditional"]
                    },
                    "PrimitiveItemType": {
                        "enum": [
                            "String",
                            "Long",
                            "Integer",
                            "Double",
                            "Boolean",
                            "Timestamp",
                        ],
                    },
                },
            },
            "ComplexTypePropertySpec": {
                "type": "object",
                "required": [
                    "Documentation",
                    "Type",
                    "Required",
                    "UpdateType",
                ],
                "additionalProperties": False,
                "properties": {
                    "Documentation": {"type": "string", "format": "uri"},
                    "Type": {
                        "type": "string",
                        "format": "^(?!(List|Map)$).+$",
                    },
                    "Required": {"type": "boolean"},
                    "UpdateType": {
                        "enum": ["Mutable", "Immutable", "Conditional"]
                    },
                },
            },
            "ComplexArrayPropertySpec": {
                "type": "object",
                "required": [
                    "Documentation",
                    "Type",
                    "Required",
                    "UpdateType",
                    "DuplicatesAllowed",
                    "ItemType",
                ],
                "additionalProperties": False,
                "properties": {
                    "Documentation": {"type": "string", "format": "uri"},
                    "Type": {"const": "List"},
                    "Required": {"type": "boolean"},
                    "UpdateType": {
                        "enum": ["Mutable", "Immutable", "Conditional"]
                    },
                    "DuplicatesAllowed": {"type": "boolean"},
                    "ItemType": {"type": "string"},
                },
            },
            "ComplexMapPropertySpec": {
                "type": "object",
                "required": [
                    "Documentation",
                    "Type",
                    "Required",
                    "UpdateType",
                    "ItemType",
                ],
                "additionalProperties": False,
                "properties": {
                    "Documentation": {"type": "string", "format": "uri"},
                    "Type": {"const": "Map"},
                    "Required": {"type": "boolean"},
                    "UpdateType": {
                        "enum": ["Mutable", "Immutable", "Conditional"]
                    },
                    "ItemType": {"type": "string"},
                },
            },
            "PrimitiveResourceAttributeSpec": {
                "type": "object",
                "required": ["PrimitiveType"],
                "additionalProperties": False,
                "properties": {
                    "PrimitiveType": {
                        "enum": [
                            "String",
                            "Long",
                            "Integer",
                            "Double",
                            "Boolean",
                            "Timestamp",
                            "Json",
                        ]
                    },
                },
            },
            "PrimitiveArrayResourceAttributeSpec": {
                "type": "object",
                "required": ["Type", "PrimitiveItemType"],
                "additionalProperties": False,
                "properties": {
                    "Type": {"const": "List"},
                    "PrimitiveItemType": {
                        "enum": [
                            "String",
                            "Long",
                            "Integer",
                            "Double",
                            "Boolean",
                            "Timestamp",
                        ]
                    },
                },
            },
            "ComplexResourceAttributeSpec": {
                "type": "object",
                "required": ["Type"],
                "additionalProperties": False,
                "properties": {
                    "Type": {"type": "string", "format": "^(?!List$).+$"},
                },
            },
            "ComplexArrayResourceAttributeSpec": {
                "type": "object",
                "required": ["Type", "ItemType"],
                "additionalProperties": False,
                "properties": {
                    "Type": {"const": "List"},
                    "ItemType": {"type": "string"},
                },
            },
            "ResourceSpec": {
                "type": "object",
                "required": ["Documentation", "Properties"],
                "properties": {
                    "Attributes": {
                        "type": "object",
                        "patternProperties": {
                            "^.+$": {
                                "oneOf": [
                                    {
                                        "$ref": "#/$defs/PrimitiveResourceAttributeSpec"
                                    },
                                    {
                                        "$ref": "#/$defs/PrimitiveArrayResourceAttributeSpec"
                                    },
                                    {
                                        "$ref": "#/$defs/ComplexResourceAttributeSpec"
                                    },
                                    {
                                        "$ref": "#/$defs/ComplexArrayResourceAttributeSpec"
                                    },
                                ],
                            }
                        },
                    },
                    "Documentation": {"type": "string", "format": "uri"},
                    "AdditionalProperties": {"type": "boolean"},
                    "Properties": {
                        "type": "object",
                        "patternProperties": {
                            "^.+$": {
                                "oneOf": [
                                    {"$ref": "#/$defs/PrimitivePropertySpec"},
                                    {
                                        "$ref": "#/$defs/PrimitiveArrayPropertySpec"
                                    },
                                    {
                                        "$ref": "#/$defs/PrimitiveMapPropertySpec"
                                    },
                                    {
                                        "$ref": "#/$defs/ComplexTypePropertySpec"
                                    },
                                    {
                                        "$ref": "#/$defs/ComplexArrayPropertySpec"
                                    },
                                    {"$ref": "#/$defs/ComplexMapPropertySpec"},
                                ],
                            },
                        },
                    },
                },
            },
        },
        "properties": {
            "ResourceSpecificationVersion": {
                "type": "string",
                "pattern": "^[0-9]+\\.[0-9]+\\.[0-9]+$",
            },
            "PropertyTypes": {
                "type": "object",
                "type": "object",
                "patternProperties": {
                    "^[A-Za-z0-9]+::[A-Za-z0-9]+::[A-Za-z0-9]+\\.[A-Za-z0-9]+$": {
                        "type": "object",
                        "required": ["Documentation", "Properties"],
                        "additionalProperties": False,
                        "properties": {
                            "Documentation": {
                                "type": "string",
                                "format": "uri",
                            },
                            "Properties": {
                                "type": "object",
                                "patternProperties": {
                                    "^.+$": {
                                        "oneOf": [
                                            {
                                                "$ref": "#/$defs/PrimitivePropertySpec"
                                            },
                                            {
                                                "$ref": "#/$defs/PrimitiveArrayPropertySpec"
                                            },
                                            {
                                                "$ref": "#/$defs/PrimitiveMapPropertySpec"
                                            },
                                            {
                                                "$ref": "#/$defs/ComplexTypePropertySpec"
                                            },
                                            {
                                                "$ref": "#/$defs/ComplexArrayPropertySpec"
                                            },
                                            {
                                                "$ref": "#/$defs/ComplexMapPropertySpec"
                                            },
                                        ],
                                    },
                                },
                            },
                        },
                    },
                },
            },
            "ResourceType": {
                "type": "object",
                "patternProperties": {
                    "^[A-Za-z0-9]+::[A-Za-z0-9]+::[A-Za-z0-9]+$": {
                        "$ref": "#/$defs/ResourceSpec"
                    },
                },
                "minProperties": 1,
                "maxProperties": 1,
            },
        },
    }
)
