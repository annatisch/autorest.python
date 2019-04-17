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

from ._configuration import AutoRestParameterGroupingTestServiceConfiguration
from .operations import ParameterGroupingOperations
from . import models


class AutoRestParameterGroupingTestService(object):
    """Test Infrastructure for AutoRest


    :ivar parameter_grouping: ParameterGrouping operations
    :vartype parameter_grouping: azureparametergrouping.operations.ParameterGroupingOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None, config=None, **kwargs):

        self._config = config or AutoRestParameterGroupingTestServiceConfiguration(credentials, **kwargs)
        super(AutoRestParameterGroupingTestService, self).__init__(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.parameter_grouping = ParameterGroupingOperations(
            self, self._config, self._serialize, self._deserialize)
