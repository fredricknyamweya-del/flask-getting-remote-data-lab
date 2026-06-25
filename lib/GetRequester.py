import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        """
        Send an HTTP GET request to the stored URL
        and return the raw response body as text.
        """
        response = requests.get(self.url)
        response.raise_for_status()  # raises error if request fails
        return response.text

    def load_json(self):
        """
        Call get_response_body, then parse the response
        into Python data structures using json.loads.
        """
        response_body = self.get_response_body()
        return json.loads(response_body)
