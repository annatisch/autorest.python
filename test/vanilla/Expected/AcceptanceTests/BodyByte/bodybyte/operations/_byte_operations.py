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

from msrest.pipeline import ClientRawResponse

from .. import models


class ByteOperations(object):
    """ByteOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def get_null(
            self, raw=False, **kwargs):
        """Get null byte value.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: bytearray or ClientRawResponse if raw=true
        :rtype: bytearray or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodybyte.models.ErrorException>`
        """
        # Construct URL
        url = self.get_null.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self.get(url, query_parameters, header_parameters)
        pipeline_response = self.pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('bytearray', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_null.metadata = {'url': '/byte/null'}

    def get_empty(
            self, raw=False, **kwargs):
        """Get empty byte value ''.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: bytearray or ClientRawResponse if raw=true
        :rtype: bytearray or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodybyte.models.ErrorException>`
        """
        # Construct URL
        url = self.get_empty.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self.get(url, query_parameters, header_parameters)
        pipeline_response = self.pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('bytearray', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_empty.metadata = {'url': '/byte/empty'}

    def get_non_ascii(
            self, raw=False, **kwargs):
        """Get non-ascii byte string hex(FF FE FD FC FB FA F9 F8 F7 F6).

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: bytearray or ClientRawResponse if raw=true
        :rtype: bytearray or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodybyte.models.ErrorException>`
        """
        # Construct URL
        url = self.get_non_ascii.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self.get(url, query_parameters, header_parameters)
        pipeline_response = self.pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('bytearray', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_non_ascii.metadata = {'url': '/byte/nonAscii'}

    def put_non_ascii(
            self, byte_body, raw=False, **kwargs):
        """Put non-ascii byte string hex(FF FE FD FC FB FA F9 F8 F7 F6).

        :param byte_body: Base64-encoded non-ascii byte string hex(FF FE FD FC
         FB FA F9 F8 F7 F6)
        :type byte_body: bytearray
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodybyte.models.ErrorException>`
        """
        # Construct URL
        url = self.put_non_ascii.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(byte_body, 'bytearray')

        # Construct and send request
        request = self.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self.pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_non_ascii.metadata = {'url': '/byte/nonAscii'}

    def get_invalid(
            self, raw=False, **kwargs):
        """Get invalid byte value ':::SWAGGER::::'.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: bytearray or ClientRawResponse if raw=true
        :rtype: bytearray or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodybyte.models.ErrorException>`
        """
        # Construct URL
        url = self.get_invalid.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self.get(url, query_parameters, header_parameters)
        pipeline_response = self.pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('bytearray', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_invalid.metadata = {'url': '/byte/invalid'}
