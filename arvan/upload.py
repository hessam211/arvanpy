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
        tus_endpoint = 'https://napi.arvancloud.com/vod/2.0/channels/' + self.channel + '/files'
        header = {'Authorization': self.token}

        with open(filename, 'rb') as f:
            x = arvantus.upload(
                f,
                tus_endpoint,
                headers=header,
                chunk_size=self.CHUNK_SIZE,  # file_name='xxx.mp4',
                metadata={'filename': 'video.mp4', 'filetype': 'video/mp4'}
            )
        return x


class UploadVideoMixin(object):
    """Handle uploading a new video to the ArvanCloud API."""

    def upload_video(self, filename, **kwargs):
        upload_endpoint = 'https://napi.arvancloud.com/vod/2.0/channels/' + self.channel + '/videos'
        header = {'Authorization': self.token}
        file_url = self.upload_file(filename)
        file_id = file_url[file_url.rfind('/') + 1:]
        data = kwargs['data'] if 'data' in kwargs else {}
        data["file_id"] = file_id
        r = requests.post(url=upload_endpoint, headers=header, data=data)
        return r


class UploadMixin(UploadFileMixin, UploadVideoMixin):
    """This is going to be extended in future for files, thumbnails"""
    pass
