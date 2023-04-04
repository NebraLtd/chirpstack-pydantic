# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)
# type: ignore

from .user_p2p import User
from datetime import datetime
from google.protobuf.message import Message  # type: ignore
from chirpstack_pydantic.base import BaseModel
from pydantic.fields import FieldInfo
import typing


class APIKey(BaseModel):

    id: str = FieldInfo(default="")
    name: str = FieldInfo(default="")
    is_admin: bool = FieldInfo(default=False)
    organization_id: int = FieldInfo(default=0)
    application_id: int = FieldInfo(default=0)


class CreateAPIKeyRequest(BaseModel):

    api_key: APIKey = FieldInfo()


class CreateAPIKeyResponse(BaseModel):

    id: str = FieldInfo(default="")
    jwt_token: str = FieldInfo(default="")


class DeleteAPIKeyRequest(BaseModel):

    id: str = FieldInfo(default="")


class ListAPIKeysRequest(BaseModel):

    limit: int = FieldInfo(default=0)
    offset: int = FieldInfo(default=0)
    is_admin: bool = FieldInfo(default=False)
    organization_id: int = FieldInfo(default=0)
    application_id: int = FieldInfo(default=0)


class ListAPIKeysResponse(BaseModel):

    total_count: int = FieldInfo(default=0)
    result: typing.List[APIKey] = FieldInfo(default_factory=list)


class OrganizationLink(BaseModel):

    organization_id: int = FieldInfo(default=0)
    organization_name: str = FieldInfo(default="")
    is_admin: bool = FieldInfo(default=False)
    is_device_admin: bool = FieldInfo(default=False)
    is_gateway_admin: bool = FieldInfo(default=False)
    created_at: datetime = FieldInfo(default_factory=datetime.now)
    updated_at: datetime = FieldInfo(default_factory=datetime.now)


class LoginRequest(BaseModel):

    email: str = FieldInfo(default="")
    password: str = FieldInfo(default="")


class LoginResponse(BaseModel):

    jwt: str = FieldInfo(default="")


class ProfileResponse(BaseModel):

    user: User = FieldInfo()
    organizations: typing.List[OrganizationLink] = FieldInfo(default_factory=list)


class GlobalSearchResult(BaseModel):

    kind: str = FieldInfo(default="")
    score: float = FieldInfo(default=0.0)
    organization_id: int = FieldInfo(default=0)
    organization_name: str = FieldInfo(default="")
    application_id: int = FieldInfo(default=0)
    application_name: str = FieldInfo(default="")
    device_dev_eui: str = FieldInfo(default="")
    device_name: str = FieldInfo(default="")
    gateway_mac: str = FieldInfo(default="")
    gateway_name: str = FieldInfo(default="")


class GlobalSearchResponse(BaseModel):

    result: typing.List[GlobalSearchResult] = FieldInfo(default_factory=list)


class GlobalSearchRequest(BaseModel):

    search: str = FieldInfo(default="")
    limit: int = FieldInfo(default=0)
    offset: int = FieldInfo(default=0)


class Branding(BaseModel):

    registration: str = FieldInfo(default="")
    footer: str = FieldInfo(default="")


class OpenIDConnect(BaseModel):

    enabled: bool = FieldInfo(default=False)
    login_url: str = FieldInfo(default="")
    login_label: str = FieldInfo(default="")
    logout_url: str = FieldInfo(default="")


class SettingsResponse(BaseModel):

    branding: Branding = FieldInfo()
    openid_connect: OpenIDConnect = FieldInfo()


class OpenIDConnectLoginRequest(BaseModel):

    code: str = FieldInfo(default="")
    state: str = FieldInfo(default="")


class OpenIDConnectLoginResponse(BaseModel):

    jwt_token: str = FieldInfo(default="")


class GetDevicesSummaryRequest(BaseModel):

    organization_id: int = FieldInfo(default=0)


class GetDevicesSummaryResponse(BaseModel):

    active_count: int = FieldInfo(default=0)
    inactive_count: int = FieldInfo(default=0)
    dr_count: typing.Dict[int, int] = FieldInfo(default_factory=dict)
    never_seen_count: int = FieldInfo(default=0)


class GetGatewaysSummaryRequest(BaseModel):

    organization_id: int = FieldInfo(default=0)


class GetGatewaysSummaryResponse(BaseModel):

    active_count: int = FieldInfo(default=0)
    inactive_count: int = FieldInfo(default=0)
    never_seen_count: int = FieldInfo(default=0)
