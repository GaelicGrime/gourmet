

import inspect as INS
from inspect import (
    isfunction,
#    ismethod,
    ismodule,
)
import typing as TYPING
from typing import types as TTYPES


from CSCF.SUBM_D import _00_VALS_IN as CF_V


locals().update(CF_V.ALL_THE_VALS)
V = None


"""

bool
dict
float
function
int
list
module
str
tuple

class03_C {INS.getmembers(class03_C.C_03, isfunction)}
class03_C.__new__ {INS.getmembers(class03_C.__new__)}
getfullargspec(class03_C)  {INS.getfullargspec(class03_C)}

"""


ALL_THE_VALS = {
    "OBJECT_BOOL_IN_DICT": "OBJECT_BOOL_IN_DICT",
    "OBJECT_BOOL_IN_FUNC": "OBJECT_BOOL_IN_FUNC",
    "OBJECT_BOOL_IN_LIST": "OBJECT_BOOL_IN_LIST",
    "OBJECT_BOOL_IN_MODL": "OBJECT_BOOL_IN_MODL",
    "OBJECT_BOOL_IN_NONE": "OBJECT_BOOL_IN_NONE",
    "OBJECT_BOOL_IN_TUPL": "OBJECT_BOOL_IN_TUPL",
    "OBJECT_DICT_IN_DICT": "OBJECT_DICT_IN_DICT",
    "OBJECT_DICT_IN_FUNC": "OBJECT_DICT_IN_FUNC",
    "OBJECT_DICT_IN_LIST": "OBJECT_DICT_IN_LIST",
    "OBJECT_DICT_IN_MODL": "OBJECT_DICT_IN_MODL",
    "OBJECT_DICT_IN_NONE": "OBJECT_DICT_IN_NONE",
    "OBJECT_DICT_IN_TUPL": "OBJECT_DICT_IN_TUPL",
    "OBJECT_FLT_IN_DICT": "OBJECT_FLT_IN_DICT",
    "OBJECT_FLT_IN_FUNC": "OBJECT_FLT_IN_FUNC",
    "OBJECT_FLT_IN_LIST": "OBJECT_FLT_IN_LIST",
    "OBJECT_FLT_IN_MODL": "OBJECT_FLT_IN_MODL",
    "OBJECT_FLT_IN_NONE": "OBJECT_FLT_IN_NONE",
    "OBJECT_FLT_IN_TUPL": "OBJECT_FLT_IN_TUPL",
    "OBJECT_FUNC_IN_DICT": "OBJECT_FUNC_IN_DICT",
    "OBJECT_FUNC_IN_FUNC": "OBJECT_FUNC_IN_FUNC",
    "OBJECT_FUNC_IN_LIST": "OBJECT_FUNC_IN_LIST",
    "OBJECT_FUNC_IN_MODL": "OBJECT_FUNC_IN_MODL",
    "OBJECT_FUNC_IN_NONE": "OBJECT_FUNC_IN_NONE",
    "OBJECT_FUNC_IN_TUPL": "OBJECT_FUNC_IN_TUPL",
    "OBJECT_INT_IN_DICT": "OBJECT_INT_IN_DICT",
    "OBJECT_INT_IN_FUNC": "OBJECT_INT_IN_FUNC",
    "OBJECT_INT_IN_LIST": "OBJECT_INT_IN_LIST",
    "OBJECT_INT_IN_MODL": "OBJECT_INT_IN_MODL",
    "OBJECT_INT_IN_NONE": "OBJECT_INT_IN_NONE",
    "OBJECT_INT_IN_TUPL": "OBJECT_INT_IN_TUPL",
    "OBJECT_LIST_IN_DICT": "OBJECT_LIST_IN_DICT",
    "OBJECT_LIST_IN_FUNC": "OBJECT_LIST_IN_FUNC",
    "OBJECT_LIST_IN_LIST": "OBJECT_LIST_IN_LIST",
    "OBJECT_LIST_IN_MODL": "OBJECT_LIST_IN_MODL",
    "OBJECT_LIST_IN_NONE": "OBJECT_LIST_IN_NONE",
    "OBJECT_LIST_IN_TUPL": "OBJECT_LIST_IN_TUPL",
    "OBJECT_MODL_IN_DICT": "OBJECT_MODL_IN_DICT",
    "OBJECT_MODL_IN_FUNC": "OBJECT_MODL_IN_FUNC",
    "OBJECT_MODL_IN_LIST": "OBJECT_MODL_IN_LIST",
    "OBJECT_MODL_IN_MODL": "OBJECT_MODL_IN_MODL",
    "OBJECT_MODL_IN_NONE": "OBJECT_MODL_IN_NONE",
    "OBJECT_MODL_IN_TUPL": "OBJECT_MODL_IN_TUPL",
    "OBJECT_NONE_IN_DICT": "OBJECT_NONE_IN_DICT",
    "OBJECT_NONE_IN_FUNC": "OBJECT_NONE_IN_FUNC",
    "OBJECT_NONE_IN_LIST": "OBJECT_NONE_IN_LIST",
    "OBJECT_NONE_IN_MODL": "OBJECT_NONE_IN_MODL",
    "OBJECT_NONE_IN_NONE": "OBJECT_NONE_IN_NONE",
    "OBJECT_NONE_IN_TUPL": "OBJECT_NONE_IN_TUPL",
    "OBJECT_STR_IN_DICT": "OBJECT_STR_IN_DICT",
    "OBJECT_STR_IN_FUNC": "OBJECT_STR_IN_FUNC",
    "OBJECT_STR_IN_LIST": "OBJECT_STR_IN_LIST",
    "OBJECT_STR_IN_MODL": "OBJECT_STR_IN_MODL",
    "OBJECT_STR_IN_NONE": "OBJECT_STR_IN_NONE",
    "OBJECT_STR_IN_TUPL": "OBJECT_STR_IN_TUPL",
    "OBJECT_TUPL_IN_DICT": "OBJECT_TUPL_IN_DICT",
    "OBJECT_TUPL_IN_FUNC": "OBJECT_TUPL_IN_FUNC",
    "OBJECT_TUPL_IN_LIST": "OBJECT_TUPL_IN_LIST",
    "OBJECT_TUPL_IN_MODL": "OBJECT_TUPL_IN_MODL",
    "OBJECT_TUPL_IN_NONE": "OBJECT_TUPL_IN_NONE",
    "OBJECT_TUPL_IN_TUPL": "OBJECT_TUPL_IN_TUPL",
    "OBJECT_UNK_IN_DICT": "OBJECT_UNK_IN_DICT",
    "OBJECT_UNK_IN_FUNC": "OBJECT_UNK_IN_FUNC",
    "OBJECT_UNK_IN_LIST": "OBJECT_UNK_IN_LIST",
    "OBJECT_UNK_IN_MODL": "OBJECT_UNK_IN_MODL",
    "OBJECT_UNK_IN_NONE": "OBJECT_UNK_IN_NONE",
    "OBJECT_UNK_IN_TUPL": "OBJECT_UNK_IN_TUPL",
    "STR_ASSIGN": "STR_ASSIGN",
    "STR_END": "STR_END",
    "STR_FINAL": "STR_FINAL",
    "TYPE_BOOL": "TYPE_BOOL",
    "TYPE_DICT": "TYPE_DICT",
    "TYPE_FLT": "TYPE_FLT",
    "TYPE_FUNC": "TYPE_FUNC",
    "TYPE_INT": "TYPE_INT",
    "TYPE_LIST": "TYPE_LIST",
    "TYPE_MODL": "TYPE_MODL",
    "TYPE_NONE": "TYPE_NONE",
    "TYPE_STR": "TYPE_STR",
    "TYPE_TUPL": "TYPE_TUPL",
    "TYPE_UNK": "TYPE_UNK",
}
locals().update(ALL_THE_VALS)


