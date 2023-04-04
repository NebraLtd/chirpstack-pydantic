# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic(https://github.com/so1n/protobuf_to_pydantic)
# type: ignore

from datetime import datetime
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from chirpstack_pydantic.base import BaseModel
from pydantic.fields import FieldInfo
import typing


class IntegrationKind(IntEnum):
    HTTP = 0
    INFLUXDB = 1
    THINGSBOARD = 2
    MYDEVICES = 3
    LORACLOUD = 4
    GCP_PUBSUB = 5
    AWS_SNS = 6
    AZURE_SERVICE_BUS = 7
    PILOT_THINGS = 8
    MQTT_GLOBAL = 9


class Marshaler(IntEnum):
    JSON = 0
    PROTOBUF = 1
    JSON_V3 = 2


class InfluxDBPrecision(IntEnum):
    NS = 0
    U = 1
    MS = 2
    S = 3
    M = 4
    H = 5


class InfluxDBVersion(IntEnum):
    INFLUXDB_1 = 0
    INFLUXDB_2 = 1


class Application(BaseModel):

    id: int = FieldInfo(default=0)
    name: str = FieldInfo(default="")
    description: str = FieldInfo(default="")
    organization_id: int = FieldInfo(default=0)
    service_profile_id: str = FieldInfo(default="")
    payload_codec: str = FieldInfo(default="")
    payload_encoder_script: str = FieldInfo(default="")
    payload_decoder_script: str = FieldInfo(default="")


class ApplicationListItem(BaseModel):

    id: int = FieldInfo(default=0)
    name: str = FieldInfo(default="")
    description: str = FieldInfo(default="")
    organization_id: int = FieldInfo(default=0)
    service_profile_id: str = FieldInfo(default="")
    service_profile_name: str = FieldInfo(default="")


class CreateApplicationRequest(BaseModel):

    application: Application = FieldInfo()


class CreateApplicationResponse(BaseModel):

    id: int = FieldInfo(default=0)


class GetApplicationRequest(BaseModel):

    id: int = FieldInfo(default=0)


class GetApplicationResponse(BaseModel):

    application: Application = FieldInfo()


class UpdateApplicationRequest(BaseModel):

    application: Application = FieldInfo()


class DeleteApplicationRequest(BaseModel):

    id: int = FieldInfo(default=0)


class ListApplicationRequest(BaseModel):

    limit: int = FieldInfo(default=0)
    offset: int = FieldInfo(default=0)
    organization_id: int = FieldInfo(default=0)
    search: str = FieldInfo(default="")


class ListApplicationResponse(BaseModel):

    total_count: int = FieldInfo(default=0)
    result: typing.List[ApplicationListItem] = FieldInfo(default_factory=list)


class HTTPIntegrationHeader(BaseModel):

    key: str = FieldInfo(default="")
    value: str = FieldInfo(default="")


class HTTPIntegration(BaseModel):

    application_id: int = FieldInfo(default=0)
    headers: typing.List[HTTPIntegrationHeader] = FieldInfo(default_factory=list)
    uplink_data_url: str = FieldInfo(default="")
    join_notification_url: str = FieldInfo(default="")
    ack_notification_url: str = FieldInfo(default="")
    error_notification_url: str = FieldInfo(default="")
    status_notification_url: str = FieldInfo(default="")
    location_notification_url: str = FieldInfo(default="")
    tx_ack_notification_url: str = FieldInfo(default="")
    integration_notification_url: str = FieldInfo(default="")
    marshaler: Marshaler = FieldInfo(default=0)
    event_endpoint_url: str = FieldInfo(default="")


class CreateHTTPIntegrationRequest(BaseModel):

    integration: HTTPIntegration = FieldInfo()


class GetHTTPIntegrationRequest(BaseModel):

    application_id: int = FieldInfo(default=0)


class GetHTTPIntegrationResponse(BaseModel):

    integration: HTTPIntegration = FieldInfo()


class UpdateHTTPIntegrationRequest(BaseModel):

    integration: HTTPIntegration = FieldInfo()


class DeleteHTTPIntegrationRequest(BaseModel):

    application_id: int = FieldInfo(default=0)


class ListIntegrationRequest(BaseModel):

    application_id: int = FieldInfo(default=0)


class IntegrationListItem(BaseModel):

    kind: IntegrationKind = FieldInfo(default=0)


