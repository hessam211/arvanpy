from __future__ import absolute_import
import requests


class GetVideoMixin(object):
    """Getting the data for a specific video ArvanCloud API."""

    def get_video(self, video_id):
        """
        Getting the whole Json of video information using Video ID
        Args:
        """
        endpoint = 'https://napi.arvancloud.com/vod/2.0/videos/' + video_id
        header = {'Authorization': self.token}

        return requests.get(url=endpoint, headers=header).json()['data']

    def get_hls(self, video_id):
        """
        Getting the HLS link using Video ID
        Args:
        """
        endpoint = 'https://napi.arvancloud.com/vod/2.0/videos/' + video_id
        header = {'Authorization': self.token}

        return requests.get(url=endpoint, headers=header).json()['data']['hls_playlist']

    def get_video_url(self, video_id):
        """
        Getting the Video Source link using Video ID
        Args:
        """
        endpoint = 'https://napi.arvancloud.com/vod/2.0/videos/' + video_id
        header = {'Authorization': self.token}

        return requests.get(url=endpoint, headers=header).json()['data']['video_url']

    def get_player_url(self, video_id):
        """
        Getting the Player link using Video ID
        Args:
        """
        endpoint = 'https://napi.arvancloud.com/vod/2.0/videos/' + video_id
        header = {'Authorization': self.token}

        return requests.get(url=endpoint, headers=header).json()['data']['player_url']


class GetMixin(GetVideoMixin):
    pass