TYPES_DICT = {
    bool: TYPE_BOOL,
    dict: TYPE_DICT,
    float: TYPE_FLT,
    int: TYPE_INT,
    list: TYPE_LIST,
    str: TYPE_STR,
    TTYPES.FunctionType: TYPE_FUNC,
    TTYPES.ModuleType: TYPE_MODL,
    TTYPES.NoneType: TYPE_NONE,
    tuple: TYPE_TUPL,
}


TYPES_RDICT = {
    TYPE_BOOL: bool,
    TYPE_DICT: dict,
    TYPE_FLT: float,
    TYPE_FUNC: TTYPES.FunctionType,
    TYPE_INT: int,
    TYPE_LIST: list,
    TYPE_MODL: TTYPES.ModuleType,
    TYPE_NONE: TTYPES.NoneType,
    TYPE_STR: str,
    TYPE_TUPL: tuple,
}


ALL_THE_BOOLS = [
    OBJECT_BOOL_IN_DICT,
    OBJECT_BOOL_IN_FUNC,
    OBJECT_BOOL_IN_LIST,
    OBJECT_BOOL_IN_MODL,
    OBJECT_BOOL_IN_NONE,
    OBJECT_BOOL_IN_TUPL,
]


ALL_THE_DICTS = [
    OBJECT_DICT_IN_DICT,
    OBJECT_DICT_IN_FUNC,
    OBJECT_DICT_IN_LIST,
    OBJECT_DICT_IN_MODL,
    OBJECT_DICT_IN_NONE,
    OBJECT_DICT_IN_TUPL,
]


