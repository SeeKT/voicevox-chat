import argparse
import json 
import yaml 
from libs.text_to_voicevox import TextToVoicevox 
from libs.text_to_llm import TextToLLM


CONFIGPATH = 'config/config.yml'

def _load_yaml(path):
    with open(path, encoding='utf-8') as f:
        yml_dict = yaml.safe_load(f)
    return yml_dict 

def main():
    config_dict = _load_yaml(CONFIGPATH)
    
    parser = argparse.ArgumentParser(description='Voice Chat to VOICEVOX')
    parser.add_argument('-s', '--speaker', default=config_dict['Parameters']['speaker'], help='the speaker id of the VOICEVOX character')
    parser.add_argument('-r', '--retry', default=config_dict['Parameters']['retry'], help='maximum limit of retry')
    parser.add_argument('--history', default=None, help='the path of chat history file')
    parser.add_argument('--vhost', default=config_dict['Parameters']['vhost'], help='VOICEVOX host')
    parser.add_argument('--vport', default=config_dict['Parameters']['vport'], help='Port of VOICEVOX')
    parser.add_argument('--lhost', default=config_dict['Parameters']['lhost'], help='Local LLM host')
    parser.add_argument('--lport', default=config_dict['Parameters']['lport'], help='Port of Local LLM')
    parser.add_argument('--system', default=config_dict['Prompt']['system'], help='System Prompt of Local LLM')
    args = parser.parse_args()
    
    ## load history file
    if args.history is not None:
        with open(args.history, 'r', encoding='utf-8') as fp:
            chattalk = json.load(fp)
    else:
        chattalk = [
            {"content": args.system, "role": "system"}
        ]
    
    texttovoicevox = TextToVoicevox(args.speaker, args.retry, args.vhost, args.vport)
    texttollm = TextToLLM(args.retry, args.lhost, args.lport, chattalk)
    while True:
        if texttollm.chatcount == 0:
            print('-'*50)
            content = texttollm._run()
            texttollm.chatcount += 1
        else:
            isCon = input("Do you want to continue? y/n \n")
            print('-'*50)
            if isCon == 'y' or isCon == 'Y':
                content = texttollm._run()
                texttollm.chatcount += 1
            elif isCon == 'n' or isCon == 'N':
                print('-'*50)
                print('Good Bye!')
                texttollm._save_talking()
                break
            else:
                print('Error input. Please input y/n \n')
                continue
        print(f"LLM chat: \n {content}")
        print('-'*50)
        texttovoicevox._text_to_voicevox(content)
    
if __name__ == '__main__':
    main()