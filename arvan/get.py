from __future__ import absolute_import
import requests


class GetVideoMixin(object):
    """Handle uploading a new temporary file to the ArvanCloud API."""

    def get_hls(self, video_id):
        """
        Getting the HLS link using File ID
        Args:
        """
        endpoint = 'https://napi.arvancloud.com/vod/2.0/videos/' + video_id
        header = {'Authorization': self.token}

        return requests.get(url=endpoint, headers=header).json()['data']['hls_playlist']


class GetMixin(GetVideoMixin):
    pass
