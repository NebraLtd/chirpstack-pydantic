# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)
# type: ignore

from datetime import datetime
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from chirpstack_pydantic.base import BaseModel
from pydantic.fields import FieldInfo
import typing


class MulticastGroupType(IntEnum):
    CLASS_C = 0
    CLASS_B = 1


class MulticastGroup(BaseModel):

    id: str = FieldInfo(default="")
    name: str = FieldInfo(default="")
    mc_addr: str = FieldInfo(default="")
    mc_nwk_s_key: str = FieldInfo(default="")
    mc_app_s_key: str = FieldInfo(default="")
    f_cnt: int = FieldInfo(default=0)
    group_type: MulticastGroupType = FieldInfo(default=0)
    dr: int = FieldInfo(default=0)
    frequency: int = FieldInfo(default=0)
    ping_slot_period: int = FieldInfo(default=0)
    application_id: int = FieldInfo(default=0)


class MulticastGroupListItem(BaseModel):

    id: str = FieldInfo(default="")
    name: str = FieldInfo(default="")
    application_id: int = FieldInfo(default=0)
    application_name: str = FieldInfo(default="")


class CreateMulticastGroupRequest(BaseModel):

    multicast_group: MulticastGroup = FieldInfo()


class CreateMulticastGroupResponse(BaseModel):

    id: str = FieldInfo(default="")


class GetMulticastGroupRequest(BaseModel):

    id: str = FieldInfo(default="")


class GetMulticastGroupResponse(BaseModel):

    multicast_group: MulticastGroup = FieldInfo()
    created_at: datetime = FieldInfo(default_factory=datetime.now)
    updated_at: datetime = FieldInfo(default_factory=datetime.now)


class UpdateMulticastGroupRequest(BaseModel):

    multicast_group: MulticastGroup = FieldInfo()


class DeleteMulticastGroupRequest(BaseModel):

    id: str = FieldInfo(default="")


class AddDeviceToMulticastGroupRequest(BaseModel):

    multicast_group_id: str = FieldInfo(default="")
    dev_eui: str = FieldInfo(default="")


class RemoveDeviceFromMulticastGroupRequest(BaseModel):

    multicast_group_id: str = FieldInfo(default="")
    dev_eui: str = FieldInfo(default="")


class ListMulticastGroupRequest(BaseModel):

    limit: int = FieldInfo(default=0)
    offset: int = FieldInfo(default=0)
    organization_id: int = FieldInfo(default=0)
    dev_eui: str = FieldInfo(default="")
    search: str = FieldInfo(default="")
    application_id: int = FieldInfo(default=0)


class ListMulticastGroupResponse(BaseModel):

    total_count: int = FieldInfo(default=0)
    result: typing.List[MulticastGroupListItem] = FieldInfo(default_factory=list)


class MulticastQueueItem(BaseModel):

    multicast_group_id: str = FieldInfo(default="")
    f_cnt: int = FieldInfo(default=0)
    f_port: int = FieldInfo(default=0)
    data: bytes = FieldInfo(default=b"")


class EnqueueMulticastQueueItemRequest(BaseModel):

    multicast_queue_item: MulticastQueueItem = FieldInfo()


class EnqueueMulticastQueueItemResponse(BaseModel):

    f_cnt: int = FieldInfo(default=0)


class FlushMulticastGroupQueueItemsRequest(BaseModel):

    multicast_group_id: str = FieldInfo(default="")


class ListMulticastGroupQueueItemsRequest(BaseModel):

    multicast_group_id: str = FieldInfo(default="")


class ListMulticastGroupQueueItemsResponse(BaseModel):

    multicast_queue_items: typing.List[MulticastQueueItem] = FieldInfo(
        default_factory=list
    )
