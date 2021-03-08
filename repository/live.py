from abc import ABC, abstractmethod


class Live(ABC):
    @abstractmethod
    def get_url(self) -> str:
        pass


class TwitchLive(Live):
    def __init__(self, channel: str):
        self.channel = channel

    def get_url(self) -> str:
        return "https://twitch.tv/" + self.channel


def create_live(service: str, channel: str) -> Live:
    if service == "twitch":
        return TwitchLive(channel)
    else:
        raise InvalidServiceException


class InvalidServiceException(Exception):
    pass
