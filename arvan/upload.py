from __future__ import absolute_import
import arvantus
import requests


class UploadFileMixin(object):
    """Handle uploading a new temporary file to the ArvanCloud API."""
    CHUNK_SIZE = 256000

    def upload_file(self, filename):
        """
        This will first upload a file using tus
        Then will create the video
        'https://napi.arvancloud.com/vod/2.0/channels/{channel_id}/files'
        Args:
        """
        TUS_ENDPOINT = 'https://napi.arvancloud.com/vod/2.0/channels/' + self.channel + '/files'
        HEADERS = {'Authorization': self.token}

        with open(filename, 'rb') as f:
            x = arvantus.upload(
                f,
                TUS_ENDPOINT,
                headers=HEADERS,
                chunk_size=self.CHUNK_SIZE,  # file_name='xxx.mp4',
                metadata={'filename': 'video.mp4', 'filetype': 'video/mp4'}
            )
        return x


class UploadVideoMixin(object):
    """Handle uploading a new video to the ArvanCloud API."""

    def upload_video(self, filename, title, convert_mode, **kwargs):
        TUS_ENDPOINT = 'https://napi.arvancloud.com/vod/2.0/channels/' + self.channel + '/videos'
        HEADERS = {'Authorization': self.token}
        file_url = self.upload_file(filename)
        file_id = file_url[file_url.rfind('/') + 1:]
        data = kwargs['data'] if 'data' in kwargs else {}
        data["title"] = title
        data["file_id"] = file_id
        data["convert_mode"] = convert_mode
        r = requests.post(url=TUS_ENDPOINT, headers=HEADERS, data=data)
        return r


class UploadMixin(UploadFileMixin, UploadVideoMixin):
    """This is going to be extended in future for files, thumbnails"""
    pass
