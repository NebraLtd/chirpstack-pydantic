# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)
# type: ignore

from uuid import UUID
from datetime import datetime
from google.protobuf.message import Message  # type: ignore
from chirpstack_pydantic.base import BaseModel
from pydantic.fields import FieldInfo
import typing


class User(BaseModel):

    id: UUID = FieldInfo(default=UUID('00000000-0000-0000-0000-000000000000'))
    session_ttl: int = FieldInfo(default=0)
    is_admin: bool = FieldInfo(default=False)
    is_active: bool = FieldInfo(default=False)
    email: str = FieldInfo(default="")
    note: str = FieldInfo(default="")


class UserListItem(BaseModel):

    id: UUID = FieldInfo(default=UUID('00000000-0000-0000-0000-000000000000'))
    email: str = FieldInfo(default="")
    is_admin: bool = FieldInfo(default=False)
    is_active: bool = FieldInfo(default=False)
    created_at: datetime = FieldInfo(default_factory=datetime.now)
    updated_at: datetime = FieldInfo(default_factory=datetime.now)


class UserOrganization(BaseModel):

    organization_id: UUID = FieldInfo(default=UUID('00000000-0000-0000-0000-000000000000'))
    is_admin: bool = FieldInfo(default=False)
    is_device_admin: bool = FieldInfo(default=False)
    is_gateway_admin: bool = FieldInfo(default=False)


class CreateUserRequest(BaseModel):

    user: User = FieldInfo()
    password: str = FieldInfo(default="")
    organizations: typing.List[UserOrganization] = FieldInfo(default_factory=list)


class CreateUserResponse(BaseModel):

    id: UUID = FieldInfo(default=UUID('00000000-0000-0000-0000-000000000000'))


class GetUserRequest(BaseModel):

    id: UUID = FieldInfo(default=UUID('00000000-0000-0000-0000-000000000000'))


class GetUserResponse(BaseModel):

    user: User = FieldInfo()
    created_at: datetime = FieldInfo(default_factory=datetime.now)
    updated_at: datetime = FieldInfo(default_factory=datetime.now)


class UpdateUserRequest(BaseModel):

    user: User = FieldInfo()


class DeleteUserRequest(BaseModel):

    id: UUID = FieldInfo(default=UUID('00000000-0000-0000-0000-000000000000'))


class ListUserRequest(BaseModel):

    limit: int = FieldInfo(default=0)
    offset: int = FieldInfo(default=0)


class ListUserResponse(BaseModel):

    total_count: int = FieldInfo(default=0)
    result: typing.List[UserListItem] = FieldInfo(default_factory=list)


class UpdateUserPasswordRequest(BaseModel):

    user_id: UUID = FieldInfo(default=UUID('00000000-0000-0000-0000-000000000000'))
    password: str = FieldInfo(default="")
