# src/remindo_api/request.py
"""Class implementation for sending requests to Remindo."""
import json
import time


from Crypto.Hash import HMAC, SHA1, SHA256, SHA512
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
        self.secEncoded = self.secret.encode("utf-8")
        self.ip = client.ip
        self.api_url_base = client.url_base
        self.uuid = client.uuid
        if client.sha:
            if client.sha == "SHA1": self.sha = SHA1
            elif client.sha == "SHA256": self.sha = SHA256
            elif client.sha == "SHA512": self.sha = SHA512
        else:
            self.sha = SHA512
        self.req_format = req_format
        self.url = url
        self.payload = content

    def make_body(self):
        self.timestamp = int(time.time())
        self.envelope = {"uuid": self.uuid, "timestamp": self.timestamp}
        self.body = {"envelope": self.envelope, "payload": self.payload}

    def make_message(self):
        self.message = self.ip + ":" + json.dumps((self.body), separators=(",", ":"))
        self.message = self.message.encode("utf-8")

    def encrypt(self):
        self.make_body()
        self.make_message()
        h = HMAC.new(key=self.secEncoded, msg=(self.message), digestmod=self.sha)
        self.signature = h.hexdigest()

    def request(self):
        """Create message request.
        
        Raise:
            RemindoRequestException: the request failed with status code
            =! 200.
        """
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
            try:
                if self.req_format == "json":
                    respJson = resp.json()
                    # To catch some error messages
                    if type(respJson["payload"]) is not bool:
                        payload = json.loads(respJson["payload"])
                        return payload
                    else:
                        payload = {"success": False}
                        return payload
            except Exception as e:
                print("A problem occurred in the request with message:")
                print(e)

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
