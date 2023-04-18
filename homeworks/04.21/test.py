import json
import random
import string
import urllib.request

def generate_random_text(length=100):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def upload_random_text(api_key, account_id, random_text):
    url = f"https://api.upload.io/v2/accounts/{account_id}/uploads/binary"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "text/plain"
    }
    data = random_text.encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=headers)
    response = urllib.request.urlopen(req)
    return json.loads(response.read())

api_key = "secret_W142ho1AiBjsP2AmE44yQrT3xkrh"
account_id = "W142ho1"

random_text = generate_random_text()
response_json = upload_random_text(api_key, account_id, random_text)
print(json.dumps(response_json, indent=2))
