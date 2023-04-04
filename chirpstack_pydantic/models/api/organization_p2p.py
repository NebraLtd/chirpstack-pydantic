# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)
# type: ignore

from datetime import datetime
from google.protobuf.message import Message  # type: ignore
from chirpstack_pydantic.base import BaseModel
from pydantic.fields import FieldInfo
import typing


class Organization(BaseModel):

    id: int = FieldInfo(default=0)
    name: str = FieldInfo(default="")
    display_name: str = FieldInfo(default="")
    can_have_gateways: bool = FieldInfo(default=False)
    max_gateway_count: int = FieldInfo(default=0)
    max_device_count: int = FieldInfo(default=0)


class OrganizationListItem(BaseModel):

    id: int = FieldInfo(default=0)
    name: str = FieldInfo(default="")
    display_name: str = FieldInfo(default="")
    can_have_gateways: bool = FieldInfo(default=False)
    created_at: datetime = FieldInfo(default_factory=datetime.now)
    updated_at: datetime = FieldInfo(default_factory=datetime.now)


class GetOrganizationRequest(BaseModel):

    id: int = FieldInfo(default=0)


class GetOrganizationResponse(BaseModel):

    organization: Organization = FieldInfo()
    created_at: datetime = FieldInfo(default_factory=datetime.now)
    updated_at: datetime = FieldInfo(default_factory=datetime.now)


class CreateOrganizationRequest(BaseModel):

    organization: Organization = FieldInfo()


class CreateOrganizationResponse(BaseModel):

    id: int = FieldInfo(default=0)


class UpdateOrganizationRequest(BaseModel):

    organization: Organization = FieldInfo()


class DeleteOrganizationRequest(BaseModel):

    id: int = FieldInfo(default=0)


class ListOrganizationRequest(BaseModel):

    limit: int = FieldInfo(default=0)
    offset: int = FieldInfo(default=0)
    search: str = FieldInfo(default="")


class ListOrganizationResponse(BaseModel):

    total_count: int = FieldInfo(default=0)
    result: typing.List[OrganizationListItem] = FieldInfo(default_factory=list)


class OrganizationUser(BaseModel):

    organization_id: int = FieldInfo(default=0)
    user_id: int = FieldInfo(default=0)
    is_admin: bool = FieldInfo(default=False)
    is_device_admin: bool = FieldInfo(default=False)
    is_gateway_admin: bool = FieldInfo(default=False)
    email: str = FieldInfo(default="")


class OrganizationUserListItem(BaseModel):

    user_id: int = FieldInfo(default=0)
    email: str = FieldInfo(default="")
    is_admin: bool = FieldInfo(default=False)
    is_device_admin: bool = FieldInfo(default=False)
    is_gateway_admin: bool = FieldInfo(default=False)
    created_at: datetime = FieldInfo(default_factory=datetime.now)
    updated_at: datetime = FieldInfo(default_factory=datetime.now)


class AddOrganizationUserRequest(BaseModel):

    organization_user: OrganizationUser = FieldInfo()


class UpdateOrganizationUserRequest(BaseModel):

    organization_user: OrganizationUser = FieldInfo()


class DeleteOrganizationUserRequest(BaseModel):

    organization_id: int = FieldInfo(default=0)
    user_id: int = FieldInfo(default=0)


class ListOrganizationUsersRequest(BaseModel):

    organization_id: int = FieldInfo(default=0)
    limit: int = FieldInfo(default=0)
    offset: int = FieldInfo(default=0)


class ListOrganizationUsersResponse(BaseModel):

    total_count: int = FieldInfo(default=0)
    result: typing.List[OrganizationUserListItem] = FieldInfo(default_factory=list)


class GetOrganizationUserRequest(BaseModel):

    organization_id: int = FieldInfo(default=0)
    user_id: int = FieldInfo(default=0)


class GetOrganizationUserResponse(BaseModel):

    organization_user: OrganizationUser = FieldInfo()
    created_at: datetime = FieldInfo(default_factory=datetime.now)
    updated_at: datetime = FieldInfo(default_factory=datetime.now)
