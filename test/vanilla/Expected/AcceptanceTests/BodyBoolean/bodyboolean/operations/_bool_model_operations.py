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


class BoolModelOperations(object):
    """BoolModelOperations operations.

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

    def get_true(
            self, raw=False, **kwargs):
        """Get true Boolean value.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: bool or ClientRawResponse if raw=true
        :rtype: bool or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodyboolean.models.ErrorException>`
        """
        # Construct URL
        url = self.get_true.metadata['url']

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
            deserialized = self._deserialize('bool', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_true.metadata = {'url': '/bool/true'}

    def put_true(
            self, raw=False, **kwargs):
        """Set Boolean value true.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodyboolean.models.ErrorException>`
        """
        bool_body = True

        # Construct URL
        url = self.put_true.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(bool_body, 'bool')

        # Construct and send request
        request = self.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self.pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_true.metadata = {'url': '/bool/true'}

    def get_false(
            self, raw=False, **kwargs):
        """Get false Boolean value.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: bool or ClientRawResponse if raw=true
        :rtype: bool or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodyboolean.models.ErrorException>`
        """
        # Construct URL
        url = self.get_false.metadata['url']

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
            deserialized = self._deserialize('bool', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_false.metadata = {'url': '/bool/false'}

    def put_false(
            self, raw=False, **kwargs):
        """Set Boolean value false.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodyboolean.models.ErrorException>`
        """
        bool_body = False

        # Construct URL
        url = self.put_false.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(bool_body, 'bool')

        # Construct and send request
        request = self.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self.pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_false.metadata = {'url': '/bool/false'}

    def get_null(
            self, raw=False, **kwargs):
        """Get null Boolean value.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: bool or ClientRawResponse if raw=true
        :rtype: bool or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodyboolean.models.ErrorException>`
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
            deserialized = self._deserialize('bool', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_null.metadata = {'url': '/bool/null'}

    def get_invalid(
            self, raw=False, **kwargs):
        """Get invalid Boolean value.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: bool or ClientRawResponse if raw=true
        :rtype: bool or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodyboolean.models.ErrorException>`
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
            deserialized = self._deserialize('bool', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_invalid.metadata = {'url': '/bool/invalid'}
