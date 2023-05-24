# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)
# type: ignore

from datetime import datetime
from datetime import timedelta
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from chirpstack_pydantic.util import Timedelta
from chirpstack_pydantic.base import BaseModel
from pydantic.fields import FieldInfo
import typing


class MulticastGroupType(IntEnum):
    CLASS_B = 0
    CLASS_C = 1


class RequestFragmentationSessionStatus(IntEnum):
    AFTER_FRAGMENT_ENQUEUE = 0
    AFTER_SESSION_TIMEOUT = 1
    NO_REQUEST = 2


class DeploymentDevice(BaseModel):

    dev_eui: bytes = FieldInfo(default=b"")
    mc_root_key: bytes = FieldInfo(default=b"")


class Deployment(BaseModel):

    application_id: int = FieldInfo(default=0)
    devices: typing.List[DeploymentDevice] = FieldInfo(default_factory=list)
    multicast_group_type: MulticastGroupType = FieldInfo(default=0)
    multicast_dr: int = FieldInfo(default=0)
    multicast_ping_slot_period: int = FieldInfo(default=0)
    multicast_frequency: int = FieldInfo(default=0)
    multicast_group_id: int = FieldInfo(default=0)
    multicast_timeout: int = FieldInfo(default=0)
    unicast_timeout: Timedelta = FieldInfo(default_factory=timedelta)
    unicast_attempt_count: int = FieldInfo(default=0)
    fragmentation_fragment_size: int = FieldInfo(default=0)
    payload: bytes = FieldInfo(default=b"")
    fragmentation_redundancy: int = FieldInfo(default=0)
    fragmentation_session_index: int = FieldInfo(default=0)
    fragmentation_matrix: int = FieldInfo(default=0)
    fragmentation_block_ack_delay: int = FieldInfo(default=0)
    fragmentation_descriptor: bytes = FieldInfo(default=b"")
    request_fragmentation_session_status: RequestFragmentationSessionStatus = FieldInfo(
        default=0
    )


class CreateDeploymentRequest(BaseModel):

    deployment: Deployment = FieldInfo()


class CreateDeploymentResponse(BaseModel):

    id: bytes = FieldInfo(default=b"")


class GetDeploymentStatusRequest(BaseModel):

    id: bytes = FieldInfo(default=b"")


class DeploymentDeviceStatus(BaseModel):

    dev_eui: bytes = FieldInfo(default=b"")
    created_at: datetime = FieldInfo(default_factory=datetime.now)
    updated_at: datetime = FieldInfo(default_factory=datetime.now)
    mc_group_setup_completed_at: datetime = FieldInfo(default_factory=datetime.now)
    mc_session_completed_at: datetime = FieldInfo(default_factory=datetime.now)
    frag_session_setup_completed_at: datetime = FieldInfo(default_factory=datetime.now)
    frag_status_completed_at: datetime = FieldInfo(default_factory=datetime.now)


class GetDeploymentStatusResponse(BaseModel):

    created_at: datetime = FieldInfo(default_factory=datetime.now)
    updated_at: datetime = FieldInfo(default_factory=datetime.now)
    mc_group_setup_completed_at: datetime = FieldInfo(default_factory=datetime.now)
    mc_session_completed_at: datetime = FieldInfo(default_factory=datetime.now)
    frag_session_setup_completed_at: datetime = FieldInfo(default_factory=datetime.now)
    enqueue_completed_at: datetime = FieldInfo(default_factory=datetime.now)
    frag_status_completed_at: datetime = FieldInfo(default_factory=datetime.now)
    device_status: typing.List[DeploymentDeviceStatus] = FieldInfo(default_factory=list)


class GetDeploymentDeviceLogsRequest(BaseModel):

    deployment_id: bytes = FieldInfo(default=b"")
    dev_eui: bytes = FieldInfo(default=b"")


class DeploymentDeviceLog(BaseModel):

    created_at: datetime = FieldInfo(default_factory=datetime.now)
    f_port: int = FieldInfo(default=0)
    command: str = FieldInfo(default="")
    fields: typing.Dict[str, str] = FieldInfo(default_factory=dict)


class GetDeploymentDeviceLogsResponse(BaseModel):

    logs: typing.List[DeploymentDeviceLog] = FieldInfo(default_factory=list)
