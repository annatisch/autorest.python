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


class HttpRedirectsOperations(object):
    """HttpRedirectsOperations operations.

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

    def head300(
            self, raw=False, **kwargs):
        """Return 300 status code and redirect to /http/success/200.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.head300.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self.head(url, query_parameters, header_parameters)
        pipeline_response = self.pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200, 300]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            client_raw_response.add_headers({
                'Location': 'str',
            })
            return client_raw_response
    head300.metadata = {'url': '/http/redirect/300'}

    def get300(
            self, raw=False, **kwargs):
        """Return 300 status code and redirect to /http/success/200.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: list or ClientRawResponse if raw=true
        :rtype: list[str] or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.get300.metadata['url']

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

        if response.status_code not in [200, 300]:
            raise models.ErrorException(self._deserialize, response)

        header_dict = {}
        deserialized = None
        if response.status_code == 300:
            deserialized = self._deserialize('[str]', response)
            header_dict = {
                'Location': 'str',
            }

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            client_raw_response.add_headers(header_dict)
            return client_raw_response

        return deserialized
    get300.metadata = {'url': '/http/redirect/300'}

    def head301(
            self, raw=False, **kwargs):
        """Return 301 status code and redirect to /http/success/200.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.head301.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self.head(url, query_parameters, header_parameters)
        pipeline_response = self.pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200, 301]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            client_raw_response.add_headers({
                'Location': 'str',
            })
            return client_raw_response
    head301.metadata = {'url': '/http/redirect/301'}

    def get301(
            self, raw=False, **kwargs):
        """Return 301 status code and redirect to /http/success/200.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.get301.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self.get(url, query_parameters, header_parameters)
        pipeline_response = self.pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200, 301]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            client_raw_response.add_headers({
                'Location': 'str',
            })
            return client_raw_response
    get301.metadata = {'url': '/http/redirect/301'}

    def put301(
            self, boolean_value=None, raw=False, **kwargs):
        """Put true Boolean value in request returns 301.  This request should not
        be automatically redirected, but should return the received 301 to the
        caller for evaluation.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.put301.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self.pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [301]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            client_raw_response.add_headers({
                'Location': 'str',
            })
            return client_raw_response
    put301.metadata = {'url': '/http/redirect/301'}

    def head302(
            self, raw=False, **kwargs):
        """Return 302 status code and redirect to /http/success/200.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.head302.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self.head(url, query_parameters, header_parameters)
        pipeline_response = self.pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200, 302]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            client_raw_response.add_headers({
                'Location': 'str',
            })
            return client_raw_response
    head302.metadata = {'url': '/http/redirect/302'}

    def get302(
            self, raw=False, **kwargs):
        """Return 302 status code and redirect to /http/success/200.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.get302.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self.get(url, query_parameters, header_parameters)
        pipeline_response = self.pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200, 302]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            client_raw_response.add_headers({
                'Location': 'str',
            })
            return client_raw_response
    get302.metadata = {'url': '/http/redirect/302'}

    def patch302(
            self, boolean_value=None, raw=False, **kwargs):
        """Patch true Boolean value in request returns 302.  This request should
        not be automatically redirected, but should return the received 302 to
        the caller for evaluation.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.patch302.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self.patch(url, query_parameters, header_parameters, body_content)
        pipeline_response = self.pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [302]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            client_raw_response.add_headers({
                'Location': 'str',
            })
            return client_raw_response
    patch302.metadata = {'url': '/http/redirect/302'}

    def post303(
            self, boolean_value=None, raw=False, **kwargs):
        """Post true Boolean value in request returns 303.  This request should be
        automatically redirected usign a get, ultimately returning a 200 status
        code.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.post303.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self.pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200, 303]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            client_raw_response.add_headers({
                'Location': 'str',
            })
            return client_raw_response
    post303.metadata = {'url': '/http/redirect/303'}

    def head307(
            self, raw=False, **kwargs):
        """Redirect with 307, resulting in a 200 success.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.head307.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self.head(url, query_parameters, header_parameters)
        pipeline_response = self.pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200, 307]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            client_raw_response.add_headers({
                'Location': 'str',
            })
            return client_raw_response
    head307.metadata = {'url': '/http/redirect/307'}

    def get307(
            self, raw=False, **kwargs):
        """Redirect get with 307, resulting in a 200 success.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.get307.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self.get(url, query_parameters, header_parameters)
        pipeline_response = self.pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200, 307]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            client_raw_response.add_headers({
                'Location': 'str',
            })
            return client_raw_response
    get307.metadata = {'url': '/http/redirect/307'}

    def put307(
            self, boolean_value=None, raw=False, **kwargs):
        """Put redirected with 307, resulting in a 200 after redirect.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.put307.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self.pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200, 307]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            client_raw_response.add_headers({
                'Location': 'str',
            })
            return client_raw_response
    put307.metadata = {'url': '/http/redirect/307'}

    def patch307(
            self, boolean_value=None, raw=False, **kwargs):
        """Patch redirected with 307, resulting in a 200 after redirect.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.patch307.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self.patch(url, query_parameters, header_parameters, body_content)
        pipeline_response = self.pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200, 307]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            client_raw_response.add_headers({
                'Location': 'str',
            })
            return client_raw_response
    patch307.metadata = {'url': '/http/redirect/307'}

    def post307(
            self, boolean_value=None, raw=False, **kwargs):
        """Post redirected with 307, resulting in a 200 after redirect.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.post307.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self.pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200, 307]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            client_raw_response.add_headers({
                'Location': 'str',
            })
            return client_raw_response
    post307.metadata = {'url': '/http/redirect/307'}

    def delete307(
            self, boolean_value=None, raw=False, **kwargs):
        """Delete redirected with 307, resulting in a 200 after redirect.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.delete307.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self.delete(url, query_parameters, header_parameters, body_content)
        pipeline_response = self.pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200, 307]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            client_raw_response.add_headers({
                'Location': 'str',
            })
            return client_raw_response
    delete307.metadata = {'url': '/http/redirect/307'}
