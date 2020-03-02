from __future__ import absolute_import
from functools import wraps
import requests
from upload import UploadMixin
from get import GetMixin
from channels import ChannelMixin


class ArvanClient(UploadMixin, GetMixin):
    """
    Base Client for Arvan Cloud API
    Api Documentation can be found here:
    https://napi.arvancloud.com/docs/vod/2.0#/
    """

    API_ROOT = "https://napi.arvancloud.com/vod/2.0"

    def __init__(self, token=None, channel=None, *args, **kwargs):
        """
        Not sure about getting the channel ID in initialization
        Probably going to remove it later
        And only get the channel name for another object
        :param token: Token You get from the panel, Must be started with "API KEY ..."
        :param channel: ID of the channel, NOT name
        """
        self.token = token
        self.channel = channel

        assert token is not None


class StaticClient(ChannelMixin, GetMixin):
    """
    Unlike the ArvanClient which needs a channel ID
    this is for Static data and doesn't need any channel ID

    I'm still not sure if it's a clean way to do it
    so if you have any suggestion for improving the architecture please contact me
    """

    API_ROOT = "https://napi.arvancloud.com/vod/2.0"
    # HTTP_METHODS = set(('head', 'get', 'post', 'put', 'patch', 'options',
    #                     'delete'))

    def __init__(self, token=None, *args, **kwargs):
        """
        :param token: Token You get from the panel, Must be started with "API KEY ..."
        """
        self.token = token

        assert token is not None

