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

from msrest import Configuration
from msrest.universal_http import ClientRedirectPolicy, ClientRetryPolicy

from .version import VERSION


class AutoRestSwaggerBATFormDataServiceConfiguration(Configuration):
    """Configuration for AutoRestSwaggerBATFormDataService
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param str base_url: Service URL
    """

    def __init__(
            self, base_url=None):

        if not base_url:
            base_url = 'http://localhost:3000'

        super(AutoRestSwaggerBATFormDataServiceConfiguration, self).__init__(base_url)
        self._configure()

        self.add_user_agent('autorestswaggerbatformdataservice/{}'.format(VERSION))

    def _configure(self):
        super(AutoRestSwaggerBATFormDataServiceConfiguration, self)._configure()
        self.retry_policy = ClientRetryPolicy()
        self.redirect_policy = ClientRedirectPolicy()
