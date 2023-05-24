# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)
# type: ignore

from ..common.common_p2p import Location
from ..common.common_p2p import MType
from ..common.common_p2p import Modulation
from ..common.common_p2p import Region
from ..gw.gw_p2p import DownlinkTXInfo
from ..gw.gw_p2p import UplinkRXInfo
from ..gw.gw_p2p import UplinkTXInfo
from ..profiles_p2p import DeviceProfile
from ..profiles_p2p import RoutingProfile
from ..profiles_p2p import ServiceProfile
from datetime import datetime
from datetime import timedelta
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from chirpstack_pydantic.validators import check_one_of
from chirpstack_pydantic.util import Timedelta
from chirpstack_pydantic.base import BaseModel
from pydantic import root_validator
from pydantic.fields import FieldInfo
import typing


class RXWindow(IntEnum):
    RX1 = 0
    RX2 = 1


class AggregationInterval(IntEnum):
    SECOND = 0
    MINUTE = 1
    HOUR = 2
    DAY = 3
    WEEK = 4
    MONTH = 5
    QUARTER = 6
    YEAR = 7


class MulticastGroupType(IntEnum):
    CLASS_C = 0
    CLASS_B = 1


class CreateServiceProfileRequest(BaseModel):

    service_profile: ServiceProfile = FieldInfo()


class CreateServiceProfileResponse(BaseModel):

    id: bytes = FieldInfo(default=b"")


class GetServiceProfileRequest(BaseModel):

    id: bytes = FieldInfo(default=b"")


class GetServiceProfileResponse(BaseModel):

    service_profile: ServiceProfile = FieldInfo()
    created_at: datetime = FieldInfo(default_factory=datetime.now)
    updated_at: datetime = FieldInfo(default_factory=datetime.now)


class UpdateServiceProfileRequest(BaseModel):

    service_profile: ServiceProfile = FieldInfo()


class DeleteServiceProfileRequest(BaseModel):

    id: bytes = FieldInfo(default=b"")


class CreateRoutingProfileRequest(BaseModel):

    routing_profile: RoutingProfile = FieldInfo()


class CreateRoutingProfileResponse(BaseModel):

    id: bytes = FieldInfo(default=b"")


class GetRoutingProfileRequest(BaseModel):

    id: bytes = FieldInfo(default=b"")


class GetRoutingProfileResponse(BaseModel):

    routing_profile: RoutingProfile = FieldInfo()
    created_at: datetime = FieldInfo(default_factory=datetime.now)
    updated_at: datetime = FieldInfo(default_factory=datetime.now)


class UpdateRoutingProfileRequest(BaseModel):

    routing_profile: RoutingProfile = FieldInfo()


class DeleteRoutingProfileRequest(BaseModel):

    id: bytes = FieldInfo(default=b"")


class CreateDeviceProfileRequest(BaseModel):

    device_profile: DeviceProfile = FieldInfo()


class CreateDeviceProfileResponse(BaseModel):

    id: bytes = FieldInfo(default=b"")


class GetDeviceProfileRequest(BaseModel):

    id: bytes = FieldInfo(default=b"")


class GetDeviceProfileResponse(BaseModel):

    device_profile: DeviceProfile = FieldInfo()
    created_at: datetime = FieldInfo(default_factory=datetime.now)
    updated_at: datetime = FieldInfo(default_factory=datetime.now)


class UpdateDeviceProfileRequest(BaseModel):

    device_profile: DeviceProfile = FieldInfo()


class DeleteDeviceProfileRequest(BaseModel):

    id: bytes = FieldInfo(default=b"")


class Device(BaseModel):

    dev_eui: bytes = FieldInfo(default=b"")
    device_profile_id: bytes = FieldInfo(default=b"")
    service_profile_id: bytes = FieldInfo(default=b"")
    routing_profile_id: bytes = FieldInfo(default=b"")
    skip_f_cnt_check: bool = FieldInfo(default=False)
    reference_altitude: float = FieldInfo(default=0.0)
    is_disabled: bool = FieldInfo(default=False)


class CreateDeviceRequest(BaseModel):

    device: Device = FieldInfo()


class GetDeviceRequest(BaseModel):

    dev_eui: bytes = FieldInfo(default=b"")


