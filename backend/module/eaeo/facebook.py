# ***********************************************************************************
# File Name: facebook.py
# Author: Kane.H
# Created: 2019-11-05
# Description: Facebook Module For Global Usage
# -----------------------------------------------------------------------------------

import requests

# ***********************************************************************************
# @Function: Get Facebook Access Token From Authorization Code
# @Returns: Access Token or None In Error Case
# -----------------------------------------------------------------------------------
def getAccessTokenFromAuthzCode(authz_code, client_id, client_secret, redirect_url):
    try:
        url = "https://graph.facebook.com/v4.0/oauth/access_token?client_id=" + client_id + "&redirect_uri=" + redirect_url + "&client_secret=" + client_secret + "&code=" + str(authz_code)
        res = requests.get(url, verify=False)
        if res.status_code != 200:
            return None
        res = res.json()
        return res["access_token"]
    except Exception as e:
        return None

def convert_shorttermaccesstoken_to_longtermaccesstoken(short_term_token, client_id, client_secret):
    try:
        url = "https://graph.facebook.com/v4.0/oauth/access_token?grant_type=fb_exchange_token&client_id=" + client_id + "&client_secret=" + client_secret + "&fb_exchange_token=" + short_term_token
        res = requests.get(url, verify=False)
        if res.status_code != 200:
            return None
        res = res.json()
        return res["access_token"]
    except Exception as e:
        return None
# ***********************************************************************************
# @Function: Get User Information From Access Token
# @Returns: User Information Dictionary
# -----------------------------------------------------------------------------------
def getUserInforFromAccesstoken(access_token):
    try:
        url = "https://graph.facebook.com/v4.0/me?fields=id,name,accounts.fields(instagram_business_account.fields(name, username))&access_token=" + str(access_token)
        res = requests.get(url, verify=False)
        if res.status_code != 200:
            return None
        return res.json()

    except Exception as e:
        return None