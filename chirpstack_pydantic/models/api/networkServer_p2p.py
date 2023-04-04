# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)
# type: ignore

from datetime import datetime
from google.protobuf.message import Message  # type: ignore
from chirpstack_pydantic.base import BaseModel
from pydantic.fields import FieldInfo
import typing


class ADRAlgorithm(BaseModel):

    id: str = FieldInfo(default="")
    name: str = FieldInfo(default="")


class NetworkServer(BaseModel):

    id: int = FieldInfo(default=0)
    name: str = FieldInfo(default="")
    server: str = FieldInfo(default="")
    ca_cert: str = FieldInfo(default="")
    tls_cert: str = FieldInfo(default="")
    tls_key: str = FieldInfo(default="")
    routing_profile_ca_cert: str = FieldInfo(default="")
    routing_profile_tls_cert: str = FieldInfo(default="")
    routing_profile_tls_key: str = FieldInfo(default="")
    gateway_discovery_enabled: bool = FieldInfo(default=False)
    gateway_discovery_interval: int = FieldInfo(default=0)
    gateway_discovery_tx_frequency: int = FieldInfo(default=0)
    gateway_discovery_dr: int = FieldInfo(default=0)


class NetworkServerListItem(BaseModel):

    id: int = FieldInfo(default=0)
    name: str = FieldInfo(default="")
    server: str = FieldInfo(default="")
    created_at: datetime = FieldInfo(default_factory=datetime.now)
    updated_at: datetime = FieldInfo(default_factory=datetime.now)


class CreateNetworkServerRequest(BaseModel):

    network_server: NetworkServer = FieldInfo()


class CreateNetworkServerResponse(BaseModel):

    id: int = FieldInfo(default=0)


class GetNetworkServerRequest(BaseModel):

    id: int = FieldInfo(default=0)


class GetNetworkServerResponse(BaseModel):

    network_server: NetworkServer = FieldInfo()
    created_at: datetime = FieldInfo(default_factory=datetime.now)
    updated_at: datetime = FieldInfo(default_factory=datetime.now)
    version: str = FieldInfo(default="")
    region: str = FieldInfo(default="")


class UpdateNetworkServerRequest(BaseModel):

    network_server: NetworkServer = FieldInfo()


class DeleteNetworkServerRequest(BaseModel):

    id: int = FieldInfo(default=0)


class ListNetworkServerRequest(BaseModel):

    limit: int = FieldInfo(default=0)
    offset: int = FieldInfo(default=0)
    organization_id: int = FieldInfo(default=0)


class ListNetworkServerResponse(BaseModel):

    total_count: int = FieldInfo(default=0)
    result: typing.List[NetworkServerListItem] = FieldInfo(default_factory=list)


class GetADRAlgorithmsRequest(BaseModel):

    network_server_id: int = FieldInfo(default=0)


class GetADRAlgorithmsResponse(BaseModel):

    adr_algorithms: typing.List[ADRAlgorithm] = FieldInfo(default_factory=list)
