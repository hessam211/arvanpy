from __future__ import absolute_import
import requests


class GetVideosMixin(object):

    def get_videos(self):
        """
        Getting all of the videos inside a channel
        """
        endpoint = 'https://napi.arvancloud.com/vod/2.0/channels/' + self.channel + '/videos'
        header = {'Authorization': self.token}

        return requests.get(url=endpoint, headers=header)


class GetVideoMixin(object):
    """Getting the data for a specific video ArvanCloud API."""

    def get_video(self, video_id):
        """
        Getting the whole Json of video information using Video ID
        """
        endpoint = 'https://napi.arvancloud.com/vod/2.0/videos/' + video_id
        header = {'Authorization': self.token}

        return requests.get(url=endpoint, headers=header)

    def get_hls(self, video_id):
        """
        Getting the HLS link using Video ID
        """
        endpoint = 'https://napi.arvancloud.com/vod/2.0/videos/' + video_id
        header = {'Authorization': self.token}

        return requests.get(url=endpoint, headers=header).json()['data']['hls_playlist']

    def get_video_url(self, video_id):
        """
        Getting the Video Source link using Video ID
        """
        endpoint = 'https://napi.arvancloud.com/vod/2.0/videos/' + video_id
        header = {'Authorization': self.token}

        return requests.get(url=endpoint, headers=header).json()['data']['video_url']

    def get_player_url(self, video_id):
        """
        Getting the Player link using Video ID
        """
        endpoint = 'https://napi.arvancloud.com/vod/2.0/videos/' + video_id
        header = {'Authorization': self.token}

        return requests.get(url=endpoint, headers=header).json()['data']['player_url']


class GetMixin(GetVideoMixin, GetVideosMixin):
    pass
