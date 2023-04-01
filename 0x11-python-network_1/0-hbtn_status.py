#!/usr/bin/python3
<<<<<<< HEAD
"""Fetches https://docs.python.org/status."""
=======
"""Fetches https://intranet.hbtn.io/status."""
>>>>>>> dd7f2d30483a78234aefc53faea37d9dd0fa2eef
import urllib.request


if __name__ == "__main__":
<<<<<<< HEAD
    request = urllib.request.Request("https://docs.python.org/status")
=======
    request = urllib.request.Request("https://intranet.hbtn.io/status")
>>>>>>> dd7f2d30483a78234aefc53faea37d9dd0fa2eef
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