ALL_THE_FUNCS = [
    OBJECT_FUNC_IN_DICT,
    OBJECT_FUNC_IN_FUNC,
    OBJECT_FUNC_IN_LIST,
    OBJECT_FUNC_IN_MODL,
    OBJECT_FUNC_IN_NONE,
    OBJECT_FUNC_IN_TUPL,
]


ALL_THE_LISTS = [
    OBJECT_LIST_IN_DICT,
    OBJECT_LIST_IN_FUNC,
    OBJECT_LIST_IN_LIST,
    OBJECT_LIST_IN_MODL,
    OBJECT_LIST_IN_NONE,
    OBJECT_LIST_IN_TUPL,
]


ALL_THE_MODLS = [
    OBJECT_MODL_IN_DICT,
    OBJECT_MODL_IN_FUNC,
    OBJECT_MODL_IN_LIST,
    OBJECT_MODL_IN_MODL,
    OBJECT_MODL_IN_NONE,
    OBJECT_MODL_IN_TUPL,
]


ALL_THE_NONES = [
    OBJECT_NONE_IN_DICT,
    OBJECT_NONE_IN_FUNC,
    OBJECT_NONE_IN_LIST,
    OBJECT_NONE_IN_MODL,
    OBJECT_NONE_IN_NONE,
    OBJECT_NONE_IN_TUPL,
]


ALL_THE_TUPLS = [
    OBJECT_TUPL_IN_DICT,
    OBJECT_TUPL_IN_FUNC,
    OBJECT_TUPL_IN_LIST,
    OBJECT_TUPL_IN_MODL,
    OBJECT_TUPL_IN_NONE,
    OBJECT_TUPL_IN_TUPL,
]


