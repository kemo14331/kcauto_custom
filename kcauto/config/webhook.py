from config.config_base import ConfigBase

class ConfigWebhook(ConfigBase):
    _enabled = False
    _url = None

    def __init__(self, config):
        super().__init__(config)
        self.enabled = config["webhook.enabled"]
        self.url = config["webhook.url"]

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        if type(value) is not bool:
            raise ValueError(
                "Specified value for webhook enabled is not a boolean.")
        self._enabled = value

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        if type(value) is not str:
            raise ValueError(
                "Specified value for webhook url is not a string.")
        self._url = value