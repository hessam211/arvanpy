from __future__ import absolute_import
from functools import wraps
import requests
from upload import UploadMixin
from get import GetMixin


class ArvanClient(UploadMixin, GetMixin):
    """
    Base Client for Arvan Cloud API
    Api Documentation can be found here:
    https://napi.arvancloud.com/docs/vod/2.0#/
    """

    API_ROOT = "https://napi.arvancloud.com/vod/2.0"
    # HTTP_METHODS = set(('head', 'get', 'post', 'put', 'patch', 'options',
    #                     'delete'))

    def __init__(self, token=None, channel=None, *args, **kwargs):
        """
        Not sure about getting the channel ID in initialization
        Probably going to remove it later
        And only get the channel name for another object
        :param token: Token You get from the panel Must be started with "API KEY ..."
        :param channel: ID of the channel, NOT name
        """
        self.token = token
        self.channel = channel
        # self._requests_methods = dict()

        assert token is not None

