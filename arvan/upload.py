from __future__ import absolute_import
import file_upload
import requests


class UploadVideoMixin(object):
    """Handle uploading a new video to the Vimeo API."""
    CHUNK_SIZE = 256000

    def upload(self, filename, **kwargs):
        """
        This will first upload a file using tus
        Then will create the video
        'https://napi.arvancloud.com/vod/2.0/channels/{channel_id}/files'
        Args:
        """
        TUS_ENDPOINT = 'https://napi.arvancloud.com/vod/2.0/channels/' + self.channel + '/files'
        HEADERS = {'Authorization': self.token}

        with open(filename, 'rb') as f:
            x = file_upload.upload(
                f,
                TUS_ENDPOINT,
                headers=HEADERS,
                chunk_size=self.CHUNK_SIZE, # file_name='xxx.mp4',
                metadata={'filename': 'video.mp4', 'filetype': 'video/mp4'}
            )
        print(x)
        return x


class UploadMixin(UploadVideoMixin):
    """This is going to be extended in future for files, thumbnails"""
    pass
