import requests
import json 
import time 
import datetime 
import os 

class TextToLLM:
    def __init__(self, max_retry, host, port, chattalk):
        self.max_retry = max_retry
        self.base_url = f"http://{host}:{port}/"
        self.headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
        self.chattalk = chattalk 
        self.data = dict()
        self.data["messages"] = chattalk
        self.historydir = 'history/'
        self.chatcount = 0
        if not os.path.exists(self.historydir):
            os.makedirs(self.historydir)
    
    def _input_chat(self):
        """Input chat strings

        Returns:
            (str): Chat contents
        """
        content = input("Your chat: \n")
        return content 

    def _add_input(self, content):
        """Add input to data dict
        """
        self.data["messages"].append(
            {"content": content, "role": "user"}
        )
    
    def _chat(self):
        """One Chat

        Raises:
            ConnectionError: maximum limit of retry

        Returns:
            (dict): query
        """
        for _ in range(self.max_retry):
            r = requests.post(
                url=self.base_url + "v1/chat/completions",
                data=json.dumps(self.data),
                headers=self.headers,
                timeout=(10.0, 30.0)
            )
            if r.status_code == 200:
                query = r.json()
                break
            time.sleep(1)
        else:
            raise ConnectionError("maximum limit of retry", self.data["messages"][-1]["content"], r.text)
        return query 
    
    def _run(self):
        """Run chat

        Returns:
            (str): response content
        """
        content = self._input_chat()
        self._add_input(content)
        resp = self._chat()
        message = resp['choices'][0]['message']
        self.data["messages"].append(message)
        return message['content'].lstrip()

    def _save_talking(self):
        """Save the history of talking
        """
        current_time = datetime.datetime.now()
        suffix = current_time.strftime('%Y%m%d%H%M%S')
        history_file = self.historydir + f'history_{suffix}.json'
        with open(history_file, 'w', encoding='utf-8') as fp:
            json.dump(self.data["messages"], fp, indent=2, ensure_ascii=False)