# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)
# type: ignore

from ..common.common_p2p import Location
from .frameLog_p2p import DownlinkFrameLog
from .frameLog_p2p import UplinkFrameLog
from datetime import datetime
from google.protobuf.message import Message  # type: ignore
from protobuf_to_pydantic.customer_validator import check_one_of
from chirpstack_pydantic.base import BaseModel
from pydantic import root_validator
from pydantic.fields import FieldInfo
import typing


class GatewayBoard(BaseModel):

    fpga_id: str = FieldInfo(default="")
    fine_timestamp_key: str = FieldInfo(default="")


class Gateway(BaseModel):

    id: str = FieldInfo(default="")
    name: str = FieldInfo(default="")
    description: str = FieldInfo(default="")
    location: Location = FieldInfo()
    organization_id: int = FieldInfo(default=0)
    discovery_enabled: bool = FieldInfo(default=False)
    network_server_id: int = FieldInfo(default=0)
    gateway_profile_id: str = FieldInfo(default="")
    boards: typing.List[GatewayBoard] = FieldInfo(default_factory=list)
    tags: typing.Dict[str, str] = FieldInfo(default_factory=dict)
    metadata: typing.Dict[str, str] = FieldInfo(default_factory=dict)
    service_profile_id: str = FieldInfo(default="")


class CreateGatewayRequest(BaseModel):

    gateway: Gateway = FieldInfo()


class GetGatewayRequest(BaseModel):

    id: str = FieldInfo(default="")


class GetGatewayResponse(BaseModel):

    gateway: Gateway = FieldInfo()
    created_at: datetime = FieldInfo(default_factory=datetime.now)
    updated_at: datetime = FieldInfo(default_factory=datetime.now)
    first_seen_at: datetime = FieldInfo(default_factory=datetime.now)
    last_seen_at: datetime = FieldInfo(default_factory=datetime.now)


class DeleteGatewayRequest(BaseModel):

    id: str = FieldInfo(default="")


class GenerateGatewayClientCertificateRequest(BaseModel):

    gateway_id: str = FieldInfo(default="")


class GenerateGatewayClientCertificateResponse(BaseModel):

    tls_cert: str = FieldInfo(default="")
    tls_key: str = FieldInfo(default="")
    ca_cert: str = FieldInfo(default="")
    expires_at: datetime = FieldInfo(default_factory=datetime.now)


class ListGatewayRequest(BaseModel):

    limit: int = FieldInfo(default=0)
    offset: int = FieldInfo(default=0)
    organization_id: int = FieldInfo(default=0)
    search: str = FieldInfo(default="")


class GatewayListItem(BaseModel):

    id: str = FieldInfo(default="")
    name: str = FieldInfo(default="")
    description: str = FieldInfo(default="")
    created_at: datetime = FieldInfo(default_factory=datetime.now)
    updated_at: datetime = FieldInfo(default_factory=datetime.now)
    first_seen_at: datetime = FieldInfo(default_factory=datetime.now)
    last_seen_at: datetime = FieldInfo(default_factory=datetime.now)
    organization_id: int = FieldInfo(default=0)
    network_server_id: int = FieldInfo(default=0)
    location: Location = FieldInfo()
    network_server_name: str = FieldInfo(default="")


class ListGatewayResponse(BaseModel):

    total_count: int = FieldInfo(default=0)
    result: typing.List[GatewayListItem] = FieldInfo(default_factory=list)


class UpdateGatewayRequest(BaseModel):

    gateway: Gateway = FieldInfo()


class GatewayStats(BaseModel):

    timestamp: datetime = FieldInfo(default_factory=datetime.now)
    rx_packets_received: int = FieldInfo(default=0)
    rx_packets_received_ok: int = FieldInfo(default=0)
    tx_packets_received: int = FieldInfo(default=0)
    tx_packets_emitted: int = FieldInfo(default=0)
    tx_packets_per_frequency: typing.Dict[int, int] = FieldInfo(default_factory=dict)
    rx_packets_per_frequency: typing.Dict[int, int] = FieldInfo(default_factory=dict)
    tx_packets_per_dr: typing.Dict[int, int] = FieldInfo(default_factory=dict)
    rx_packets_per_dr: typing.Dict[int, int] = FieldInfo(default_factory=dict)
    tx_packets_per_status: typing.Dict[str, int] = FieldInfo(default_factory=dict)


class GetGatewayStatsRequest(BaseModel):

    gateway_id: str = FieldInfo(default="")
    interval: str = FieldInfo(default="")
    start_timestamp: datetime = FieldInfo(default_factory=datetime.now)
    end_timestamp: datetime = FieldInfo(default_factory=datetime.now)


class GetGatewayStatsResponse(BaseModel):

    result: typing.List[GatewayStats] = FieldInfo(default_factory=list)


class PingRX(BaseModel):

    gateway_id: str = FieldInfo(default="")
    rssi: int = FieldInfo(default=0)
    lora_snr: float = FieldInfo(default=0.0)
    latitude: float = FieldInfo(default=0.0)
    longitude: float = FieldInfo(default=0.0)
    altitude: float = FieldInfo(default=0.0)


class GetLastPingRequest(BaseModel):

    gateway_id: str = FieldInfo(default="")


class GetLastPingResponse(BaseModel):

    created_at: datetime = FieldInfo(default_factory=datetime.now)
    frequency: int = FieldInfo(default=0)
    dr: int = FieldInfo(default=0)
    ping_rx: typing.List[PingRX] = FieldInfo(default_factory=list)


class StreamGatewayFrameLogsRequest(BaseModel):

    gateway_id: str = FieldInfo(default="")


class StreamGatewayFrameLogsResponse(BaseModel):

    _one_of_dict = {
        "StreamGatewayFrameLogsResponse.frame": {
            "fields": {"downlink_frame", "uplink_frame"}
        }
    }
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    uplink_frame: UplinkFrameLog = FieldInfo()
    downlink_frame: DownlinkFrameLog = FieldInfo()
