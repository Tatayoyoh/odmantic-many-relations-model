import sys
import json
import http.client

BACKEND_URL = 'localhost:9800'

REQUEST_HEADERS = {
    "Host": BACKEND_URL,
    "Content-type": "application/json"
}

def request(method='GET', url='/', data=None, print_response=False):
    """
        A quit wrap of `http.client` for tests
        `http.client` needs no pip install with Python3 :)
    """

    conn = http.client.HTTPConnection(BACKEND_URL)

    if data: data = json.dumps(data)

    try:
        conn.request(method, url, data, REQUEST_HEADERS)
    except:
        quit('No FastAPI backend is running at http://%s\nStart this example with "docker compose up -d"'%BACKEND_URL)

    r = conn.getresponse()

    response = json.loads(r.read())

    if r.status != 200:
        quit("%s %s"%(r.status, response))

    if print_response:
        print(json.dumps(response, indent=2))

    return response


def quit(reason:str):
    print(reason)
    sys.exit(-1)