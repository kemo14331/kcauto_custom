import datetime
import socket
import requests
import json

from version import __version__
import config.config_core as cfg
from util.logger import Log


class WebHookCore(object):

    def __init__(self):
        Log.log_debug("Webhook module initialized.")

    def _post(self, payload):
        try:
            headers = {'Content-Type': 'application/json'}
            requests.post(cfg.config.webhook.url,
                          json.dumps(payload), headers=headers)
        except Exception as e:
            Log.log_error("Failed to post webhook.")
            Log.log_error(e)

    def post(self, title, text, color=0x3bc552, fields=[]):
        self._post({
            "embeds": [{
                "title": title,
                "description": text,
                "color": color,
                "timestamp": f'{datetime.datetime.utcnow()}',
                "footer": {
                    "text": socket.gethostname()
                },
                "author": {
                    "name": f'KCAuto {__version__}',
                    "url": 'https://github.com/XVs32/kcauto_custom/',
                    "icon_url": 'https://upload.wikimedia.org/wikipedia/en/0/02/Kantai_Collection_logo.png'
                },
                "fields": fields
            }]
        })


webhook = WebHookCore()
