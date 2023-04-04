# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)
# type: ignore

from google.protobuf.message import Message  # type: ignore
from chirpstack_pydantic.base import BaseModel
from pydantic.fields import FieldInfo
import typing


class DeviceQueueItem(BaseModel):

    dev_eui: str = FieldInfo(default="")
    confirmed: bool = FieldInfo(default=False)
    f_cnt: int = FieldInfo(default=0)
    f_port: int = FieldInfo(default=0)
    data: bytes = FieldInfo(default=b"")
    json_object: str = FieldInfo(default="")


class EnqueueDeviceQueueItemRequest(BaseModel):

    device_queue_item: DeviceQueueItem = FieldInfo()


class EnqueueDeviceQueueItemResponse(BaseModel):

    f_cnt: int = FieldInfo(default=0)


class FlushDeviceQueueRequest(BaseModel):

    dev_eui: str = FieldInfo(default="")


class ListDeviceQueueItemsRequest(BaseModel):

    dev_eui: str = FieldInfo(default="")
    count_only: bool = FieldInfo(default=False)


class ListDeviceQueueItemsResponse(BaseModel):

    device_queue_items: typing.List[DeviceQueueItem] = FieldInfo(default_factory=list)
    total_count: int = FieldInfo(default=0)
