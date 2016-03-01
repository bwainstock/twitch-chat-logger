import json
import requests
import time

from requests.exceptions import ConnectionError, SSLError


def get_top_streams(n):
    twitch_api_url = 'https://api.twitch.tv/kraken/streams/?limit=%i' % n
    try:
        return json.loads(requests.get(twitch_api_url).text)['streams']
    except (ValueError, ConnectionError, SSLError):
        time.sleep(5)
        return get_top_streams(n)


def get_channel_names(streams):
    return [stream['channel']['name'] for stream in streams]


def current_time_in_milli():
    return int(round(time.time() * 1000))


def parse_channels_list(filename):
        with open(filename, 'r') as f:
            return f.read().lower().splitlines()


def get_streams_from_channels(channels):
    twitch_stream_url = 'https://api.twitch.tv/kraken/streams/{channel}'
    print channels
    streams = [json.loads(requests.get(twitch_stream_url.format(channel=channel)).text) for channel in channels]
    return [stream['stream'] for stream in streams if 'stream' in stream]
