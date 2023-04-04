import json
from typing import Type

from google.protobuf.json_format import MessageToDict, Parse
from google.protobuf.message import Message
from pydantic import BaseModel
from chirpstack_api import api as chirpstack_api

from .aliases import protobuf_aliases, pydantic_to_protobuf_aliases
from .models import api as pydantic_api


class PydanticModelNotFound(Exception):
    pass


class ChirpstackModelNotFound(Exception):
    pass


def protobuf_to_pydantic(message: Type[Message]) -> Type[BaseModel]:
    msg_type: str = message.DESCRIPTOR.name

    pydantic_model = None
    if hasattr(pydantic_api, msg_type):
        pydantic_model = getattr(pydantic_api, msg_type)
    elif msg_type in protobuf_aliases:
        pydantic_model = protobuf_aliases[msg_type]
    else:
        raise PydanticModelNotFound(
            f"No pydantic model found for protobuf message type: {msg_type}"
        )

    msg_dict = MessageToDict(message)
    obj = pydantic_model.parse_obj(msg_dict)

    return obj


def pydantic_to_protobuf(model_obj: Type[BaseModel]) -> Type[Message]:
    msg_type: str = model_obj.__class__.__name__

    protobuf_class = None
    if hasattr(chirpstack_api, msg_type):
        protobuf_class = getattr(chirpstack_api, msg_type)
    elif msg_type in pydantic_to_protobuf_aliases:
        protobuf_class = pydantic_to_protobuf_aliases[msg_type]
    else:
        raise ChirpstackModelNotFound(
            f"No chirpstack protobuf model found for message type: {msg_type}"
        )

    pb_obj = protobuf_class()
    pb_obj = Parse(model_obj.json(), pb_obj)

    return pb_obj
