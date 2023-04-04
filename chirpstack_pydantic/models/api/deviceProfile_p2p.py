# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)
# type: ignore

import typing
from uuid import UUID
from datetime import datetime

from google.protobuf.message import Message  # type: ignore
from chirpstack_pydantic.base import BaseModel
from pydantic.fields import FieldInfo

from .profiles_p2p import DeviceProfile
from ..common.common_p2p import Region


class CreateDeviceProfileRequest(BaseModel):

    device_profile: DeviceProfile = FieldInfo()


class CreateDeviceProfileResponse(BaseModel):

    id: str = FieldInfo(default="")


class GetDeviceProfileRequest(BaseModel):

    id: str = FieldInfo(default="")


class GetDeviceProfileResponse(BaseModel):

    device_profile: DeviceProfile = FieldInfo()
    created_at: datetime = FieldInfo(default_factory=datetime.now)
    updated_at: datetime = FieldInfo(default_factory=datetime.now)


class UpdateDeviceProfileRequest(BaseModel):

    device_profile: DeviceProfile = FieldInfo()


class DeleteDeviceProfileRequest(BaseModel):

    id: str = FieldInfo(default="")


class DeviceProfileListItem(BaseModel):

    id: UUID
    name: str = FieldInfo(default="")
    created_at: datetime = FieldInfo(default_factory=datetime.now)
    updated_at: datetime = FieldInfo(default_factory=datetime.now)
    mac_version: str
    supports_otaa: bool


class ListDeviceProfileRequest(BaseModel):

    limit: int = FieldInfo(default=0)
    offset: int = FieldInfo(default=0)
    search: str = None
    tenant_id: UUID = None


class ListDeviceProfilesResponse(BaseModel):

    total_count: int = FieldInfo(default=0)
    result: typing.List[DeviceProfileListItem] = FieldInfo(default_factory=list)
