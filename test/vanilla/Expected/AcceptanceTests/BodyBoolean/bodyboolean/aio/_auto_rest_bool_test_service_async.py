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

from ._configuration_async import AutoRestBoolTestServiceConfiguration
from .operations_async import BoolModelOperations
from .. import models


class AutoRestBoolTestService(SDKClientAsync):
    """Test Infrastructure for AutoRest

    :ivar config: Configuration for client.
    :vartype config: AutoRestBoolTestServiceConfiguration

    :ivar bool_model: BoolModel operations
    :vartype bool_model: bodyboolean.aio.operations_async.BoolModelOperations

    :param str base_url: Service URL
    """

    def __init__(
            self, base_url=None, config=None, pipeline=None):

        self.config = config or AutoRestBoolTestServiceConfiguration(base_url)
        super(AutoRestBoolTestService, self).__init__(None, self.config, pipeline=pipeline)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.bool_model = BoolModelOperations(
            self._client, self.config, self._serialize, self._deserialize)
