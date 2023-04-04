# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)
# type: ignore

from ..common.common_p2p import Location
from ..gw.gw_p2p import DownlinkTXInfo
from ..gw.gw_p2p import UplinkRXInfo
from ..gw.gw_p2p import UplinkTXInfo
from datetime import datetime
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic.fields import FieldInfo
import typing


class ErrorType(IntEnum):
    UNKNOWN = 0
    DOWNLINK_PAYLOAD_SIZE = 1
    DOWNLINK_FCNT = 2
    UPLINK_CODEC = 3
    DOWNLINK_CODEC = 4
    OTAA = 5
    UPLINK_FCNT_RESET = 6
    UPLINK_MIC = 7
    UPLINK_FCNT_RETRANSMISSION = 8
    DOWNLINK_GATEWAY = 9


class UplinkEvent(BaseModel):

    application_id: int = FieldInfo(default=0)
    application_name: str = FieldInfo(default="")
    device_name: str = FieldInfo(default="")
    dev_eui: bytes = FieldInfo(default=b"")
    rx_info: typing.List[UplinkRXInfo] = FieldInfo(default_factory=list)
    tx_info: UplinkTXInfo = FieldInfo()
    adr: bool = FieldInfo(default=False)
    dr: int = FieldInfo(default=0)
    f_cnt: int = FieldInfo(default=0)
    f_port: int = FieldInfo(default=0)
    data: bytes = FieldInfo(default=b"")
    object_json: str = FieldInfo(default="")
    tags: typing.Dict[str, str] = FieldInfo(default_factory=dict)
    confirmed_uplink: bool = FieldInfo(default=False)
    dev_addr: bytes = FieldInfo(default=b"")
    published_at: datetime = FieldInfo(default_factory=datetime.now)
    device_profile_id: str = FieldInfo(default="")
    device_profile_name: str = FieldInfo(default="")


class JoinEvent(BaseModel):

    application_id: int = FieldInfo(default=0)
    application_name: str = FieldInfo(default="")
    device_name: str = FieldInfo(default="")
    dev_eui: bytes = FieldInfo(default=b"")
    dev_addr: bytes = FieldInfo(default=b"")
    rx_info: typing.List[UplinkRXInfo] = FieldInfo(default_factory=list)
    tx_info: UplinkTXInfo = FieldInfo()
    dr: int = FieldInfo(default=0)
    tags: typing.Dict[str, str] = FieldInfo(default_factory=dict)
    published_at: datetime = FieldInfo(default_factory=datetime.now)


class AckEvent(BaseModel):

    application_id: int = FieldInfo(default=0)
    application_name: str = FieldInfo(default="")
    device_name: str = FieldInfo(default="")
    dev_eui: bytes = FieldInfo(default=b"")
    acknowledged: bool = FieldInfo(default=False)
    f_cnt: int = FieldInfo(default=0)
    tags: typing.Dict[str, str] = FieldInfo(default_factory=dict)
    published_at: datetime = FieldInfo(default_factory=datetime.now)


class TxAckEvent(BaseModel):

    application_id: int = FieldInfo(default=0)
    application_name: str = FieldInfo(default="")
    device_name: str = FieldInfo(default="")
    dev_eui: bytes = FieldInfo(default=b"")
    f_cnt: int = FieldInfo(default=0)
    tags: typing.Dict[str, str] = FieldInfo(default_factory=dict)
    gateway_id: bytes = FieldInfo(default=b"")
    tx_info: DownlinkTXInfo = FieldInfo()
    published_at: datetime = FieldInfo(default_factory=datetime.now)


class ErrorEvent(BaseModel):

    application_id: int = FieldInfo(default=0)
    application_name: str = FieldInfo(default="")
    device_name: str = FieldInfo(default="")
    dev_eui: bytes = FieldInfo(default=b"")
    type: ErrorType = FieldInfo(default=0)
    error: str = FieldInfo(default="")
    f_cnt: int = FieldInfo(default=0)
    tags: typing.Dict[str, str] = FieldInfo(default_factory=dict)
    published_at: datetime = FieldInfo(default_factory=datetime.now)


class StatusEvent(BaseModel):

    application_id: int = FieldInfo(default=0)
    application_name: str = FieldInfo(default="")
    device_name: str = FieldInfo(default="")
    dev_eui: bytes = FieldInfo(default=b"")
    margin: int = FieldInfo(default=0)
    external_power_source: bool = FieldInfo(default=False)
    battery_level_unavailable: bool = FieldInfo(default=False)
    battery_level: float = FieldInfo(default=0.0)
    tags: typing.Dict[str, str] = FieldInfo(default_factory=dict)
    published_at: datetime = FieldInfo(default_factory=datetime.now)


class LocationEvent(BaseModel):

    application_id: int = FieldInfo(default=0)
    application_name: str = FieldInfo(default="")
    device_name: str = FieldInfo(default="")
    dev_eui: bytes = FieldInfo(default=b"")
    location: Location = FieldInfo()
    tags: typing.Dict[str, str] = FieldInfo(default_factory=dict)
    uplink_ids: typing.List[bytes] = FieldInfo(default_factory=list)
    f_cnt: int = FieldInfo(default=0)
    published_at: datetime = FieldInfo(default_factory=datetime.now)


class IntegrationEvent(BaseModel):

    application_id: int = FieldInfo(default=0)
    application_name: str = FieldInfo(default="")
    device_name: str = FieldInfo(default="")
    dev_eui: bytes = FieldInfo(default=b"")
    tags: typing.Dict[str, str] = FieldInfo(default_factory=dict)
    integration_name: str = FieldInfo(default="")
    event_type: str = FieldInfo(default="")
    object_json: str = FieldInfo(default="")
    published_at: datetime = FieldInfo(default_factory=datetime.now)
