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

from ._configuration import AutoRestSwaggerBATServiceConfiguration
from .operations import StringOperations
from .operations import EnumOperations
from . import models


class AutoRestSwaggerBATService(object):
    """Test Infrastructure for AutoRest Swagger BAT


    :ivar string: String operations
    :vartype string: bodystring.operations.StringOperations
    :ivar enum: Enum operations
    :vartype enum: bodystring.operations.EnumOperations

    :param str base_url: Service URL
    """

    def __init__(self, base_url=None, config=None, **kwargs):

        self._config = config or AutoRestSwaggerBATServiceConfiguration(**kwargs)
        super(AutoRestSwaggerBATService, self).__init__(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.string = StringOperations(
            self, self._config, self._serialize, self._deserialize)
        self.enum = EnumOperations(
            self, self._config, self._serialize, self._deserialize)