class GetDeviceResponse(BaseModel):

    device: Device = FieldInfo()
    created_at: datetime = FieldInfo(default_factory=datetime.now)
    updated_at: datetime = FieldInfo(default_factory=datetime.now)


class UpdateDeviceRequest(BaseModel):

    device: Device = FieldInfo()


class DeleteDeviceRequest(BaseModel):

    dev_eui: bytes = FieldInfo(default=b"")


class DeviceActivation(BaseModel):

    dev_eui: bytes = FieldInfo(default=b"")
    dev_addr: bytes = FieldInfo(default=b"")
    s_nwk_s_int_key: bytes = FieldInfo(default=b"")
    f_nwk_s_int_key: bytes = FieldInfo(default=b"")
    nwk_s_enc_key: bytes = FieldInfo(default=b"")
    f_cnt_up: int = FieldInfo(default=0)
    n_f_cnt_down: int = FieldInfo(default=0)
    a_f_cnt_down: int = FieldInfo(default=0)
    skip_f_cnt_check: bool = FieldInfo(default=False)


class ActivateDeviceRequest(BaseModel):

    device_activation: DeviceActivation = FieldInfo()


class DeactivateDeviceRequest(BaseModel):

    dev_eui: bytes = FieldInfo(default=b"")


class GetDeviceActivationRequest(BaseModel):

    dev_eui: bytes = FieldInfo(default=b"")


class GetDeviceActivationResponse(BaseModel):

    device_activation: DeviceActivation = FieldInfo()


class GetRandomDevAddrResponse(BaseModel):

    dev_addr: bytes = FieldInfo(default=b"")


class CreateMACCommandQueueItemRequest(BaseModel):

    dev_eui: bytes = FieldInfo(default=b"")
    cid: int = FieldInfo(default=0)
    commands: typing.List[bytes] = FieldInfo(default_factory=list)


class SendProprietaryPayloadRequest(BaseModel):

    mac_payload: bytes = FieldInfo(default=b"")
    mic: bytes = FieldInfo(default=b"")
    gateway_macs: typing.List[bytes] = FieldInfo(default_factory=list)
    polarization_inversion: bool = FieldInfo(default=False)
    frequency: int = FieldInfo(default=0)
    dr: int = FieldInfo(default=0)


class Gateway(BaseModel):

    id: bytes = FieldInfo(default=b"")
    location: Location = FieldInfo()
    gateway_profile_id: bytes = FieldInfo(default=b"")
    boards: typing.List[GatewayBoard] = FieldInfo(default_factory=list)
    routing_profile_id: bytes = FieldInfo(default=b"")
    service_profile_id: bytes = FieldInfo(default=b"")


class GatewayBoard(BaseModel):

    fpga_id: bytes = FieldInfo(default=b"")
    fine_timestamp_key: bytes = FieldInfo(default=b"")


class CreateGatewayRequest(BaseModel):

    gateway: Gateway = FieldInfo()


class GetGatewayRequest(BaseModel):

    id: bytes = FieldInfo(default=b"")


class GetGatewayResponse(BaseModel):

    gateway: Gateway = FieldInfo()
    created_at: datetime = FieldInfo(default_factory=datetime.now)
    updated_at: datetime = FieldInfo(default_factory=datetime.now)
    first_seen_at: datetime = FieldInfo(default_factory=datetime.now)
    last_seen_at: datetime = FieldInfo(default_factory=datetime.now)


class UpdateGatewayRequest(BaseModel):

    gateway: Gateway = FieldInfo()


class DeleteGatewayRequest(BaseModel):

    id: bytes = FieldInfo(default=b"")


class GenerateGatewayClientCertificateRequest(BaseModel):

    id: bytes = FieldInfo(default=b"")


class GenerateGatewayClientCertificateResponse(BaseModel):

    tls_cert: bytes = FieldInfo(default=b"")
    tls_key: bytes = FieldInfo(default=b"")
    ca_cert: bytes = FieldInfo(default=b"")
    expires_at: datetime = FieldInfo(default_factory=datetime.now)


class GatewayStats(BaseModel):

    timestamp: datetime = FieldInfo(default_factory=datetime.now)
    rx_packets_received: int = FieldInfo(default=0)
    rx_packets_received_ok: int = FieldInfo(default=0)
    tx_packets_received: int = FieldInfo(default=0)
    tx_packets_emitted: int = FieldInfo(default=0)


