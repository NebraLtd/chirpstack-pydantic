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


class Device(BaseModel):

    dev_eui: str = FieldInfo(default="")
    name: str = FieldInfo(default="")
    application_id: int = FieldInfo(default=0)
    description: str = FieldInfo(default="")
    device_profile_id: str = FieldInfo(default="")
    skip_f_cnt_check: bool = FieldInfo(default=False)
    reference_altitude: float = FieldInfo(default=0.0)
    variables: typing.Dict[str, str] = FieldInfo(default_factory=dict)
    tags: typing.Dict[str, str] = FieldInfo(default_factory=dict)
    is_disabled: bool = FieldInfo(default=False)


class DeviceListItem(BaseModel):

    dev_eui: str = FieldInfo(default="")
    name: str = FieldInfo(default="")
    application_id: int = FieldInfo(default=0)
    description: str = FieldInfo(default="")
    device_profile_id: str = FieldInfo(default="")
    device_profile_name: str = FieldInfo(default="")
    device_status_battery: int = FieldInfo(default=0)
    device_status_margin: int = FieldInfo(default=0)
    device_status_external_power_source: bool = FieldInfo(default=False)
    device_status_battery_level_unavailable: bool = FieldInfo(default=False)
    device_status_battery_level: float = FieldInfo(default=0.0)
    last_seen_at: datetime = FieldInfo(default_factory=datetime.now)


class DeviceKeys(BaseModel):

    dev_eui: str = FieldInfo(default="")
    nwk_key: str = FieldInfo(default="")
    app_key: str = FieldInfo(default="")
    gen_app_key: str = FieldInfo(default="")


class CreateDeviceRequest(BaseModel):

    device: Device = FieldInfo()


class GetDeviceRequest(BaseModel):

    dev_eui: str = FieldInfo(default="")


class GetDeviceResponse(BaseModel):

    device: Device = FieldInfo()
    last_seen_at: datetime = FieldInfo(default_factory=datetime.now)
    device_status_battery: int = FieldInfo(default=0)
    device_status_margin: int = FieldInfo(default=0)
    location: Location = FieldInfo()


class ListDeviceRequest(BaseModel):

    limit: int = FieldInfo(default=0)
    offset: int = FieldInfo(default=0)
    application_id: int = FieldInfo(default=0)
    search: str = FieldInfo(default="")
    multicast_group_id: str = FieldInfo(default="")
    service_profile_id: str = FieldInfo(default="")
    tags: typing.Dict[str, str] = FieldInfo(default_factory=dict)


class ListDeviceResponse(BaseModel):

    total_count: int = FieldInfo(default=0)
    result: typing.List[DeviceListItem] = FieldInfo(default_factory=list)


class DeleteDeviceRequest(BaseModel):

    dev_eui: str = FieldInfo(default="")


class UpdateDeviceRequest(BaseModel):

    device: Device = FieldInfo()


class CreateDeviceKeysRequest(BaseModel):

    device_keys: DeviceKeys = FieldInfo()


class GetDeviceKeysRequest(BaseModel):

    dev_eui: str = FieldInfo(default="")


class GetDeviceKeysResponse(BaseModel):

    device_keys: DeviceKeys = FieldInfo()


class UpdateDeviceKeysRequest(BaseModel):

    device_keys: DeviceKeys = FieldInfo()


class DeleteDeviceKeysRequest(BaseModel):

    dev_eui: str = FieldInfo(default="")


class DeviceActivation(BaseModel):

    dev_eui: str = FieldInfo(default="")
    dev_addr: str = FieldInfo(default="")
    app_s_key: str = FieldInfo(default="")
    nwk_s_enc_key: str = FieldInfo(default="")
    s_nwk_s_int_key: str = FieldInfo(default="")
    f_nwk_s_int_key: str = FieldInfo(default="")
    f_cnt_up: int = FieldInfo(default=0)
    n_f_cnt_down: int = FieldInfo(default=0)
    a_f_cnt_down: int = FieldInfo(default=0)


class ActivateDeviceRequest(BaseModel):

    device_activation: DeviceActivation = FieldInfo()


class DeactivateDeviceRequest(BaseModel):

    dev_eui: str = FieldInfo(default="")


class GetDeviceActivationRequest(BaseModel):

    dev_eui: str = FieldInfo(default="")


class GetDeviceActivationResponse(BaseModel):

    device_activation: DeviceActivation = FieldInfo()


class GetRandomDevAddrRequest(BaseModel):

    dev_eui: str = FieldInfo(default="")


class GetRandomDevAddrResponse(BaseModel):

    dev_addr: str = FieldInfo(default="")


class DeviceStats(BaseModel):

    timestamp: datetime = FieldInfo(default_factory=datetime.now)
    rx_packets: int = FieldInfo(default=0)
    gw_rssi: float = FieldInfo(default=0.0)
    gw_snr: float = FieldInfo(default=0.0)
    rx_packets_per_frequency: typing.Dict[int, int] = FieldInfo(default_factory=dict)
    rx_packets_per_dr: typing.Dict[int, int] = FieldInfo(default_factory=dict)
    errors: typing.Dict[str, int] = FieldInfo(default_factory=dict)


class GetDeviceStatsRequest(BaseModel):

    dev_eui: str = FieldInfo(default="")
    interval: str = FieldInfo(default="")
    start_timestamp: datetime = FieldInfo(default_factory=datetime.now)
    end_timestamp: datetime = FieldInfo(default_factory=datetime.now)


class GetDeviceStatsResponse(BaseModel):

    result: typing.List[DeviceStats] = FieldInfo(default_factory=list)


class StreamDeviceFrameLogsRequest(BaseModel):

    dev_eui: str = FieldInfo(default="")


class StreamDeviceFrameLogsResponse(BaseModel):

    _one_of_dict = {
        "StreamDeviceFrameLogsResponse.frame": {
            "fields": {"downlink_frame", "uplink_frame"}
        }
    }
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    uplink_frame: UplinkFrameLog = FieldInfo()
    downlink_frame: DownlinkFrameLog = FieldInfo()


class StreamDeviceEventLogsRequest(BaseModel):

    dev_eui: str = FieldInfo(default="")


class StreamDeviceEventLogsResponse(BaseModel):

    type: str = FieldInfo(default="")
    payload_json: str = FieldInfo(default="")
    published_at: datetime = FieldInfo(default_factory=datetime.now)
    stream_id: str = FieldInfo(default="")


class ClearDeviceNoncesRequest(BaseModel):

    dev_eui: str = FieldInfo(default="")
