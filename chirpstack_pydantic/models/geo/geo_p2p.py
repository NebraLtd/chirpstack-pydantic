# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)
# type: ignore

from ..common.common_p2p import Location
from ..gw.gw_p2p import UplinkRXInfo
from google.protobuf.message import Message  # type: ignore
from chirpstack_pydantic.base import BaseModel
from pydantic.fields import FieldInfo
import typing


class ResolveResult(BaseModel):

    location: Location = FieldInfo()


class FrameRXInfo(BaseModel):

    rx_info: typing.List[UplinkRXInfo] = FieldInfo(default_factory=list)


class ResolveTDOARequest(BaseModel):

    dev_eui: bytes = FieldInfo(default=b"")
    frame_rx_info: FrameRXInfo = FieldInfo()
    device_reference_altitude: float = FieldInfo(default=0.0)


class ResolveMultiFrameTDOARequest(BaseModel):

    dev_eui: bytes = FieldInfo(default=b"")
    frame_rx_info_set: typing.List[FrameRXInfo] = FieldInfo(default_factory=list)
    device_reference_altitude: float = FieldInfo(default=0.0)


class ResolveTDOAResponse(BaseModel):

    result: ResolveResult = FieldInfo()


class ResolveMultiFrameTDOAResponse(BaseModel):

    result: ResolveResult = FieldInfo()
