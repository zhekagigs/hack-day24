import json

import requests
import uuid
import time

def create_clip(audio_url):
    url = "https://api.d-id.com/clips"

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik53ek53TmV1R3ptcFZTQjNVZ0J4ZyJ9.eyJodHRwczovL2QtaWQuY29tL2ZlYXR1cmVzIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJvZHVjdF9pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vc3RyaXBlX2N1c3RvbWVyX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJvZHVjdF9uYW1lIjoidHJpYWwiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9zdWJzY3JpcHRpb25faWQiOiIiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9iaWxsaW5nX2ludGVydmFsIjoibW9udGgiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9wbGFuX2dyb3VwIjoiZGVpZC10cmlhbCIsImh0dHBzOi8vZC1pZC5jb20vc3RyaXBlX3ByaWNlX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJpY2VfY3JlZGl0cyI6IiIsImh0dHBzOi8vZC1pZC5jb20vY2hhdF9zdHJpcGVfc3Vic2NyaXB0aW9uX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jaGF0X3N0cmlwZV9wcmljZV9jcmVkaXRzIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jaGF0X3N0cmlwZV9wcmljZV9pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vcHJvdmlkZXIiOiJnb29nbGUtb2F1dGgyIiwiaHR0cHM6Ly9kLWlkLmNvbS9pc19uZXciOmZhbHNlLCJodHRwczovL2QtaWQuY29tL2FwaV9rZXlfbW9kaWZpZWRfYXQiOiIyMDI0LTAyLTIxVDE0OjI1OjEwLjAyNVoiLCJodHRwczovL2QtaWQuY29tL29yZ19pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vYXBwc192aXNpdGVkIjpbIlN0dWRpbyJdLCJodHRwczovL2QtaWQuY29tL2N4X2xvZ2ljX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jcmVhdGlvbl90aW1lc3RhbXAiOiIyMDI0LTAyLTIxVDE0OjIxOjM4LjUzNloiLCJodHRwczovL2QtaWQuY29tL2FwaV9nYXRld2F5X2tleV9pZCI6InJpMzBlZDkxd2giLCJodHRwczovL2QtaWQuY29tL3VzYWdlX2lkZW50aWZpZXJfa2V5IjoidThUclJzMllRRURHQnAtNjBvdXdYIiwiaHR0cHM6Ly9kLWlkLmNvbS9oYXNoX2tleSI6ImMyNy1iTXhNWlViaU1Sc0RKd043WCIsImh0dHBzOi8vZC1pZC5jb20vcHJpbWFyeSI6dHJ1ZSwiaHR0cHM6Ly9kLWlkLmNvbS9lbWFpbCI6InpoZWthZ2lnc0BnbWFpbC5jb20iLCJodHRwczovL2QtaWQuY29tL3BheW1lbnRfcHJvdmlkZXIiOiJzdHJpcGUiLCJpc3MiOiJodHRwczovL2F1dGguZC1pZC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDQ3OTE4NDIzMjA2ODczNTQ1MDUiLCJhdWQiOlsiaHR0cHM6Ly9kLWlkLnVzLmF1dGgwLmNvbS9hcGkvdjIvIiwiaHR0cHM6Ly9kLWlkLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE3MDg1MjU1OTAsImV4cCI6MTcwODYxMTk5MCwiYXpwIjoiR3pyTkkxT3JlOUZNM0VlRFJmM20zejNUU3cwSmxSWXEiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIHJlYWQ6Y3VycmVudF91c2VyIHVwZGF0ZTpjdXJyZW50X3VzZXJfbWV0YWRhdGEgb2ZmbGluZV9hY2Nlc3MifQ.f_f5DnlrOqlEodLEch9Skc9YFPHKbundNa3Xv-PHw16VVm790luA4lqEav8GWZYLgRciFAMjIbIVftWWSjERfDWy7X4dSZSrHp7i-Skre-K8xpPKsJ81tv4V_uZhU33oBo2K8C519XCpLfeDsXesjpTJxanrqdRdz1ByVKFKs2-_EvkOFAc0bsbf4GHyv-EnUMGkbOXEkrXbaCa-3N5CSqLN_9viI0o2azIA5M1EZkrkGCUp-EDi2aw-JwNWJDQrCDmNG8bgurq3TiIp5Ap33OCuVaIra-eaXXMKuhNFFfoWUf_62r1yeuCVnQR9jaYHKrIRpSPaGPNo22EBKTl_7A"
    }

    script = {
            "type": "audio",
            "text": "Hello World",
            "audio_url": audio_url
        }

    body = {
        "presenter_id": "amy-Aq6OmGZnMt",
        "script": script
    }

    response = requests.post(url, headers=headers, json=body)
    print(response.text)

    data = response.json()
    video_id = data['id']
    url = f'https://api.d-id.com/clips/{video_id}'
    video_link = get_clip_link(url)
    filename = download_clip(video_link)
    return filename


