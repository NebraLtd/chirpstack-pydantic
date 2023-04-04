# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)
# type: ignore

from ..common.common_p2p import Location
from ..common.common_p2p import Modulation
from datetime import datetime
from datetime import timedelta
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from protobuf_to_pydantic.customer_validator import check_one_of
from protobuf_to_pydantic.util import Timedelta
from chirpstack_pydantic.base import BaseModel
from pydantic import root_validator
from pydantic.fields import FieldInfo
import typing


class DownlinkTiming(IntEnum):
    IMMEDIATELY = 0
    DELAY = 1
    GPS_EPOCH = 2


class FineTimestampType(IntEnum):
    NONE = 0
    ENCRYPTED = 1
    PLAIN = 2


class CRCStatus(IntEnum):
    NO_CRC = 0
    BAD_CRC = 1
    CRC_OK = 2


class TxAckStatus(IntEnum):
    IGNORED = 0
    OK = 1
    TOO_LATE = 2
    TOO_EARLY = 3
    COLLISION_PACKET = 4
    COLLISION_BEACON = 5
    TX_FREQ = 6
    TX_POWER = 7
    GPS_UNLOCKED = 8
    QUEUE_FULL = 9
    INTERNAL_ERROR = 10


class LoRaModulationInfo(BaseModel):

    bandwidth: int = FieldInfo(default=0)
    spreading_factor: int = FieldInfo(default=0)
    code_rate: str = FieldInfo(default="")
    polarization_inversion: bool = FieldInfo(default=False)


class FSKModulationInfo(BaseModel):

    frequency_deviation: int = FieldInfo(default=0)
    datarate: int = FieldInfo(default=0)


class LRFHSSModulationInfo(BaseModel):

    operating_channel_width: int = FieldInfo(default=0)
    code_rate: str = FieldInfo(default="")
    grid_steps: int = FieldInfo(default=0)


class EncryptedFineTimestamp(BaseModel):

    aes_key_index: int = FieldInfo(default=0)
    encrypted_ns: bytes = FieldInfo(default=b"")
    fpga_id: bytes = FieldInfo(default=b"")


class PlainFineTimestamp(BaseModel):

    time: datetime = FieldInfo(default_factory=datetime.now)


