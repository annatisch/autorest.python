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

from ._configuration_async import AutoRestRFC1123DateTimeTestServiceConfiguration
from .operations_async import Datetimerfc1123Operations
from .. import models


class AutoRestRFC1123DateTimeTestService:
    """Test Infrastructure for AutoRest


    :ivar datetimerfc1123: Datetimerfc1123 operations
    :vartype datetimerfc1123: bodydatetimerfc1123.aio.operations_async.Datetimerfc1123Operations

    :param str base_url: Service URL
    """

    def __init__(
            self, base_url=None, config=None, **kwargs):

        self._config = config or AutoRestRFC1123DateTimeTestServiceConfiguration(**kwargs)
        super(AutoRestRFC1123DateTimeTestService, self).__init__(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.datetimerfc1123 = Datetimerfc1123Operations(
            self, self._config, self._serialize, self._deserialize)
