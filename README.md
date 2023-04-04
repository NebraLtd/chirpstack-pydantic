## Pydantic models for Chirpstack Protobufs

This repo contains pydantic models for Chripstack's gRPC API. The main aim it to facilitate API/Frontend development for projects like fastapi that primarily work with pydantic models.

The models here will be kept version compatible with the [chirpstack_api](https://pypi.org/project/chirpstack-api/). Current state of chirpstack development means that there are frequent backward incompatible changes to protobuf definitions that are not synced with their docs or github repo so using the package with the same chirpstack_api version is recommended.