class Modulation(BaseModel):

    _one_of_dict = {"Modulation.parameters": {"fields": {"fsk", "lora", "lr_fhss"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    lora: LoRaModulationInfo = FieldInfo()
    fsk: FSKModulationInfo = FieldInfo()
    lr_fhss: LRFHSSModulationInfo = FieldInfo()


class PerModulationCount(BaseModel):

    modulation: Modulation = FieldInfo()
    count: int = FieldInfo(default=0)


class UplinkTXInfo(BaseModel):

    _one_of_dict = {
        "UplinkTXInfo.modulation_info": {
            "fields": {
                "fsk_modulation_info",
                "lora_modulation_info",
                "lr_fhss_modulation_info",
            }
        }
    }
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    frequency: int = FieldInfo(default=0)
    modulation: Modulation = FieldInfo(default=0)
    lora_modulation_info: LoRaModulationInfo = FieldInfo()
    fsk_modulation_info: FSKModulationInfo = FieldInfo()
    lr_fhss_modulation_info: LRFHSSModulationInfo = FieldInfo()


class GatewayStats(BaseModel):

    gateway_id: bytes = FieldInfo(default=b"")
    ip: str = FieldInfo(default="")
    time: datetime = FieldInfo(default_factory=datetime.now)
    location: Location = FieldInfo()
    config_version: str = FieldInfo(default="")
    rx_packets_received: int = FieldInfo(default=0)
    rx_packets_received_ok: int = FieldInfo(default=0)
    tx_packets_received: int = FieldInfo(default=0)
    tx_packets_emitted: int = FieldInfo(default=0)
    meta_data: typing.Dict[str, str] = FieldInfo(default_factory=dict)
    stats_id: bytes = FieldInfo(default=b"")
    tx_packets_per_frequency: typing.Dict[int, int] = FieldInfo(default_factory=dict)
    rx_packets_per_frequency: typing.Dict[int, int] = FieldInfo(default_factory=dict)
    tx_packets_per_modulation: typing.List[PerModulationCount] = FieldInfo(
        default_factory=list
    )
    rx_packets_per_modulation: typing.List[PerModulationCount] = FieldInfo(
        default_factory=list
    )
    tx_packets_per_status: typing.Dict[str, int] = FieldInfo(default_factory=dict)


class UplinkRXInfo(BaseModel):

    _one_of_dict = {
        "UplinkRXInfo.fine_timestamp": {
            "fields": {"encrypted_fine_timestamp", "plain_fine_timestamp"}
        }
    }
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    gateway_id: bytes = FieldInfo(default=b"")
    time: datetime = FieldInfo(default_factory=datetime.now)
    time_since_gps_epoch: Timedelta = FieldInfo(default_factory=timedelta)
    rssi: int = FieldInfo(default=0)
    lora_snr: float = FieldInfo(default=0.0)
    channel: int = FieldInfo(default=0)
    rf_chain: int = FieldInfo(default=0)
    board: int = FieldInfo(default=0)
    antenna: int = FieldInfo(default=0)
    location: Location = FieldInfo()
    fine_timestamp_type: FineTimestampType = FieldInfo(default=0)
    encrypted_fine_timestamp: EncryptedFineTimestamp = FieldInfo()
    plain_fine_timestamp: PlainFineTimestamp = FieldInfo()
    context: bytes = FieldInfo(default=b"")
    uplink_id: bytes = FieldInfo(default=b"")
    crc_status: CRCStatus = FieldInfo(default=0)


class ImmediatelyTimingInfo(BaseModel):
    pass


class DelayTimingInfo(BaseModel):

    delay: Timedelta = FieldInfo(default_factory=timedelta)


class GPSEpochTimingInfo(BaseModel):

    time_since_gps_epoch: Timedelta = FieldInfo(default_factory=timedelta)


class DownlinkTXInfo(BaseModel):

    _one_of_dict = {
        "DownlinkTXInfo.modulation_info": {
            "fields": {"fsk_modulation_info", "lora_modulation_info"}
        },
        "DownlinkTXInfo.timing_info": {
            "fields": {
                "delay_timing_info",
                "gps_epoch_timing_info",
                "immediately_timing_info",
            }
        },
    }
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    gateway_id: bytes = FieldInfo(default=b"")
    frequency: int = FieldInfo(default=0)
    power: int = FieldInfo(default=0)
    modulation: Modulation = FieldInfo(default=0)
    lora_modulation_info: LoRaModulationInfo = FieldInfo()
    fsk_modulation_info: FSKModulationInfo = FieldInfo()
    board: int = FieldInfo(default=0)
    antenna: int = FieldInfo(default=0)
    timing: DownlinkTiming = FieldInfo(default=0)
    immediately_timing_info: ImmediatelyTimingInfo = FieldInfo()
    delay_timing_info: DelayTimingInfo = FieldInfo()
    gps_epoch_timing_info: GPSEpochTimingInfo = FieldInfo()
    context: bytes = FieldInfo(default=b"")


class UplinkFrame(BaseModel):

    phy_payload: bytes = FieldInfo(default=b"")
    tx_info: UplinkTXInfo = FieldInfo()
    rx_info: UplinkRXInfo = FieldInfo()


class UplinkFrameSet(BaseModel):

    phy_payload: bytes = FieldInfo(default=b"")
    tx_info: UplinkTXInfo = FieldInfo()
    rx_info: typing.List[UplinkRXInfo] = FieldInfo(default_factory=list)


class DownlinkFrameItem(BaseModel):

    phy_payload: bytes = FieldInfo(default=b"")
    tx_info: DownlinkTXInfo = FieldInfo()


class DownlinkFrame(BaseModel):

    phy_payload: bytes = FieldInfo(default=b"")
    tx_info: DownlinkTXInfo = FieldInfo()
    token: int = FieldInfo(default=0)
    downlink_id: bytes = FieldInfo(default=b"")
    items: typing.List[DownlinkFrameItem] = FieldInfo(default_factory=list)
    gateway_id: bytes = FieldInfo(default=b"")


class LoRaModulationConfig(BaseModel):

    bandwidth: int = FieldInfo(default=0)
    spreading_factors: typing.List[int] = FieldInfo(default_factory=list)


class FSKModulationConfig(BaseModel):

    bandwidth: int = FieldInfo(default=0)
    bitrate: int = FieldInfo(default=0)


class DownlinkTXAckItem(BaseModel):

    status: TxAckStatus = FieldInfo(default=0)


class DownlinkTXAck(BaseModel):

    gateway_id: bytes = FieldInfo(default=b"")
    token: int = FieldInfo(default=0)
    error: str = FieldInfo(default="")
    downlink_id: bytes = FieldInfo(default=b"")
    items: typing.List[DownlinkTXAckItem] = FieldInfo(default_factory=list)


class ChannelConfiguration(BaseModel):

    _one_of_dict = {
        "ChannelConfiguration.modulation_config": {
            "fields": {"fsk_modulation_config", "lora_modulation_config"}
        }
    }
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    frequency: int = FieldInfo(default=0)
    modulation: Modulation = FieldInfo(default=0)
    lora_modulation_config: LoRaModulationConfig = FieldInfo()
    fsk_modulation_config: FSKModulationConfig = FieldInfo()
    board: int = FieldInfo(default=0)
    demodulator: int = FieldInfo(default=0)


class GatewayConfiguration(BaseModel):

    gateway_id: bytes = FieldInfo(default=b"")
    version: str = FieldInfo(default="")
    channels: typing.List[ChannelConfiguration] = FieldInfo(default_factory=list)
    stats_interval: Timedelta = FieldInfo(default_factory=timedelta)


class GatewayCommandExecRequest(BaseModel):

    gateway_id: bytes = FieldInfo(default=b"")
    command: str = FieldInfo(default="")
    ExecId: bytes = FieldInfo(default=b"")
    stdin: bytes = FieldInfo(default=b"")
    environment: typing.Dict[str, str] = FieldInfo(default_factory=dict)


class GatewayCommandExecResponse(BaseModel):

    gateway_id: bytes = FieldInfo(default=b"")
    exec_id: bytes = FieldInfo(default=b"")
    stdout: bytes = FieldInfo(default=b"")
    stderr: bytes = FieldInfo(default=b"")
    error: str = FieldInfo(default="")


class RawPacketForwarderEvent(BaseModel):

    gateway_id: bytes = FieldInfo(default=b"")
    raw_id: bytes = FieldInfo(default=b"")
    payload: bytes = FieldInfo(default=b"")


class RawPacketForwarderCommand(BaseModel):

    gateway_id: bytes = FieldInfo(default=b"")
    raw_id: bytes = FieldInfo(default=b"")
    payload: bytes = FieldInfo(default=b"")


class ConnState(BaseModel):
    class State(IntEnum):
        OFFLINE = 0
        ONLINE = 1

    gateway_id: bytes = FieldInfo(default=b"")
    state: State = FieldInfo(default=0)
