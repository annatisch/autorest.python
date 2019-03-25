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
from msrest.universal_http import AsyncClientRedirectPolicy, AsyncClientRetryPolicy

from ..version import VERSION


class AutoRestUrlMutliCollectionFormatTestServiceConfiguration(Configuration):
    """Configuration for AutoRestUrlMutliCollectionFormatTestService
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param str base_url: Service URL
    """

    def __init__(
            self, base_url=None):

        if not base_url:
            base_url = 'http://localhost:3000'

        super(AutoRestUrlMutliCollectionFormatTestServiceConfiguration, self).__init__(base_url)
        self._configure()

        self.add_user_agent('autoresturlmutlicollectionformattestservice/{}'.format(VERSION))

    def _configure(self):
        super(AutoRestUrlMutliCollectionFormatTestServiceConfiguration, self)._configure()
        self.retry_policy = AsyncClientRetryPolicy()
        self.redirect_policy = AsyncClientRedirectPolicy()
