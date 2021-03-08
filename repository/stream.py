import streamlink
from streamlink.stream import Stream

from repository.live import Live


def serialize_stream(stream: Stream):
    return stream.__json__()


def get_stream_info(live: Live):
    streams = streamlink.streams(live.get_url())
    return {quality: serialize_stream(stream) for quality, stream in streams.items()}