def get_clip_link(url):
    print("get clip link", url)
    print("waiting")
    time.sleep(10)
    headers = {
        "accept": "application/json",
        "authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik53ek53TmV1R3ptcFZTQjNVZ0J4ZyJ9.eyJodHRwczovL2QtaWQuY29tL2ZlYXR1cmVzIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJvZHVjdF9pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vc3RyaXBlX2N1c3RvbWVyX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJvZHVjdF9uYW1lIjoidHJpYWwiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9zdWJzY3JpcHRpb25faWQiOiIiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9iaWxsaW5nX2ludGVydmFsIjoibW9udGgiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9wbGFuX2dyb3VwIjoiZGVpZC10cmlhbCIsImh0dHBzOi8vZC1pZC5jb20vc3RyaXBlX3ByaWNlX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJpY2VfY3JlZGl0cyI6IiIsImh0dHBzOi8vZC1pZC5jb20vY2hhdF9zdHJpcGVfc3Vic2NyaXB0aW9uX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jaGF0X3N0cmlwZV9wcmljZV9jcmVkaXRzIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jaGF0X3N0cmlwZV9wcmljZV9pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vcHJvdmlkZXIiOiJnb29nbGUtb2F1dGgyIiwiaHR0cHM6Ly9kLWlkLmNvbS9pc19uZXciOmZhbHNlLCJodHRwczovL2QtaWQuY29tL2FwaV9rZXlfbW9kaWZpZWRfYXQiOiIyMDI0LTAyLTIxVDE0OjI1OjEwLjAyNVoiLCJodHRwczovL2QtaWQuY29tL29yZ19pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vYXBwc192aXNpdGVkIjpbIlN0dWRpbyJdLCJodHRwczovL2QtaWQuY29tL2N4X2xvZ2ljX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jcmVhdGlvbl90aW1lc3RhbXAiOiIyMDI0LTAyLTIxVDE0OjIxOjM4LjUzNloiLCJodHRwczovL2QtaWQuY29tL2FwaV9nYXRld2F5X2tleV9pZCI6InJpMzBlZDkxd2giLCJodHRwczovL2QtaWQuY29tL3VzYWdlX2lkZW50aWZpZXJfa2V5IjoidThUclJzMllRRURHQnAtNjBvdXdYIiwiaHR0cHM6Ly9kLWlkLmNvbS9oYXNoX2tleSI6ImMyNy1iTXhNWlViaU1Sc0RKd043WCIsImh0dHBzOi8vZC1pZC5jb20vcHJpbWFyeSI6dHJ1ZSwiaHR0cHM6Ly9kLWlkLmNvbS9lbWFpbCI6InpoZWthZ2lnc0BnbWFpbC5jb20iLCJodHRwczovL2QtaWQuY29tL3BheW1lbnRfcHJvdmlkZXIiOiJzdHJpcGUiLCJpc3MiOiJodHRwczovL2F1dGguZC1pZC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDQ3OTE4NDIzMjA2ODczNTQ1MDUiLCJhdWQiOlsiaHR0cHM6Ly9kLWlkLnVzLmF1dGgwLmNvbS9hcGkvdjIvIiwiaHR0cHM6Ly9kLWlkLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE3MDg1MjU1OTAsImV4cCI6MTcwODYxMTk5MCwiYXpwIjoiR3pyTkkxT3JlOUZNM0VlRFJmM20zejNUU3cwSmxSWXEiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIHJlYWQ6Y3VycmVudF91c2VyIHVwZGF0ZTpjdXJyZW50X3VzZXJfbWV0YWRhdGEgb2ZmbGluZV9hY2Nlc3MifQ.f_f5DnlrOqlEodLEch9Skc9YFPHKbundNa3Xv-PHw16VVm790luA4lqEav8GWZYLgRciFAMjIbIVftWWSjERfDWy7X4dSZSrHp7i-Skre-K8xpPKsJ81tv4V_uZhU33oBo2K8C519XCpLfeDsXesjpTJxanrqdRdz1ByVKFKs2-_EvkOFAc0bsbf4GHyv-EnUMGkbOXEkrXbaCa-3N5CSqLN_9viI0o2azIA5M1EZkrkGCUp-EDi2aw-JwNWJDQrCDmNG8bgurq3TiIp5Ap33OCuVaIra-eaXXMKuhNFFfoWUf_62r1yeuCVnQR9jaYHKrIRpSPaGPNo22EBKTl_7A"
    }

    response = requests.get(url, headers=headers)
    print("RESPONSE FROM CLIP BY ID", response.text)
    # parse the JSON response

    data = response.json()

    while data.get('result_url') is None:
        response = requests.get(url, headers=headers)
        time.sleep(2)
        print("RETRY GET VIDEO LINK")
        # parse the JSON response
        data = response.json()

    # extract the result_url
    result_url = data.get('result_url')

    print("VIDEO URL", result_url)

    return result_url


def download_clip(url: str):
    print("download clip", url)

    response = requests.get(url)
    random_uuid = uuid.uuid4()
    random_filename = f"{random_uuid}.mp4"

    with open(random_filename, 'wb') as f:
        f.write(response.content)
    print("FILENAME", random_filename)
    return random_filename
