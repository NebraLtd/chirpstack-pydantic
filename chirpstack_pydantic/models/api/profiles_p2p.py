# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)
# type: ignore

from datetime import timedelta
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from protobuf_to_pydantic.util import Timedelta
from chirpstack_pydantic.base import BaseModel
from pydantic.fields import FieldInfo
import typing


class RatePolicy(IntEnum):
    DROP = 0
    MARK = 1


class ServiceProfile(BaseModel):

    id: str = FieldInfo(default="")
    name: str = FieldInfo(default="")
    organization_id: int = FieldInfo(default=0)
    network_server_id: int = FieldInfo(default=0)
    ul_rate: int = FieldInfo(default=0)
    ul_bucket_size: int = FieldInfo(default=0)
    ul_rate_policy: RatePolicy = FieldInfo(default=0)
    dl_rate: int = FieldInfo(default=0)
    dl_bucket_size: int = FieldInfo(default=0)
    dl_rate_policy: RatePolicy = FieldInfo(default=0)
    add_gw_metadata: bool = FieldInfo(default=False)
    dev_status_req_freq: int = FieldInfo(default=0)
    report_dev_status_battery: bool = FieldInfo(default=False)
    report_dev_status_margin: bool = FieldInfo(default=False)
    dr_min: int = FieldInfo(default=0)
    dr_max: int = FieldInfo(default=0)
    channel_mask: bytes = FieldInfo(default=b"")
    pr_allowed: bool = FieldInfo(default=False)
    hr_allowed: bool = FieldInfo(default=False)
    ra_allowed: bool = FieldInfo(default=False)
    nwk_geo_loc: bool = FieldInfo(default=False)
    target_per: int = FieldInfo(default=0)
    min_gw_diversity: int = FieldInfo(default=0)
    gws_private: bool = FieldInfo(default=False)


class DeviceProfile(BaseModel):

    id: str = FieldInfo(default="")
    name: str = FieldInfo(default="")
    organization_id: int = FieldInfo(default=0)
    network_server_id: int = FieldInfo(default=0)
    supports_class_b: bool = FieldInfo(default=False)
    class_b_timeout: int = FieldInfo(default=0)
    ping_slot_period: int = FieldInfo(default=0)
    ping_slot_dr: int = FieldInfo(default=0)
    ping_slot_freq: int = FieldInfo(default=0)
    supports_class_c: bool = FieldInfo(default=False)
    class_c_timeout: int = FieldInfo(default=0)
    mac_version: str = FieldInfo(default="")
    reg_params_revision: str = FieldInfo(default="")
    rx_delay_1: int = FieldInfo(default=0)
    rx_dr_offset_1: int = FieldInfo(default=0)
    rx_datarate_2: int = FieldInfo(default=0)
    rx_freq_2: int = FieldInfo(default=0)
    factory_preset_freqs: typing.List[int] = FieldInfo(default_factory=list)
    max_eirp: int = FieldInfo(default=0)
    max_duty_cycle: int = FieldInfo(default=0)
    supports_join: bool = FieldInfo(default=False)
    rf_region: str = FieldInfo(default="")
    supports_32bit_f_cnt: bool = FieldInfo(default=False)
    payload_codec: str = FieldInfo(default="")
    payload_encoder_script: str = FieldInfo(default="")
    payload_decoder_script: str = FieldInfo(default="")
    geoloc_buffer_ttl: int = FieldInfo(default=0)
    geoloc_min_buffer_size: int = FieldInfo(default=0)
    tags: typing.Dict[str, str] = FieldInfo(default_factory=dict)
    uplink_interval: Timedelta = FieldInfo(default_factory=timedelta)
    adr_algorithm_id: str = FieldInfo(default="")
