# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)
# type: ignore

from ..gw.gw_p2p import DownlinkTXInfo
from ..gw.gw_p2p import UplinkFrameSet
from ..gw.gw_p2p import UplinkRXInfo
from ..gw.gw_p2p import UplinkTXInfo
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic.fields import FieldInfo
import typing


class MType(IntEnum):
    UNKNOWN = 0
    JOIN_REQUEST = 1
    JOIN_ACCEPT = 2
    UNCONFIRMED_DATA_UP = 3
    UNCONFIRMED_DATA_DOWN = 4
    CONFIRMED_DATA_UP = 5
    CONFIRMED_DATA_DOWN = 6
    REJOIN_REQUEST = 7


class HandleUplinkMetaDataRequest(BaseModel):

    dev_eui: bytes = FieldInfo(default=b"")
    tx_info: UplinkTXInfo = FieldInfo()
    rx_info: typing.List[UplinkRXInfo] = FieldInfo(default_factory=list)
    phy_payload_byte_count: int = FieldInfo(default=0)
    mac_command_byte_count: int = FieldInfo(default=0)
    application_payload_byte_count: int = FieldInfo(default=0)
    message_type: MType = FieldInfo(default=0)


class HandleDownlinkMetaDataRequest(BaseModel):

    dev_eui: bytes = FieldInfo(default=b"")
    multicast_group_id: bytes = FieldInfo(default=b"")
    tx_info: DownlinkTXInfo = FieldInfo()
    phy_payload_byte_count: int = FieldInfo(default=0)
    mac_command_byte_count: int = FieldInfo(default=0)
    application_payload_byte_count: int = FieldInfo(default=0)
    message_type: MType = FieldInfo(default=0)
    gateway_id: bytes = FieldInfo(default=b"")


class HandleUplinkMACCommandRequest(BaseModel):

    dev_eui: bytes = FieldInfo(default=b"")
    cid: int = FieldInfo(default=0)
    commands: typing.List[bytes] = FieldInfo(default_factory=list)


class HandleRejectedUplinkFrameSetRequest(BaseModel):

    frame_set: UplinkFrameSet = FieldInfo()
