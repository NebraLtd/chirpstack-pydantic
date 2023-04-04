# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)
# type: ignore

from .profiles_p2p import ServiceProfile
from datetime import datetime
from google.protobuf.message import Message  # type: ignore
from chirpstack_pydantic.base import BaseModel
from pydantic.fields import FieldInfo
import typing


class CreateServiceProfileRequest(BaseModel):

    service_profile: ServiceProfile = FieldInfo()


class CreateServiceProfileResponse(BaseModel):

    id: str = FieldInfo(default="")


class GetServiceProfileRequest(BaseModel):

    id: str = FieldInfo(default="")


class GetServiceProfileResponse(BaseModel):

    service_profile: ServiceProfile = FieldInfo()
    created_at: datetime = FieldInfo(default_factory=datetime.now)
    updated_at: datetime = FieldInfo(default_factory=datetime.now)


class UpdateServiceProfileRequest(BaseModel):

    service_profile: ServiceProfile = FieldInfo()


class DeleteServiceProfileRequest(BaseModel):

    id: str = FieldInfo(default="")


class ListServiceProfileRequest(BaseModel):

    limit: int = FieldInfo(default=0)
    offset: int = FieldInfo(default=0)
    organization_id: int = FieldInfo(default=0)
    network_server_id: int = FieldInfo(default=0)


class ServiceProfileListItem(BaseModel):

    id: str = FieldInfo(default="")
    name: str = FieldInfo(default="")
    organization_id: int = FieldInfo(default=0)
    network_server_id: int = FieldInfo(default=0)
    created_at: datetime = FieldInfo(default_factory=datetime.now)
    updated_at: datetime = FieldInfo(default_factory=datetime.now)
    network_server_name: str = FieldInfo(default="")


class ListServiceProfileResponse(BaseModel):

    total_count: int = FieldInfo(default=0)
    result: typing.List[ServiceProfileListItem] = FieldInfo(default_factory=list)