class GetGatewayStatsRequest(BaseModel):

    gateway_id: bytes = FieldInfo(default=b"")
    interval: AggregationInterval = FieldInfo(default=0)
    start_timestamp: datetime = FieldInfo(default_factory=datetime.now)
    end_timestamp: datetime = FieldInfo(default_factory=datetime.now)


class GetGatewayStatsResponse(BaseModel):

    result: typing.List[GatewayStats] = FieldInfo(default_factory=list)


class DeviceQueueItem(BaseModel):

    dev_eui: bytes = FieldInfo(default=b"")
    frm_payload: bytes = FieldInfo(default=b"")
    f_cnt: int = FieldInfo(default=0)
    f_port: int = FieldInfo(default=0)
    confirmed: bool = FieldInfo(default=False)
    dev_addr: bytes = FieldInfo(default=b"")


class CreateDeviceQueueItemRequest(BaseModel):

    item: DeviceQueueItem = FieldInfo()


class FlushDeviceQueueForDevEUIRequest(BaseModel):

    dev_eui: bytes = FieldInfo(default=b"")


class GetDeviceQueueItemsForDevEUIRequest(BaseModel):

    dev_eui: bytes = FieldInfo(default=b"")
    count_only: bool = FieldInfo(default=False)


class GetDeviceQueueItemsForDevEUIResponse(BaseModel):

    items: typing.List[DeviceQueueItem] = FieldInfo(default_factory=list)
    total_count: int = FieldInfo(default=0)


class GetNextDownlinkFCntForDevEUIRequest(BaseModel):

    dev_eui: bytes = FieldInfo(default=b"")


class GetNextDownlinkFCntForDevEUIResponse(BaseModel):

    f_cnt: int = FieldInfo(default=0)


class UplinkFrameLog(BaseModel):

    phy_payload: bytes = FieldInfo(default=b"")
    tx_info: UplinkTXInfo = FieldInfo()
    rx_info: typing.List[UplinkRXInfo] = FieldInfo(default_factory=list)
    m_type: MType = FieldInfo(default=0)
    dev_addr: bytes = FieldInfo(default=b"")
    dev_eui: bytes = FieldInfo(default=b"")
    published_at: datetime = FieldInfo(default_factory=datetime.now)


class DownlinkFrameLog(BaseModel):

    phy_payload: bytes = FieldInfo(default=b"")
    tx_info: DownlinkTXInfo = FieldInfo()
    token: int = FieldInfo(default=0)
    downlink_id: bytes = FieldInfo(default=b"")
    gateway_id: bytes = FieldInfo(default=b"")
    m_type: MType = FieldInfo(default=0)
    dev_addr: bytes = FieldInfo(default=b"")
    dev_eui: bytes = FieldInfo(default=b"")
    published_at: datetime = FieldInfo(default_factory=datetime.now)


class StreamFrameLogsForGatewayRequest(BaseModel):

    gateway_id: bytes = FieldInfo(default=b"")


class StreamFrameLogsForGatewayResponse(BaseModel):

    _one_of_dict = {
        "StreamFrameLogsForGatewayResponse.frame": {
            "fields": {"downlink_frame", "uplink_frame_set"}
        }
    }
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    uplink_frame_set: UplinkFrameLog = FieldInfo()
    downlink_frame: DownlinkFrameLog = FieldInfo()


class StreamFrameLogsForDeviceRequest(BaseModel):

    dev_eui: bytes = FieldInfo(default=b"")


class StreamFrameLogsForDeviceResponse(BaseModel):

    _one_of_dict = {
        "StreamFrameLogsForDeviceResponse.frame": {
            "fields": {"downlink_frame", "uplink_frame_set"}
        }
    }
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    uplink_frame_set: UplinkFrameLog = FieldInfo()
    downlink_frame: DownlinkFrameLog = FieldInfo()


class GetVersionResponse(BaseModel):

    version: str = FieldInfo(default="")
    region: Region = FieldInfo(default=0)


class GatewayProfile(BaseModel):

    id: bytes = FieldInfo(default=b"")
    channels: typing.List[int] = FieldInfo(default_factory=list)
    extra_channels: typing.List[GatewayProfileExtraChannel] = FieldInfo(
        default_factory=list
    )
    stats_interval: Timedelta = FieldInfo(default_factory=timedelta)


