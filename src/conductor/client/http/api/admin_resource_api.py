from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from conductor.client.http.api_client import ApiClient


class AdminResourceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_event_queues(self, **kwargs):  # noqa: E501
        """Get registered queues  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_event_queues(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool verbose:
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_event_queues_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_event_queues_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_event_queues_with_http_info(self, **kwargs):  # noqa: E501
        """Get registered queues  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_event_queues_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool verbose:
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['verbose']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_event_queues" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'verbose' in params:
            query_params.append(('verbose', params['verbose']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/admin/queues', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, object)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_redis_usage(self, **kwargs):  # noqa: E501
        """Get details of redis usage  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_redis_usage(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_redis_usage_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_redis_usage_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_redis_usage_with_http_info(self, **kwargs):  # noqa: E501
        """Get details of redis usage  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_redis_usage_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: dict(str, object)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_redis_usage" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/admin/redisUsage', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, object)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def requeue_sweep(self, workflow_id, **kwargs):  # noqa: E501
        """Queue up all the running workflows for sweep  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.requeue_sweep(workflow_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workflow_id: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.requeue_sweep_with_http_info(workflow_id, **kwargs)  # noqa: E501
        else:
            (data) = self.requeue_sweep_with_http_info(workflow_id, **kwargs)  # noqa: E501
            return data

    def requeue_sweep_with_http_info(self, workflow_id, **kwargs):  # noqa: E501
        """Queue up all the running workflows for sweep  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.requeue_sweep_with_http_info(workflow_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workflow_id: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workflow_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method requeue_sweep" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workflow_id' is set
        if ('workflow_id' not in params or
                params['workflow_id'] is None):
            raise ValueError("Missing the required parameter `workflow_id` when calling `requeue_sweep`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in params:
            path_params['workflowId'] = params['workflow_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/admin/sweep/requeue/{workflowId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def verify_and_repair_workflow_consistency(self, workflow_id, **kwargs):  # noqa: E501
        """Verify and repair workflow consistency  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.verify_and_repair_workflow_consistency(workflow_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workflow_id: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.verify_and_repair_workflow_consistency_with_http_info(workflow_id, **kwargs)  # noqa: E501
        else:
            (data) = self.verify_and_repair_workflow_consistency_with_http_info(workflow_id, **kwargs)  # noqa: E501
            return data

    def verify_and_repair_workflow_consistency_with_http_info(self, workflow_id, **kwargs):  # noqa: E501
        """Verify and repair workflow consistency  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.verify_and_repair_workflow_consistency_with_http_info(workflow_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workflow_id: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workflow_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method verify_and_repair_workflow_consistency" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workflow_id' is set
        if ('workflow_id' not in params or
                params['workflow_id'] is None):
            raise ValueError("Missing the required parameter `workflow_id` when calling `verify_and_repair_workflow_consistency`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in params:
            path_params['workflowId'] = params['workflow_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/admin/consistency/verifyAndRepair/{workflowId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def view(self, tasktype, **kwargs):  # noqa: E501
        """Get the list of pending tasks for a given task type  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.view(tasktype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tasktype: (required)
        :param int start:
        :param int count:
        :return: list[Task]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.view_with_http_info(tasktype, **kwargs)  # noqa: E501
        else:
            (data) = self.view_with_http_info(tasktype, **kwargs)  # noqa: E501
            return data

    def view_with_http_info(self, tasktype, **kwargs):  # noqa: E501
        """Get the list of pending tasks for a given task type  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.view_with_http_info(tasktype, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tasktype: (required)
        :param int start:
        :param int count:
        :return: list[Task]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tasktype', 'start', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method view" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tasktype' is set
        if ('tasktype' not in params or
                params['tasktype'] is None):
            raise ValueError("Missing the required parameter `tasktype` when calling `view`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tasktype' in params:
            path_params['tasktype'] = params['tasktype']  # noqa: E501

        query_params = []
        if 'start' in params:
            query_params.append(('start', params['start']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/admin/task/{tasktype}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Task]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
