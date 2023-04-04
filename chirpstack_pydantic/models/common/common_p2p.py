# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)
# type: ignore

from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from chirpstack_pydantic.base import BaseModel
from pydantic.fields import FieldInfo



class Modulation(IntEnum):
    LORA = 0
    FSK = 1
    LR_FHSS = 2


class Region(IntEnum):
    EU868 = 0
    US915 = 2
    CN779 = 3
    EU433 = 4
    AU915 = 5
    CN470 = 6
    AS923 = 7
    AS923_2 = 12
    AS923_3 = 13
    AS923_4 = 14
    KR920 = 8
    IN865 = 9
    RU864 = 10
    ISM2400 = 11


class MType(IntEnum):
    JoinRequest = 0
    JoinAccept = 1
    UnconfirmedDataUp = 2
    UnconfirmedDataDown = 3
    ConfirmedDataUp = 4
    ConfirmedDataDown = 5
    RejoinRequest = 6
    Proprietary = 7


class LocationSource(IntEnum):
    UNKNOWN = 0
    GPS = 1
    CONFIG = 2
    GEO_RESOLVER_TDOA = 3
    GEO_RESOLVER_RSSI = 4
    GEO_RESOLVER_GNSS = 5
    GEO_RESOLVER_WIFI = 6




class KeyEnvelope(BaseModel):

    kek_label: str = FieldInfo(default="")
    aes_key: bytes = FieldInfo(default=b"")




class Location(BaseModel):

    latitude: float = FieldInfo(default=0.0)
    longitude: float = FieldInfo(default=0.0)
    altitude: float = FieldInfo(default=0.0)
    source: LocationSource = FieldInfo(default=0)
    accuracy: int = FieldInfo(default=0)


