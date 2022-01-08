# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import proto  # type: ignore

from google.api import auth_pb2  # type: ignore
from google.api import documentation_pb2  # type: ignore
from google.api import endpoint_pb2  # type: ignore
from google.api import monitored_resource_pb2  # type: ignore
from google.api import monitoring_pb2  # type: ignore
from google.api import quota_pb2  # type: ignore
from google.api import usage_pb2  # type: ignore
from google.protobuf import api_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.api.serviceusage.v1',
    manifest={
        'State',
        'Service',
        'ServiceConfig',
        'OperationMetadata',
    },
)


class State(proto.Enum):
    r"""Whether or not a service has been enabled for use by a
    consumer.
    """
    STATE_UNSPECIFIED = 0
    DISABLED = 1
    ENABLED = 2


class Service(proto.Message):
    r"""A service that is available for use by the consumer.

    Attributes:
        name (str):
            The resource name of the consumer and
            service.
            A valid name would be:
            -
            projects/123/services/serviceusage.googleapis.com
        parent (str):
            The resource name of the consumer.
            A valid name would be:
            - projects/123
        config (google.cloud.service_usage_v1.types.ServiceConfig):
            The service configuration of the available service. Some
            fields may be filtered out of the configuration in responses
            to the ``ListServices`` method. These fields are present
            only in responses to the ``GetService`` method.
        state (google.cloud.service_usage_v1.types.State):
            Whether or not the service has been enabled
            for use by the consumer.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    parent = proto.Field(
        proto.STRING,
        number=5,
    )
    config = proto.Field(
        proto.MESSAGE,
        number=2,
        message='ServiceConfig',
    )
    state = proto.Field(
        proto.ENUM,
        number=4,
        enum='State',
    )


class ServiceConfig(proto.Message):
    r"""The configuration of the service.

    Attributes:
        name (str):
            The DNS address at which this service is available.

            An example DNS address would be:
            ``calendar.googleapis.com``.
        title (str):
            The product title for this service.
        apis (Sequence[google.protobuf.api_pb2.Api]):
            A list of API interfaces exported by this
            service. Contains only the names, versions, and
            method names of the interfaces.
        documentation (google.api.documentation_pb2.Documentation):
            Additional API documentation. Contains only
            the summary and the documentation URL.
        quota (google.api.quota_pb2.Quota):
            Quota configuration.
        authentication (google.api.auth_pb2.Authentication):
            Auth configuration. Contains only the OAuth
            rules.
        usage (google.api.usage_pb2.Usage):
            Configuration controlling usage of this
            service.
        endpoints (Sequence[google.api.endpoint_pb2.Endpoint]):
            Configuration for network endpoints. Contains
            only the names and aliases of the endpoints.
        monitored_resources (Sequence[google.api.monitored_resource_pb2.MonitoredResourceDescriptor]):
            Defines the monitored resources used by this service. This
            is required by the
            [Service.monitoring][google.api.Service.monitoring] and
            [Service.logging][google.api.Service.logging]
            configurations.
        monitoring (google.api.monitoring_pb2.Monitoring):
            Monitoring configuration. This should not include the
            'producer_destinations' field.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    title = proto.Field(
        proto.STRING,
        number=2,
    )
    apis = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=api_pb2.Api,
    )
    documentation = proto.Field(
        proto.MESSAGE,
        number=6,
        message=documentation_pb2.Documentation,
    )
    quota = proto.Field(
        proto.MESSAGE,
        number=10,
        message=quota_pb2.Quota,
    )
    authentication = proto.Field(
        proto.MESSAGE,
        number=11,
        message=auth_pb2.Authentication,
    )
    usage = proto.Field(
        proto.MESSAGE,
        number=15,
        message=usage_pb2.Usage,
    )
    endpoints = proto.RepeatedField(
        proto.MESSAGE,
        number=18,
        message=endpoint_pb2.Endpoint,
    )
    monitored_resources = proto.RepeatedField(
        proto.MESSAGE,
        number=25,
        message=monitored_resource_pb2.MonitoredResourceDescriptor,
    )
    monitoring = proto.Field(
        proto.MESSAGE,
        number=28,
        message=monitoring_pb2.Monitoring,
    )


class OperationMetadata(proto.Message):
    r"""The operation metadata returned for the batchend services
    operation.

    Attributes:
        resource_names (Sequence[str]):
            The full name of the resources that this
            operation is directly associated with.
    """

    resource_names = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
