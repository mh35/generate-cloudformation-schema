"""JSON Schemaの出力型定義です."""

from typing import Any, Literal, NotRequired, TypedDict, Union

_SchemaBase = TypedDict(
    "_SchemaBase",
    {
        "$comment": NotRequired[str],
        "title": NotRequired[str],
        "description": NotRequired[str],
    },
)

_RefField = TypedDict(
    "_RefField",
    {
        "$comment": NotRequired[str],
        "title": NotRequired[str],
        "description": NotRequired[str],
        "$ref": str,
    },
)


class _EnumField(_SchemaBase):
    """列挙型のフィールドです."""

    enum: list[Any]


class _ConstField(_SchemaBase):
    """定数型のフィールドです."""

    const: Any


class _BoolField(_SchemaBase):
    """論理値型のフィールドです."""

    type: Literal["boolean"]


class _NullField(_SchemaBase):
    """nullのフィールドです."""

    type: Literal["null"]


class _IntField(_SchemaBase):
    """整数型のフィールドです."""

    type: Literal["integer"]
    multipleOf: NotRequired[int]
    minimum: NotRequired[int]
    exclusiveMinimum: NotRequired[int]
    maximum: NotRequired[int]
    exclusiveMaximum: NotRequired[int]


class _NumberField(_SchemaBase):
    """小数型のフィールドです."""

    type: Literal["number"]
    multipleOf: NotRequired[int | float]
    minimum: NotRequired[int | float]
    exclusiveMinimum: NotRequired[int | float]
    maximum: NotRequired[int | float]
    exclusiveMaximum: NotRequired[int | float]


class _StringField(_SchemaBase):
    """文字列型のフィールドです."""

    type: Literal["string"]
    minLength: NotRequired[int]
    maxLength: NotRequired[int]
    pattern: NotRequired[str]


_FieldSchema = Union[
    _RefField,
    _EnumField,
    _ConstField,
    _NullField,
    _IntField,
    _NumberField,
    _StringField,
    "_ArrayField",
    "_ObjectField",
    "_AllOfSchema",
    "_AnyOfSchema",
    "_OneOfSchema",
    "_NotSchema",
]


class _ArrayField(_SchemaBase):
    """配列型のフィールドです."""

    type: Literal["array"]
    items: NotRequired[_FieldSchema] | Literal[False]
    prefixItems: NotRequired[list[_FieldSchema]]


class _ObjectField(_SchemaBase):
    """オブジェクト型のフィールドです."""

    type: Literal["object"]
    properties: NotRequired[dict[str, _FieldSchema]]
    patternProperties: NotRequired[dict[str, _FieldSchema]]
    additionalProperties: NotRequired[bool | _FieldSchema]
    required: NotRequired[list[str]]
    minProperties: NotRequired[int]
    maxProperties: NotRequired[int]


class _AllOfSchema(_SchemaBase):
    """すべてを満たすべきと定めるスキーマです."""

    allOf: list[_FieldSchema]


class _AnyOfSchema(_SchemaBase):
    """これらのいずれか1つ以上を満たすべきと定めるスキーマです."""

    anyOf: list[_FieldSchema]


class _OneOfSchema(_SchemaBase):
    """これらのちょうど1つを満たすべきと定めるスキーマです."""

    oneOf: list[_FieldSchema]


_NotSchema = TypedDict("_NotSchema", {"not": _FieldSchema})


SchemaDict = TypedDict(
    "SchemaDict",
    {
        "$schema": Literal["https://json-schema.org/draft/2020-12/schema"],
        "$id": NotRequired[str],
        "$comment": NotRequired[str],
        "title": NotRequired[str],
        "description": NotRequired[str],
        "type": Literal["object"],
        "required": NotRequired[list[str]],
        "additionalProperties": NotRequired[bool | _FieldSchema],
        "$defs": NotRequired[dict[str, _FieldSchema]],
        "properties": dict[str, _FieldSchema],
    },
)
