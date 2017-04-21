#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import logging
logger = logging.getLogger(__name__)


class HttpProxyMiddleware(object):

    def process_request(self, request, spider):
        return None

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        return None
