import requests
import re

def tmobileLogin(username, password):
    s = requests.Session()
    result = s.get("https://tmobile.ee.co.uk/service/your-account/default-tm-login/")
    match = re.search('name="org\.apache\.struts\.taglib\.html\.TOKEN" value="([a-f0-9]+)"></div>', result.text)
    data = {'username': username, 'password': password, 'org.apache.struts.taglib.html.TOKEN': match.group(1), 'submit': 'Log+In'}
    result = s.post("https://tmobile.ee.co.uk/service/your-account/login/", data=data)
    if result.status_code != 200:
        return False
    else:
        return s

def tmobileGetSendToken(s):
    result = s.get("https://tmobile.ee.co.uk/service/your-account/private/wgt/send-text-preparing/")
    if result.status_code != 200:
        return False
    else:
        match = re.search('name="org\.apache\.struts\.taglib\.html\.TOKEN" value="([a-f0-9]+)"></div>', result.text)
        if match:
            return match.group(1)
        else:
            return False

def tmobileSendMsg(s, recipients, msg, token):
    data = {'selectedRecipients': recipients, 'org.apache.struts.taglib.html.TOKEN': token, 'message': msg, 'submit': 'Send'}
    result = s.post("https://tmobile.ee.co.uk/service/your-account/private/wgt/send-text-processing/", data = data)
    if result.status_code != 200:
        return False
    else:
        return True
