"""リソース仕様のJSON型の定義です."""

from typing import Literal, TypedDict


class _PrimitiveProperty(TypedDict):
    """プリミティブなプロパティの属性定義です."""

    Documentation: str
    PrimitiveType: Literal[
        "String", "Long", "Integer", "Double", "Boolean", "Timestamp", "Json"
    ]
    Required: bool
    UpdateType: str


class _PrimitiveArrayProperty(TypedDict):
    """プリミティブな配列プロパティの属性定義です."""

    Documentation: str
    Type: Literal["List"]
    DuplicatesAllowed: bool
    PrimitiveItemType: Literal[
        "String", "Long", "Integer", "Double", "Boolean", "Timestamp"
    ]
    Required: bool
    UpdateType: str


class _PrimitiveMapProperty(TypedDict):
    """プリミティブなマッププロパティの属性定義です."""

    Documentation: str
    Type: Literal["Map"]
    PrimitiveItemType: Literal[
        "String", "Long", "Integer", "Double", "Boolean", "Timestamp"
    ]
    Required: bool
    UpdateType: str


class _ComplexTypeProperty(TypedDict):
    """他の型を参照する単一型プロパティの属性定義です."""

    Documentation: str
    Type: str
    Required: bool
    UpdateType: str


class _ComplexArrayProperty(TypedDict):
    """他の型を参照する配列プロパティの属性定義です."""

    Documentation: str
    Type: Literal["List"]
    DuplicatesAllowed: bool
    ItemType: str
    Required: bool
    UpdateType: str


class _ComplexMapProperty(TypedDict):
    """他の型を参照するマッププロパティの属性定義です."""

    Documentation: str
    Type: Literal["Map"]
    ItemType: str
    Required: bool
    UpdateType: str
