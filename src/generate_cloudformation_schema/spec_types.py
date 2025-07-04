"""リソース仕様のJSON型の定義です."""

from typing import Literal, NotRequired, TypedDict, Union


_UpdateType = Literal["Mutable", "Immutable", "Conditional"]


class _PrimitiveProperty(TypedDict):
    """プリミティブなプロパティの属性定義です."""

    Documentation: str
    PrimitiveType: Literal[
        "String", "Long", "Integer", "Double", "Boolean", "Timestamp", "Json"
    ]
    Required: bool
    UpdateType: _UpdateType


class _PrimitiveArrayProperty(TypedDict):
    """プリミティブな配列プロパティの属性定義です."""

    Documentation: str
    Type: Literal["List"]
    DuplicatesAllowed: bool
    PrimitiveItemType: Literal[
        "String", "Long", "Integer", "Double", "Boolean", "Timestamp"
    ]
    Required: bool
    UpdateType: _UpdateType


class _PrimitiveMapProperty(TypedDict):
    """プリミティブなマッププロパティの属性定義です."""

    Documentation: str
    Type: Literal["Map"]
    PrimitiveItemType: Literal[
        "String", "Long", "Integer", "Double", "Boolean", "Timestamp"
    ]
    Required: bool
    UpdateType: _UpdateType


class _ComplexTypeProperty(TypedDict):
    """他の型を参照する単一型プロパティの属性定義です."""

    Documentation: str
    Type: str
    Required: bool
    UpdateType: _UpdateType


class _ComplexArrayProperty(TypedDict):
    """他の型を参照する配列プロパティの属性定義です."""

    Documentation: str
    Type: Literal["List"]
    DuplicatesAllowed: bool
    ItemType: str
    Required: bool
    UpdateType: _UpdateType


class _ComplexMapProperty(TypedDict):
    """他の型を参照するマッププロパティの属性定義です."""

    Documentation: str
    Type: Literal["Map"]
    ItemType: str
    Required: bool
    UpdateType: _UpdateType


_PropertyType = Union[
    _PrimitiveProperty,
    _PrimitiveArrayProperty,
    _PrimitiveMapProperty,
    _ComplexTypeProperty,
    _ComplexArrayProperty,
    _ComplexMapProperty,
]

class _PropertyDef(TypedDict):
    """プロパティ定義情報の属性定義です."""

    Documentation: str
    Properties: dict[str, _PropertyType]


class _PrimitiveResourceAttributeType(TypedDict):
    """プリミティブなリソース属性の属性定義です."""

    PrimitiveType: Literal[
        "String", "Long", "Integer", "Double", "Boolean", "Timestamp", "Json"
    ]


class _PrimitiveListResourceAttributeType(TypedDict):
    """プリミティブな配列リソース属性の属性定義です."""

    Type: Literal["List"]
    PrimitiveItemType: Literal[
        "String", "Long", "Integer", "Double", "Boolean", "Timestamp"
    ]


class _ComplexResourceAttributeType(TypedDict):
    """他の型を参照する単一型リソース属性の属性定義です."""

    Type: str


class _ComplexListResourceAttributeType(TypedDict):
    """他の型を参照する配列リソース属性の属性定義です."""

    Type: Literal["List"]
    ItemType: str


_ResourceAttributeType = Union[
    _PrimitiveResourceAttributeType,
    _PrimitiveListResourceAttributeType,
    _ComplexResourceAttributeType,
    _ComplexListResourceAttributeType,
]


class _ResourceTypeSpec(TypedDict):
    """リソース全体の型定義です."""

    Attributes: NotRequired[dict[str, _ResourceAttributeType]]
    AdditionalProperties: NotRequired[bool]
    Documentation: str
    Properties: dict[str, _PropertyType]


class ResourcesSpec(TypedDict):
    """リソース定義全体の型定義です."""

    PropertyTypes: NotRequired[dict[str, _PropertyDef]]
    ResourceSpecificationVersion: str
    ResourceTypes: dict[str, _ResourceTypeSpec]


class SingleResourceSpec(TypedDict):
    """単一リソース定義全体の型定義です."""

    PropertyTypes: NotRequired[dict[str, _PropertyDef]]
    ResourceSpecificationVersion: str
    ResourceType: dict[str, _ResourceTypeSpec]
