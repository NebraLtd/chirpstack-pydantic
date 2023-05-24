# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)
# type: ignore

from ..common.common_p2p import Modulation
from datetime import datetime
from datetime import timedelta
from google.protobuf.message import Message  # type: ignore
from chirpstack_pydantic.util import Timedelta
from chirpstack_pydantic.base import BaseModel
from pydantic.fields import FieldInfo
import typing


class GatewayProfileExtraChannel(BaseModel):

    modulation: Modulation = FieldInfo(default=0)
    frequency: int = FieldInfo(default=0)
    bandwidth: int = FieldInfo(default=0)
    bitrate: int = FieldInfo(default=0)
    spreading_factors: typing.List[int] = FieldInfo(default_factory=list)


class GatewayProfile(BaseModel):

    id: str = FieldInfo(default="")
    name: str = FieldInfo(default="")
    network_server_id: int = FieldInfo(default=0)
    channels: typing.List[int] = FieldInfo(default_factory=list)
    extra_channels: typing.List[GatewayProfileExtraChannel] = FieldInfo(
        default_factory=list
    )
    stats_interval: Timedelta = FieldInfo(default_factory=timedelta)


class GatewayProfileListItem(BaseModel):

    id: str = FieldInfo(default="")
    name: str = FieldInfo(default="")
    network_server_id: int = FieldInfo(default=0)
    network_server_name: str = FieldInfo(default="")
    created_at: datetime = FieldInfo(default_factory=datetime.now)
    updated_at: datetime = FieldInfo(default_factory=datetime.now)


class CreateGatewayProfileRequest(BaseModel):

    gateway_profile: GatewayProfile = FieldInfo()


class CreateGatewayProfileResponse(BaseModel):

    id: str = FieldInfo(default="")


class GetGatewayProfileRequest(BaseModel):

    id: str = FieldInfo(default="")


class GetGatewayProfileResponse(BaseModel):

    gateway_profile: GatewayProfile = FieldInfo()
    created_at: datetime = FieldInfo(default_factory=datetime.now)
    updated_at: datetime = FieldInfo(default_factory=datetime.now)


class UpdateGatewayProfileRequest(BaseModel):

    gateway_profile: GatewayProfile = FieldInfo()


class DeleteGatewayProfileRequest(BaseModel):

    id: str = FieldInfo(default="")


class ListGatewayProfilesRequest(BaseModel):

    limit: int = FieldInfo(default=0)
    offset: int = FieldInfo(default=0)
    network_server_id: int = FieldInfo(default=0)


class ListGatewayProfilesResponse(BaseModel):

    total_count: int = FieldInfo(default=0)
    result: typing.List[GatewayProfileListItem] = FieldInfo(default_factory=list)