class GatewayProfileExtraChannel(BaseModel):

    modulation: Modulation = FieldInfo(default=0)
    frequency: int = FieldInfo(default=0)
    bandwidth: int = FieldInfo(default=0)
    bitrate: int = FieldInfo(default=0)
    spreading_factors: typing.List[int] = FieldInfo(default_factory=list)


class CreateGatewayProfileRequest(BaseModel):

    gateway_profile: GatewayProfile = FieldInfo()


class CreateGatewayProfileResponse(BaseModel):

    id: bytes = FieldInfo(default=b"")


class GetGatewayProfileRequest(BaseModel):

    id: bytes = FieldInfo(default=b"")


class GetGatewayProfileResponse(BaseModel):

    gateway_profile: GatewayProfile = FieldInfo()
    created_at: datetime = FieldInfo(default_factory=datetime.now)
    updated_at: datetime = FieldInfo(default_factory=datetime.now)


class UpdateGatewayProfileRequest(BaseModel):

    gateway_profile: GatewayProfile = FieldInfo()


class DeleteGatewayProfileRequest(BaseModel):

    id: bytes = FieldInfo(default=b"")


class MulticastGroup(BaseModel):

    id: bytes = FieldInfo(default=b"")
    mc_addr: bytes = FieldInfo(default=b"")
    mc_nwk_s_key: bytes = FieldInfo(default=b"")
    f_cnt: int = FieldInfo(default=0)
    group_type: MulticastGroupType = FieldInfo(default=0)
    dr: int = FieldInfo(default=0)
    frequency: int = FieldInfo(default=0)
    ping_slot_period: int = FieldInfo(default=0)
    service_profile_id: bytes = FieldInfo(default=b"")
    routing_profile_id: bytes = FieldInfo(default=b"")


class CreateMulticastGroupRequest(BaseModel):

    multicast_group: MulticastGroup = FieldInfo()


class CreateMulticastGroupResponse(BaseModel):

    id: bytes = FieldInfo(default=b"")


class GetMulticastGroupRequest(BaseModel):

    id: bytes = FieldInfo(default=b"")


class GetMulticastGroupResponse(BaseModel):

    multicast_group: MulticastGroup = FieldInfo()
    created_at: datetime = FieldInfo(default_factory=datetime.now)
    updated_at: datetime = FieldInfo(default_factory=datetime.now)


class UpdateMulticastGroupRequest(BaseModel):

    multicast_group: MulticastGroup = FieldInfo()


class DeleteMulticastGroupRequest(BaseModel):

    id: bytes = FieldInfo(default=b"")


class AddDeviceToMulticastGroupRequest(BaseModel):

    dev_eui: bytes = FieldInfo(default=b"")
    multicast_group_id: bytes = FieldInfo(default=b"")


class RemoveDeviceFromMulticastGroupRequest(BaseModel):

    dev_eui: bytes = FieldInfo(default=b"")
    multicast_group_id: bytes = FieldInfo(default=b"")


class MulticastQueueItem(BaseModel):

    multicast_group_id: bytes = FieldInfo(default=b"")
    f_cnt: int = FieldInfo(default=0)
    f_port: int = FieldInfo(default=0)
    frm_payload: bytes = FieldInfo(default=b"")


class EnqueueMulticastQueueItemRequest(BaseModel):

    multicast_queue_item: MulticastQueueItem = FieldInfo()


class FlushMulticastQueueForMulticastGroupRequest(BaseModel):

    multicast_group_id: bytes = FieldInfo(default=b"")


class GetMulticastQueueItemsForMulticastGroupRequest(BaseModel):

    multicast_group_id: bytes = FieldInfo(default=b"")


class GetMulticastQueueItemsForMulticastGroupResponse(BaseModel):

    multicast_queue_items: typing.List[MulticastQueueItem] = FieldInfo(
        default_factory=list
    )


class GetADRAlgorithmsResponse(BaseModel):

    adr_algorithms: typing.List[ADRAlgorithm] = FieldInfo(default_factory=list)


class ADRAlgorithm(BaseModel):

    id: str = FieldInfo(default="")
    name: str = FieldInfo(default="")


class ClearDeviceNoncesRequest(BaseModel):

    dev_eui: bytes = FieldInfo(default=b"")
