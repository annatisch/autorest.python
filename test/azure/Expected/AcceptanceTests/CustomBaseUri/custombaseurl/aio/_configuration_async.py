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
from msrestazure import AzureConfiguration
from msrest.universal_http import AsyncClientRedirectPolicy, AsyncClientRetryPolicy

from ..version import VERSION


class AutoRestParameterizedHostTestClientConfiguration(AzureConfiguration):
    """Configuration for AutoRestParameterizedHostTestClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param host: A string value that is used as a global part of the
     parameterized host
    :type host: str
    """

    def __init__(
            self, credentials, host):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if host is None:
            raise ValueError("Parameter 'host' must not be None.")
        base_url = 'http://{accountName}{host}'

        super(AutoRestParameterizedHostTestClientConfiguration, self).__init__(base_url)
        self._configure()

        self.add_user_agent('autorestparameterizedhosttestclient/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.host = host

    def _configure(self):
        super(AutoRestParameterizedHostTestClientConfiguration, self)._configure()
        self.retry_policy = AsyncClientRetryPolicy()
        self.redirect_policy = AsyncClientRedirectPolicy()
