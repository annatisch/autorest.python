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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import AutoRestResourceFlatteningTestServiceConfiguration
from .operations import AutoRestResourceFlatteningTestServiceOperationsMixin
from . import models


class AutoRestResourceFlatteningTestService(AutoRestResourceFlatteningTestServiceOperationsMixin, SDKClient):
    """Resource Flattening for AutoRest

    :ivar config: Configuration for client.
    :vartype config: AutoRestResourceFlatteningTestServiceConfiguration

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None, config=None, pipeline=None):

        self.config = config or AutoRestResourceFlatteningTestServiceConfiguration(credentials, base_url)
        super(AutoRestResourceFlatteningTestService, self).__init__(self.config.credentials, self.config, pipeline=pipeline)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

