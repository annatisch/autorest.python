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

from msrest.async_client import SDKClientAsync
from msrest import Serializer, Deserializer

from ._configuration_async import AutoRestPagingTestServiceConfiguration
from .operations_async import PagingOperations
from .. import models


class AutoRestPagingTestService(SDKClientAsync):
    """Long-running Operation for AutoRest

    :ivar config: Configuration for client.
    :vartype config: AutoRestPagingTestServiceConfiguration

    :ivar paging: Paging operations
    :vartype paging: paging.operations.PagingOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        self.config = AutoRestPagingTestServiceConfiguration(credentials, base_url)
        super(AutoRestPagingTestService, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.paging = PagingOperations(
            self._client, self.config, self._serialize, self._deserialize)