class ListIntegrationResponse(BaseModel):

    total_count: int = FieldInfo(default=0)
    result: typing.List[IntegrationListItem] = FieldInfo(default_factory=list)


class InfluxDBIntegration(BaseModel):

    application_id: int = FieldInfo(default=0)
    endpoint: str = FieldInfo(default="")
    db: str = FieldInfo(default="")
    username: str = FieldInfo(default="")
    password: str = FieldInfo(default="")
    retention_policy_name: str = FieldInfo(default="")
    precision: InfluxDBPrecision = FieldInfo(default=0)
    version: InfluxDBVersion = FieldInfo(default=0)
    token: str = FieldInfo(default="")
    organization: str = FieldInfo(default="")
    bucket: str = FieldInfo(default="")


class CreateInfluxDBIntegrationRequest(BaseModel):

    integration: InfluxDBIntegration = FieldInfo()


class GetInfluxDBIntegrationRequest(BaseModel):

    application_id: int = FieldInfo(default=0)


class GetInfluxDBIntegrationResponse(BaseModel):

    integration: InfluxDBIntegration = FieldInfo()


class UpdateInfluxDBIntegrationRequest(BaseModel):

    integration: InfluxDBIntegration = FieldInfo()


class DeleteInfluxDBIntegrationRequest(BaseModel):

    application_id: int = FieldInfo(default=0)


class ThingsBoardIntegration(BaseModel):

    application_id: int = FieldInfo(default=0)
    server: str = FieldInfo(default="")


class CreateThingsBoardIntegrationRequest(BaseModel):

    integration: ThingsBoardIntegration = FieldInfo()


class GetThingsBoardIntegrationRequest(BaseModel):

    application_id: int = FieldInfo(default=0)


class GetThingsBoardIntegrationResponse(BaseModel):

    integration: ThingsBoardIntegration = FieldInfo()


class UpdateThingsBoardIntegrationRequest(BaseModel):

    integration: ThingsBoardIntegration = FieldInfo()


class DeleteThingsBoardIntegrationRequest(BaseModel):

    application_id: int = FieldInfo(default=0)


class MyDevicesIntegration(BaseModel):

    application_id: int = FieldInfo(default=0)
    endpoint: str = FieldInfo(default="")


class CreateMyDevicesIntegrationRequest(BaseModel):

    integration: MyDevicesIntegration = FieldInfo()


class GetMyDevicesIntegrationRequest(BaseModel):

    application_id: int = FieldInfo(default=0)


class GetMyDevicesIntegrationResponse(BaseModel):

    integration: MyDevicesIntegration = FieldInfo()


class UpdateMyDevicesIntegrationRequest(BaseModel):

    integration: MyDevicesIntegration = FieldInfo()


class DeleteMyDevicesIntegrationRequest(BaseModel):

    application_id: int = FieldInfo(default=0)


class LoRaCloudIntegration(BaseModel):

    application_id: int = FieldInfo(default=0)
    geolocation: bool = FieldInfo(default=False)
    geolocation_token: str = FieldInfo(default="")
    geolocation_buffer_ttl: int = FieldInfo(default=0)
    geolocation_min_buffer_size: int = FieldInfo(default=0)
    geolocation_tdoa: bool = FieldInfo(default=False)
    geolocation_rssi: bool = FieldInfo(default=False)
    geolocation_gnss: bool = FieldInfo(default=False)
    geolocation_gnss_payload_field: str = FieldInfo(default="")
    geolocation_gnss_use_rx_time: bool = FieldInfo(default=False)
    geolocation_wifi: bool = FieldInfo(default=False)
    geolocation_wifi_payload_field: str = FieldInfo(default="")
    das: bool = FieldInfo(default=False)
    das_token: str = FieldInfo(default="")
    das_modem_port: int = FieldInfo(default=0)
    das_gnss_port: int = FieldInfo(default=0)
    das_gnss_use_rx_time: bool = FieldInfo(default=False)
    das_streaming_geoloc_workaround: bool = FieldInfo(default=False)


class CreateLoRaCloudIntegrationRequest(BaseModel):

    integration: LoRaCloudIntegration = FieldInfo()


class GetLoRaCloudIntegrationRequest(BaseModel):

    application_id: int = FieldInfo(default=0)


