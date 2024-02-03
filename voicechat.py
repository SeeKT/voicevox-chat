import argparse
import json 
from libs.text_to_voicevox import TextToVoicevox 

def main():
    parser = argparse.ArgumentParser(description='Voice Chat to VOICEVOX')
    parser.add_argument('-s', '--speaker', default=2, help='the speaker id of the VOICEVOX character')
    parser.add_argument('-r', '--retry', default=20, help='maximum limit of retry')
    parser.add_argument('--host', default='127.0.0.1', help='VOICEVOX host')
    parser.add_argument('--port', default='50021', help='Port of VOICEVOX')
    
    args = parser.parse_args()
    
    texttovoicevox = TextToVoicevox(args.speaker, args.retry, args.host, args.port)
    message = 'LLM の API を使いたかったけど、公開されているものは有償だから手元で構築することにしたよ。'
    texttovoicevox._text_to_voicevox(message)
    
if __name__ == '__main__':
    main()