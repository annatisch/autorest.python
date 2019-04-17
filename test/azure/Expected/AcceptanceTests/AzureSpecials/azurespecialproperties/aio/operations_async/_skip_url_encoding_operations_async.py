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

import uuid
from msrest.pipeline import ClientRawResponse

from ... import models


class SkipUrlEncodingOperations:
    """SkipUrlEncodingOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar unencoded_path_param: An unencoded path parameter with value 'path1/path2/path3'. Constant value: "path1/path2/path3".
    :ivar q1: An unencoded query parameter with value 'value1&q2=value2&q3=value3'. Constant value: "value1&q2=value2&q3=value3".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.unencoded_path_param = "path1/path2/path3"
        self.q1 = "value1&q2=value2&q3=value3"

        self.config = config

    async def get_method_path_valid(
            self, unencoded_path_param, *, raw=False, **kwargs):
        """Get method with unencoded path parameter with value
        'path1/path2/path3'.

        :param unencoded_path_param: Unencoded path parameter with value
         'path1/path2/path3'
        :type unencoded_path_param: str
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<azurespecialproperties.models.ErrorException>`
        """
        # Construct URL
        url = self.get_method_path_valid.metadata['url']
        path_format_arguments = {
            'unencodedPathParam': self._serialize.url("unencoded_path_param", unencoded_path_param, 'str', skip_quote=True)
        }
        url = self.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct and send request
        request = self.get(url, query_parameters, header_parameters)
        pipeline_response = await self.pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    get_method_path_valid.metadata = {'url': '/azurespecials/skipUrlEncoding/method/path/valid/{unencodedPathParam}'}

    async def get_path_path_valid(
            self, unencoded_path_param, *, raw=False, **kwargs):
        """Get method with unencoded path parameter with value
        'path1/path2/path3'.

        :param unencoded_path_param: Unencoded path parameter with value
         'path1/path2/path3'
        :type unencoded_path_param: str
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<azurespecialproperties.models.ErrorException>`
        """
        # Construct URL
        url = self.get_path_path_valid.metadata['url']
        path_format_arguments = {
            'unencodedPathParam': self._serialize.url("unencoded_path_param", unencoded_path_param, 'str', skip_quote=True)
        }
        url = self.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct and send request
        request = self.get(url, query_parameters, header_parameters)
        pipeline_response = await self.pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    get_path_path_valid.metadata = {'url': '/azurespecials/skipUrlEncoding/path/path/valid/{unencodedPathParam}'}

    async def get_swagger_path_valid(
            self, *, raw=False, **kwargs):
        """Get method with unencoded path parameter with value
        'path1/path2/path3'.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<azurespecialproperties.models.ErrorException>`
        """
        # Construct URL
        url = self.get_swagger_path_valid.metadata['url']
        path_format_arguments = {
            'unencodedPathParam': self._serialize.url("self.unencoded_path_param", self.unencoded_path_param, 'str', skip_quote=True)
        }
        url = self.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct and send request
        request = self.get(url, query_parameters, header_parameters)
        pipeline_response = await self.pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    get_swagger_path_valid.metadata = {'url': '/azurespecials/skipUrlEncoding/swagger/path/valid/{unencodedPathParam}'}

    async def get_method_query_valid(
            self, q1, *, raw=False, **kwargs):
        """Get method with unencoded query parameter with value
        'value1&q2=value2&q3=value3'.

        :param q1: Unencoded query parameter with value
         'value1&q2=value2&q3=value3'
        :type q1: str
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<azurespecialproperties.models.ErrorException>`
        """
        # Construct URL
        url = self.get_method_query_valid.metadata['url']

        # Construct parameters
        query_parameters = {}
        query_parameters['q1'] = self._serialize.query("q1", q1, 'str', skip_quote=True)

        # Construct headers
        header_parameters = {}
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct and send request
        request = self.get(url, query_parameters, header_parameters)
        pipeline_response = await self.pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    get_method_query_valid.metadata = {'url': '/azurespecials/skipUrlEncoding/method/query/valid'}

    async def get_method_query_null(
            self, q1=None, *, raw=False, **kwargs):
        """Get method with unencoded query parameter with value null.

        :param q1: Unencoded query parameter with value null
        :type q1: str
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<azurespecialproperties.models.ErrorException>`
        """
        # Construct URL
        url = self.get_method_query_null.metadata['url']

        # Construct parameters
        query_parameters = {}
        if q1 is not None:
            query_parameters['q1'] = self._serialize.query("q1", q1, 'str', skip_quote=True)

        # Construct headers
        header_parameters = {}
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct and send request
        request = self.get(url, query_parameters, header_parameters)
        pipeline_response = await self.pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    get_method_query_null.metadata = {'url': '/azurespecials/skipUrlEncoding/method/query/null'}

    async def get_path_query_valid(
            self, q1, *, raw=False, **kwargs):
        """Get method with unencoded query parameter with value
        'value1&q2=value2&q3=value3'.

        :param q1: Unencoded query parameter with value
         'value1&q2=value2&q3=value3'
        :type q1: str
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<azurespecialproperties.models.ErrorException>`
        """
        # Construct URL
        url = self.get_path_query_valid.metadata['url']

        # Construct parameters
        query_parameters = {}
        query_parameters['q1'] = self._serialize.query("q1", q1, 'str', skip_quote=True)

        # Construct headers
        header_parameters = {}
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct and send request
        request = self.get(url, query_parameters, header_parameters)
        pipeline_response = await self.pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    get_path_query_valid.metadata = {'url': '/azurespecials/skipUrlEncoding/path/query/valid'}

    async def get_swagger_query_valid(
            self, *, raw=False, **kwargs):
        """Get method with unencoded query parameter with value
        'value1&q2=value2&q3=value3'.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<azurespecialproperties.models.ErrorException>`
        """
        # Construct URL
        url = self.get_swagger_query_valid.metadata['url']

        # Construct parameters
        query_parameters = {}
        query_parameters['q1'] = self._serialize.query("self.q1", self.q1, 'str', skip_quote=True)

        # Construct headers
        header_parameters = {}
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct and send request
        request = self.get(url, query_parameters, header_parameters)
        pipeline_response = await self.pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    get_swagger_query_valid.metadata = {'url': '/azurespecials/skipUrlEncoding/swagger/query/valid'}
