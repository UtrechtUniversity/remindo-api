import json
import time

import requests
from Cryptodome.Hash import HMAC, SHA1


class RemindoRequestException(Exception):
    """Class that is called for exception messages

    You can see the usage of this class looking at the test

    """

    def __init__(self, error_msg, url):
        self.error_msg = error_msg
        self.url = url

    def __str__(self):
        return (self.url, ":", self.error_msg)


class RemindoRequest:
    """Main class to send requests to Remindo

    To finish its documentation

    """

    def __init__(self, client, url, content, req_format="json"):
        """Instantiate all the relevant parameters

        To instantiate all the keys, this class uses the `config.ini` file.

        """
        self.secret = client.secret
        self.ip = client.ip
        self.api_url_base = client.url_base
        self.uuid = client.uuid
        self.req_format = req_format
        self.url = url
        self.content = content
        self.timestamp = int(time.time())
        self.envelope = {"uuid": self.uuid, "timestamp": self.timestamp}
        self.secEncoded = self.secret.encode("utf-8")
        self.payload = self.content
        self.body = {"envelope": self.envelope, "payload": self.payload}
        self.message = self.ip + ":" + json.dumps((self.body), separators=(",", ":"))
        self.message = self.message.encode("utf-8")
        h = HMAC.new((self.secEncoded), msg=(self.message), digestmod=SHA1)
        self.signature = h.hexdigest()

    def request(self):
        """Create message request"""
        self.contentDumped = json.dumps(self.content)
        params = {
            "payload": self.payload,
            "envelope": self.envelope,
            "signature": self.signature,
        }
        time.sleep(0.1)
        parameters = json.dumps(params, separators=(",", ":"))
        resp = requests.post(
            (self.api_url_base + self.url), data=parameters, timeout=None
        )
        if resp.status_code != 200:
            raise RemindoRequestException(resp.reason, self.url)
        else:
            if self.req_format == "json":
                respJson = resp.json()
                payload = json.loads(respJson["payload"])
                return payload
            raise Exception("Other problem")

    def makeFilter(self, params):
        """Creates filter based on parameters that are passed."""
        if "," in params:
            params = params.split(",")
            body = {params[i]: params[(i + 1)] for i in range(0, len(params), 2)}
            return body
        return params

    def makeTable(self, response):
        """Creates filter based on parameters that are passed."""
        table = response
        return table