OBJECT_TYPE_DICT = {
    TYPE_BOOL: {
        TYPE_DICT: OBJECT_BOOL_IN_DICT,
        TYPE_FUNC: OBJECT_BOOL_IN_FUNC,
        TYPE_LIST: OBJECT_BOOL_IN_LIST,
        TYPE_MODL: OBJECT_BOOL_IN_MODL,
        TYPE_NONE: OBJECT_BOOL_IN_NONE,
        TYPE_TUPL: OBJECT_BOOL_IN_TUPL,
    },
    TYPE_DICT: {
        TYPE_DICT: OBJECT_DICT_IN_DICT,
        TYPE_FUNC: OBJECT_DICT_IN_FUNC,
        TYPE_LIST: OBJECT_DICT_IN_LIST,
        TYPE_MODL: OBJECT_DICT_IN_MODL,
        TYPE_NONE: OBJECT_DICT_IN_NONE,
        TYPE_TUPL: OBJECT_DICT_IN_TUPL,
    },
    TYPE_FLT: {
        TYPE_DICT: OBJECT_FLT_IN_DICT,
        TYPE_FUNC: OBJECT_FLT_IN_FUNC,
        TYPE_LIST: OBJECT_FLT_IN_LIST,
        TYPE_MODL: OBJECT_FLT_IN_MODL,
        TYPE_NONE: OBJECT_FLT_IN_NONE,
        TYPE_TUPL: OBJECT_FLT_IN_TUPL,
    },
    TYPE_FUNC: {
        TYPE_DICT: OBJECT_FUNC_IN_DICT,
        TYPE_FUNC: OBJECT_FUNC_IN_FUNC,
        TYPE_LIST: OBJECT_FUNC_IN_LIST,
        TYPE_MODL: OBJECT_FUNC_IN_MODL,
        TYPE_NONE: OBJECT_FUNC_IN_NONE,
        TYPE_TUPL: OBJECT_FUNC_IN_TUPL,
    },
    TYPE_INT: {
        TYPE_DICT: OBJECT_INT_IN_DICT,
        TYPE_FUNC: OBJECT_INT_IN_FUNC,
        TYPE_LIST: OBJECT_INT_IN_LIST,
        TYPE_MODL: OBJECT_INT_IN_MODL,
        TYPE_NONE: OBJECT_INT_IN_NONE,
        TYPE_TUPL: OBJECT_INT_IN_TUPL,
    },
    TYPE_LIST: {
        TYPE_DICT: OBJECT_LIST_IN_DICT,
        TYPE_FUNC: OBJECT_LIST_IN_FUNC,
        TYPE_LIST: OBJECT_LIST_IN_LIST,
        TYPE_MODL: OBJECT_LIST_IN_MODL,
        TYPE_NONE: OBJECT_LIST_IN_NONE,
        TYPE_TUPL: OBJECT_LIST_IN_TUPL,
    },
    TYPE_MODL: {
        TYPE_DICT: OBJECT_MODL_IN_DICT,
        TYPE_FUNC: OBJECT_MODL_IN_FUNC,
        TYPE_LIST: OBJECT_MODL_IN_LIST,
        TYPE_MODL: OBJECT_MODL_IN_MODL,
        TYPE_NONE: OBJECT_MODL_IN_NONE,
        TYPE_TUPL: OBJECT_MODL_IN_TUPL,
    },
    TYPE_NONE: {
        TYPE_DICT: OBJECT_NONE_IN_DICT,
        TYPE_FUNC: OBJECT_NONE_IN_FUNC,
        TYPE_LIST: OBJECT_NONE_IN_LIST,
        TYPE_MODL: OBJECT_NONE_IN_MODL,
        TYPE_NONE: OBJECT_NONE_IN_NONE,
        TYPE_TUPL: OBJECT_NONE_IN_TUPL,
    },
    TYPE_STR: {
        TYPE_DICT: OBJECT_STR_IN_DICT,
        TYPE_FUNC: OBJECT_STR_IN_FUNC,
        TYPE_LIST: OBJECT_STR_IN_LIST,
        TYPE_MODL: OBJECT_STR_IN_MODL,
        TYPE_NONE: OBJECT_STR_IN_NONE,
        TYPE_TUPL: OBJECT_STR_IN_TUPL,
    },
    TYPE_TUPL: {
        TYPE_DICT: OBJECT_TUPL_IN_DICT,
        TYPE_FUNC: OBJECT_TUPL_IN_FUNC,
        TYPE_LIST: OBJECT_TUPL_IN_LIST,
        TYPE_MODL: OBJECT_TUPL_IN_MODL,
        TYPE_NONE: OBJECT_TUPL_IN_NONE,
        TYPE_TUPL: OBJECT_TUPL_IN_TUPL,
    },
    TYPE_UNK: {
        TYPE_DICT: OBJECT_UNK_IN_DICT,
        TYPE_FUNC: OBJECT_UNK_IN_FUNC,
        TYPE_LIST: OBJECT_UNK_IN_LIST,
        TYPE_MODL: OBJECT_UNK_IN_MODL,
        TYPE_NONE: OBJECT_UNK_IN_NONE,
        TYPE_TUPL: OBJECT_UNK_IN_TUPL,
    },
}


COMMA_SET = [
    TYPE_DICT,
    TYPE_LIST,
    TYPE_TUPL,
]




















#
