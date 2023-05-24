from typing import Any


#################
# pre validator #
#################
def check_one_of(cls: Any, values: tuple) -> tuple:
    """validatorValidator for supporting protobuf one_of"""
    for one_of_name, one_of_dict in getattr(
        cls, "_one_of_dict", {}
    ).items():  # type: str, OneOfTypedDict
        have_value_name = sum(
            [1 for one_of_field_name in one_of_dict["fields"] if one_of_field_name in values]
        )
        if have_value_name >= 2:
            raise ValueError(f"OneOf:{one_of_name} has {have_value_name} value")
        if one_of_dict.get("required", False) and have_value_name == 0:
            raise ValueError(f"OneOf:{one_of_name} must set value")
    return values
