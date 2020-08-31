#!/usr/bin/python3
import argparse
import requests, json, pprint
import sys, os, time
import config as c

# Issues:
# Todo:
# In progress:
# Done:
#  API boilerplate function
#  Auth
#  Basic framework
#  Initial parser
#

def get_args():
    """Get command line arguments"""
    p = argparse.ArgumentParser(description='LW API helper.')
    p.add_argument('--auth-test', action='store_true', help='Test authenticating with lw')
    if len(sys.argv)==1:
        p.print_help(sys.stderr)
        sys.exit(1)
    args = p.parse_args()
    return args


def lw_api_request(endpoint=None, un=c.un, token=None, path="/", data=None, method="GET", timeout=10):
    """Make an api request to liquidweb"""
    endpoint = endpoint or "https://api.liquidweb.com/bleed/"
    token = token or lw_auth()[0]
    path = path.strip(" /")
    headers = {'Content-Type': 'application/json'}
    url = '{}{}'.format(endpoint, path)
    if method == "GET" and data:
        method = "POST"
    if data:
        data = json.dumps(data)
    if method not in ["GET", "POST", "PUT", "DELETE"]:
        raise Exception("HTTP method {} not supported".format(method))
    r = requests.request(method, url, auth=(un, token), data=data, headers=headers, timeout=timeout)
    if r.status_code in (200, 201, 204):
        return r
    else:
        print("Status Code {} while requesting {}".format(r.status_code, url))
        raise Exception("error making api call")


def lw_auth(un=c.un, pw=c.pw, nocache=False):
    """Fetch LW auth token"""
    token_cache = os.path.expanduser(c.token_cache)
    try:
        with open(token_cache, 'r') as f:
            token_data = json.load(f)
            if token_data['expires'] > time.time():
                # Yay! we can use the cached token
                return token_data['token'], token_data['expires']
    except (IOError, ValueError):
        # token file doesnt exist, or is empty/expired. time to get a new one
        pass
    r = lw_api_request(un=c.un, token=pw, path="/Account/Auth/token")
    token_data = r.json()
    with open(token_cache, 'w') as f:
        json.dump(token_data, f)
    return token_data['token'], token_data['expires']
    # url = 'https://api.liquidweb.com/bleed/Account/Auth/token'
    # r = requests.get(url, auth=(un, pw))
    # if r.status_code == 200:
    #     token_data = r.json()
    #     with open(token_cache, 'w') as f:
    #         json.dump(token_data, f)
    #     return token_data['token'], token_data['expires']
    # else:
    #     print("Status Code {} while requesting {}".format(r.status_code, url) )
    #    raise Exception("error making api call")

def main():
    """do stuff i guess"""
    args = get_args()
    if args.auth_test:
        pprint.pprint(lw_auth())


if __name__ == '__main__':
    main()