class GetLoRaCloudIntegrationResponse(BaseModel):

    integration: LoRaCloudIntegration = FieldInfo()


class UpdateLoRaCloudIntegrationRequest(BaseModel):

    integration: LoRaCloudIntegration = FieldInfo()


class DeleteLoRaCloudIntegrationRequest(BaseModel):

    application_id: int = FieldInfo(default=0)


class GCPPubSubIntegration(BaseModel):

    application_id: int = FieldInfo(default=0)
    marshaler: Marshaler = FieldInfo(default=0)
    credentials_file: str = FieldInfo(default="")
    project_id: str = FieldInfo(default="")
    topic_name: str = FieldInfo(default="")


class CreateGCPPubSubIntegrationRequest(BaseModel):

    integration: GCPPubSubIntegration = FieldInfo()


class GetGCPPubSubIntegrationRequest(BaseModel):

    application_id: int = FieldInfo(default=0)


class GetGCPPubSubIntegrationResponse(BaseModel):

    integration: GCPPubSubIntegration = FieldInfo()


class UpdateGCPPubSubIntegrationRequest(BaseModel):

    integration: GCPPubSubIntegration = FieldInfo()


class DeleteGCPPubSubIntegrationRequest(BaseModel):

    application_id: int = FieldInfo(default=0)


class AWSSNSIntegration(BaseModel):

    application_id: int = FieldInfo(default=0)
    marshaler: Marshaler = FieldInfo(default=0)
    region: str = FieldInfo(default="")
    access_key_id: str = FieldInfo(default="")
    secret_access_key: str = FieldInfo(default="")
    topic_arn: str = FieldInfo(default="")


class CreateAWSSNSIntegrationRequest(BaseModel):

    integration: AWSSNSIntegration = FieldInfo()


class GetAWSSNSIntegrationRequest(BaseModel):

    application_id: int = FieldInfo(default=0)


class GetAWSSNSIntegrationResponse(BaseModel):

    integration: AWSSNSIntegration = FieldInfo()


class UpdateAWSSNSIntegrationRequest(BaseModel):

    integration: AWSSNSIntegration = FieldInfo()


class DeleteAWSSNSIntegrationRequest(BaseModel):

    application_id: int = FieldInfo(default=0)


class AzureServiceBusIntegration(BaseModel):

    application_id: int = FieldInfo(default=0)
    marshaler: Marshaler = FieldInfo(default=0)
    connection_string: str = FieldInfo(default="")
    publish_name: str = FieldInfo(default="")


class CreateAzureServiceBusIntegrationRequest(BaseModel):

    integration: AzureServiceBusIntegration = FieldInfo()


class GetAzureServiceBusIntegrationRequest(BaseModel):

    application_id: int = FieldInfo(default=0)


class GetAzureServiceBusIntegrationResponse(BaseModel):

    integration: AzureServiceBusIntegration = FieldInfo()


class UpdateAzureServiceBusIntegrationRequest(BaseModel):

    integration: AzureServiceBusIntegration = FieldInfo()


class DeleteAzureServiceBusIntegrationRequest(BaseModel):

    application_id: int = FieldInfo(default=0)


class PilotThingsIntegration(BaseModel):

    application_id: int = FieldInfo(default=0)
    server: str = FieldInfo(default="")
    token: str = FieldInfo(default="")


class CreatePilotThingsIntegrationRequest(BaseModel):

    integration: PilotThingsIntegration = FieldInfo()


class GetPilotThingsIntegrationRequest(BaseModel):

    application_id: int = FieldInfo(default=0)


class GetPilotThingsIntegrationResponse(BaseModel):

    integration: PilotThingsIntegration = FieldInfo()


class UpdatePilotThingsIntegrationRequest(BaseModel):

    integration: PilotThingsIntegration = FieldInfo()


class DeletePilotThingsIntegrationRequest(BaseModel):

    application_id: int = FieldInfo(default=0)


class GenerateMQTTIntegrationClientCertificateRequest(BaseModel):

    application_id: int = FieldInfo(default=0)


class GenerateMQTTIntegrationClientCertificateResponse(BaseModel):

    tls_cert: str = FieldInfo(default="")
    tls_key: str = FieldInfo(default="")
    ca_cert: str = FieldInfo(default="")
    expires_at: datetime = FieldInfo(default_factory=datetime.now)
