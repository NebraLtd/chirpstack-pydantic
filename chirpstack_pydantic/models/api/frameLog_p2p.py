# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)
# type: ignore

from ..gw.gw_p2p import DownlinkTXInfo
from ..gw.gw_p2p import UplinkRXInfo
from ..gw.gw_p2p import UplinkTXInfo
from datetime import datetime
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from chirpstack_pydantic.base import BaseModel
from pydantic.fields import FieldInfo
import typing


class RXWindow(IntEnum):
    RX1 = 0
    RX2 = 1


class UplinkFrameLog(BaseModel):

    tx_info: UplinkTXInfo = FieldInfo()
    rx_info: typing.List[UplinkRXInfo] = FieldInfo(default_factory=list)
    phy_payload_json: str = FieldInfo(default="")
    published_at: datetime = FieldInfo(default_factory=datetime.now)


class DownlinkFrameLog(BaseModel):

    tx_info: DownlinkTXInfo = FieldInfo()
    phy_payload_json: str = FieldInfo(default="")
    gateway_id: str = FieldInfo(default="")
    published_at: datetime = FieldInfo(default_factory=datetime.now)
