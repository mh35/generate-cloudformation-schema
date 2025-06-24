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
