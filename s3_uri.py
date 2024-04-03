from urllib.parse import urlparse


class S3Uri(object):
    def __init__(self, uri):
        self._parsed = urlparse(uri, allow_fragments=False)

    @property
    def bucket(self):
        return self._parsed.netloc

    @property
    def key(self):
        return self._parsed.path.lstrip("/")

    @property
    def uri(self):
        return self._parsed.geturl()
