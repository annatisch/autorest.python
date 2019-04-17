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

from ._configuration_async import AutoRestLongRunningOperationTestServiceConfiguration
from .operations_async import LROsOperations
from .operations_async import LRORetrysOperations
from .operations_async import LROSADsOperations
from .operations_async import LROsCustomHeaderOperations
from .. import models


class AutoRestLongRunningOperationTestService:
    """Long-running Operation for AutoRest


    :ivar lr_os: LROs operations
    :vartype lr_os: lro.operations.LROsOperations
    :ivar lro_retrys: LRORetrys operations
    :vartype lro_retrys: lro.operations.LRORetrysOperations
    :ivar lrosa_ds: LROSADs operations
    :vartype lrosa_ds: lro.operations.LROSADsOperations
    :ivar lr_os_custom_header: LROsCustomHeader operations
    :vartype lr_os_custom_header: lro.operations.LROsCustomHeaderOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None, config=None, **kwargs):

        self._config = config or AutoRestLongRunningOperationTestServiceConfiguration(credentials, **kwargs)
        super(AutoRestLongRunningOperationTestService, self).__init__(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.lr_os = LROsOperations(
            self, self._config, self._serialize, self._deserialize)
        self.lro_retrys = LRORetrysOperations(
            self, self._config, self._serialize, self._deserialize)
        self.lrosa_ds = LROSADsOperations(
            self, self._config, self._serialize, self._deserialize)
        self.lr_os_custom_header = LROsCustomHeaderOperations(
            self, self._config, self._serialize, self._deserialize)
