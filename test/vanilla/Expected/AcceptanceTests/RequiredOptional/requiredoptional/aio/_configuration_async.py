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


class AutoRestRequiredOptionalTestServiceConfiguration(Configuration):
    """Configuration for AutoRestRequiredOptionalTestService
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param required_global_path: number of items to skip
    :type required_global_path: str
    :param required_global_query: number of items to skip
    :type required_global_query: str
    :param optional_global_query: number of items to skip
    :type optional_global_query: int
    :param str base_url: Service URL
    """

    def __init__(
            self, required_global_path, required_global_query, optional_global_query=None, base_url=None):

        if required_global_path is None:
            raise ValueError("Parameter 'required_global_path' must not be None.")
        if required_global_query is None:
            raise ValueError("Parameter 'required_global_query' must not be None.")
        if not base_url:
            base_url = 'http://localhost:3000'

        super(AutoRestRequiredOptionalTestServiceConfiguration, self).__init__(base_url)
        self._configure()

        self.add_user_agent('autorestrequiredoptionaltestservice/{}'.format(VERSION))

        self.required_global_path = required_global_path
        self.required_global_query = required_global_query
        self.optional_global_query = optional_global_query

    def _configure(self):
        super(AutoRestRequiredOptionalTestServiceConfiguration, self)._configure()
        self.retry_policy = AsyncClientRetryPolicy()
        self.redirect_policy = AsyncClientRedirectPolicy()
