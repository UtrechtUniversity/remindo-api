# src/remindo_api/request.py
"""Class implementation for sending requests to Remindo."""
import json
import time


from Cryptodome.Hash import HMAC, SHA1, SHA256
import requests


class RemindoRequestException(Exception):
    """Class that is called for exception messages.

    You can see the usage of this class looking at the test.
    """

    def __init__(self, error_msg, url):
        self.error_msg = error_msg
        self.url = url

    def __str__(self):
        return (self.url, ":", self.error_msg)


class RemindoRequest:
    """Main class to send requests to Remindo.

    To finish its documentation.
    """

    def __init__(self, client, url, content, req_format="json"):
        """Instantiate all the relevant parameters.

        To instantiate all the keys, this class uses the `config.ini` file.
        """
        self.secret = client.secret
        self.ip = client.ip
        self.api_url_base = client.url_base
        self.uuid = client.uuid
        self.req_format = req_format
        self.url = url
        self.content = content
        self.payload = self.content

    def make_envelope(self):
        self.timestamp = int(time.time())
        self.envelope = {"uuid": self.uuid, "timestamp": self.timestamp}
        self.secEncoded = self.secret.encode("utf-8")

    def make_body(self):
        self.make_envelope()
        self.body = {"envelope": self.envelope, "payload": self.payload}

    def make_message(self):
        self.message = self.ip + ":" + json.dumps((self.body), separators=(",", ":"))
        self.message = self.message.encode("utf-8")

    def encrypt(self):
        self.make_body()
        self.make_message()
        h = HMAC.new(key=self.secEncoded, msg=(self.message), digestmod=SHA256)
        self.signature = h.hexdigest()

    def request(self):
        """Create message request."""
        self.contentDumped = json.dumps(self.content)
        self.encrypt()
        params = {
            "payload": self.payload,
            "envelope": self.envelope,
            "signature": self.signature,
        }
        time.sleep(0.05)
        parameters = json.dumps(params, separators=(",", ":"))
        resp = requests.post(
            (self.api_url_base + self.url), data=parameters, timeout=None
        )
        if resp.status_code != 200:
            raise RemindoRequestException(resp.reason, self.url)
        else:
            if self.req_format == "json":
                respJson = resp.json()
                # To catch some error messages
                if type(respJson["payload"]) is not bool:
                    payload = json.loads(respJson["payload"])
                    return payload
                else:
                    payload = {"success": False}
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
