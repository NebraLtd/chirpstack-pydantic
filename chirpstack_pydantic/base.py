from pydantic import BaseModel as PydanticBaseModel


def to_camel(string: str) -> str:
    output = "".join(word.capitalize() for word in string.split("_"))
    return output[0].lower() + output[1:]


class BaseModel(PydanticBaseModel):
    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True
