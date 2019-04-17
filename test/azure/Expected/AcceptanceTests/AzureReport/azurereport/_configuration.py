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
from azure.core.configuration import Configuration, ConnectionConfiguration
from azure.core.pipeline import policies

from .version import VERSION


class AutoRestReportServiceForAzureConfiguration(Configuration):
    """Configuration for AutoRestReportServiceForAzure
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    """

    def __init__(self, credentials, **kwargs):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")

        super(AutoRestReportServiceForAzureConfiguration, self).__init__(**kwargs)
        self._configure(**kwargs)

        self.user_agent_policy.add_user_agent('autorestreportserviceforazure/{}'.format(VERSION))
        self.user_agent_policy.add_user_agent('Azure-SDK-For-Python')
        self.generate_client_request_id = True
        self.accept_language = None

        self.credentials = credentials

    def _configure(self, **kwargs):
        self.connection = ConnectionConfiguration(**kwargs)
        self.user_agent_policy = policies.UserAgentPolicy(**kwargs)
        self.headers_policy = policies.HeadersPolicy(**kwargs)
        self.proxy_policy = policies.ProxyPolicy(**kwargs)
        self.logging_policy = policies.NetworkTraceLoggingPolicy(**kwargs)
        self.retry_policy = policies.RetryPolicy(**kwargs)
        self.redirect_policy = policies.RedirectPolicy(**kwargs)
