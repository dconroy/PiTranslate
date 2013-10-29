import json
import requests
import urllib
import subprocess
import argparse

parser = argparse.ArgumentParser(description='This is a demo script by DaveConroy.com.')
parser.add_argument('-o','--origin_language', help='Origin Language',required=True)
parser.add_argument('-d','--destination_language', help='Destination Language', required=True)
parser.add_argument('-t','--text_to_translate', help='Text to Translate', required=True)
args = parser.parse_args()

## show values ##
print ("Origin: %s" % args.origin_language )
print ("Destination: %s" % args.destination_language )
print ("Text: %s" % args.text_to_translate )

text = args.text_to_translate
origin_language=args.origin_language
destination_language=args.destination_language


def speakOriginText(phrase):
    googleSpeechURL = "http://translate.google.com/translate_tts?tl="+ origin_language +"&q=" + phrase
    subprocess.call(["mplayer",googleSpeechURL], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def speakDestinationText(phrase):
    googleSpeechURL = "http://translate.google.com/translate_tts?tl=" + destination_language +"&q=" + phrase
    print googleSpeechURL
    subprocess.call(["mplayer",googleSpeechURL], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

args = {
        'client_id': '',#your client id here
        'client_secret': '',#your azure secret here
        'scope': 'http://api.microsofttranslator.com',
        'grant_type': 'client_credentials'
    }

oauth_url = 'https://datamarket.accesscontrol.windows.net/v2/OAuth2-13'
oauth_junk = json.loads(requests.post(oauth_url,data=urllib.urlencode(args)).content)
translation_args = {
        'text': text,
        'to': destination_language,
        'from': origin_language
        }

headers={'Authorization': 'Bearer '+oauth_junk['access_token']}
translation_url = 'http://api.microsofttranslator.com/V2/Ajax.svc/Translate?'
translation_result = requests.get(translation_url+urllib.urlencode(translation_args),headers=headers)
translation=translation_result.text[2:-1]

speakOriginText('Translating ' + translation_args["text"])
speakDestinationText(translation)
