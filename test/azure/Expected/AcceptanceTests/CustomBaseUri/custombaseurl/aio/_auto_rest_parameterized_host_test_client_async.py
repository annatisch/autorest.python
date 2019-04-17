# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.core import PipelineClient
from msrest import Serializer, Deserializer

from ._configuration_async import AutoRestParameterizedHostTestClientConfiguration
from .operations_async import PathsOperations
from .. import models


class AutoRestParameterizedHostTestClient:
    """Test Infrastructure for AutoRest


    :ivar paths: Paths operations
    :vartype paths: custombaseurl.operations.PathsOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param host: A string value that is used as a global part of the
     parameterized host
    :type host: str
    """

    def __init__(
            self, credentials, host, config=None, **kwargs):

        self._config = config or AutoRestParameterizedHostTestClientConfiguration(credentials, host, **kwargs)
        super(AutoRestParameterizedHostTestClient, self).__init__(base_url=None, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.paths = PathsOperations(
            self, self._config, self._serialize, self._deserialize)
