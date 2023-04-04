"""
Aliases for protobuffer descriptor names to pydantic model classes. This is needed because the
protobuf definitions found for chirpstack on their github repo don't match the actual chirpstack-api
python package that they offer (seems the repo is not in-sync with the latest package). To avoid
issues we keep a dict of such incompatibilities here so our package keeps working.
"""

from .models import api as pydantic_api
from chirpstack_api import api as chirpstack_api

protobuf_aliases = {"ListUsersResponse": pydantic_api.ListUserResponse}
pydantic_to_protobuf_aliases = {"ListUserResponse": chirpstack_api.ListUsersResponse}
