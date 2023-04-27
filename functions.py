# IMPORT REQUESTS TO RECEIVE RESPONSES
import requests


# FUNCRION TO MAKE REQUEST
def get_code(url) -> requests.Response:
    return requests.get(url)
