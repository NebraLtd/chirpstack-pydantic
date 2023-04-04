# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)
# type: ignore

from ..common.common_p2p import KeyEnvelope
from ..common.common_p2p import Location
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


class ErrorType(IntEnum):
    GENERIC = 0
    OTAA = 1
    DATA_UP_FCNT_RESET = 2
    DATA_UP_MIC = 3
    DEVICE_QUEUE_ITEM_SIZE = 4
    DEVICE_QUEUE_ITEM_FCNT = 5
    DATA_UP_FCNT_RETRANSMISSION = 6
    DATA_DOWN_GATEWAY = 7


class DeviceActivationContext(BaseModel):

    dev_addr: bytes = FieldInfo(default=b"")
    app_s_key: KeyEnvelope = FieldInfo()


class HandleUplinkDataRequest(BaseModel):

    dev_eui: bytes = FieldInfo(default=b"")
    join_eui: bytes = FieldInfo(default=b"")
    f_cnt: int = FieldInfo(default=0)
    f_port: int = FieldInfo(default=0)
    adr: bool = FieldInfo(default=False)
    dr: int = FieldInfo(default=0)
    tx_info: UplinkTXInfo = FieldInfo()
    rx_info: typing.List[UplinkRXInfo] = FieldInfo(default_factory=list)
    data: bytes = FieldInfo(default=b"")
    device_activation_context: DeviceActivationContext = FieldInfo()
    confirmed_uplink: bool = FieldInfo(default=False)


class HandleProprietaryUplinkRequest(BaseModel):

    mac_payload: bytes = FieldInfo(default=b"")
    mic: bytes = FieldInfo(default=b"")
    tx_info: UplinkTXInfo = FieldInfo()
    rx_info: typing.List[UplinkRXInfo] = FieldInfo(default_factory=list)


class HandleErrorRequest(BaseModel):

    dev_eui: bytes = FieldInfo(default=b"")
    type: ErrorType = FieldInfo(default=0)
    error: str = FieldInfo(default="")
    f_cnt: int = FieldInfo(default=0)


class HandleDownlinkACKRequest(BaseModel):

    dev_eui: bytes = FieldInfo(default=b"")
    f_cnt: int = FieldInfo(default=0)
    acknowledged: bool = FieldInfo(default=False)


class SetDeviceStatusRequest(BaseModel):

    dev_eui: bytes = FieldInfo(default=b"")
    battery: int = FieldInfo(default=0)
    margin: int = FieldInfo(default=0)
    external_power_source: bool = FieldInfo(default=False)
    battery_level_unavailable: bool = FieldInfo(default=False)
    battery_level: float = FieldInfo(default=0.0)


class SetDeviceLocationRequest(BaseModel):

    dev_eui: bytes = FieldInfo(default=b"")
    location: Location = FieldInfo()
    uplink_ids: typing.List[bytes] = FieldInfo(default_factory=list)


class HandleGatewayStatsRequest(BaseModel):

    gateway_id: bytes = FieldInfo(default=b"")
    stats_id: bytes = FieldInfo(default=b"")
    time: datetime = FieldInfo(default_factory=datetime.now)
    location: Location = FieldInfo()
    rx_packets_received: int = FieldInfo(default=0)
    rx_packets_received_ok: int = FieldInfo(default=0)
    tx_packets_received: int = FieldInfo(default=0)
    tx_packets_emitted: int = FieldInfo(default=0)
    metadata: typing.Dict[str, str] = FieldInfo(default_factory=dict)
    tx_packets_per_frequency: typing.Dict[int, int] = FieldInfo(default_factory=dict)
    rx_packets_per_frequency: typing.Dict[int, int] = FieldInfo(default_factory=dict)
    tx_packets_per_dr: typing.Dict[int, int] = FieldInfo(default_factory=dict)
    rx_packets_per_dr: typing.Dict[int, int] = FieldInfo(default_factory=dict)
    tx_packets_per_status: typing.Dict[str, int] = FieldInfo(default_factory=dict)


class HandleTxAckRequest(BaseModel):

    dev_eui: bytes = FieldInfo(default=b"")
    f_cnt: int = FieldInfo(default=0)
    gateway_id: bytes = FieldInfo(default=b"")
    tx_info: DownlinkTXInfo = FieldInfo()


class ReEncryptDeviceQueueItemsRequest(BaseModel):

    dev_eui: bytes = FieldInfo(default=b"")
    dev_addr: bytes = FieldInfo(default=b"")
    f_cnt_start: int = FieldInfo(default=0)
    items: typing.List[ReEncryptDeviceQueueItem] = FieldInfo(default_factory=list)


class ReEncryptDeviceQueueItemsResponse(BaseModel):

    items: typing.List[ReEncryptedDeviceQueueItem] = FieldInfo(default_factory=list)


class ReEncryptDeviceQueueItem(BaseModel):

    frm_payload: bytes = FieldInfo(default=b"")
    f_cnt: int = FieldInfo(default=0)
    f_port: int = FieldInfo(default=0)
    confirmed: bool = FieldInfo(default=False)


class ReEncryptedDeviceQueueItem(BaseModel):

    frm_payload: bytes = FieldInfo(default=b"")
    f_cnt: int = FieldInfo(default=0)
    f_port: int = FieldInfo(default=0)
    confirmed: bool = FieldInfo(default=False)
