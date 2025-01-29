import requests
from time import sleep


class Requester:
    def __init__(self, max_retries=1, backoff_factor=2,status_forcelist=[403,429,500,502,503,504,]):
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor
        self.status_forcelist = status_forcelist
    
    def _retry_logic(self, method, url, **kwargs):
        for i in range(self.max_retries):
            try:
                response = method(url, **kwargs)     
                if response.status_code not in self.status_forcelist:
                    return response  
            except requests.RequestException as e:
                print(f"Request error: {e}")

            sleep(self.backoff_factor * (2 ** (i - 1)))
        return None 

    def get(self,url,headers=None,params=None):
         return self._retry_logic(requests.get, url, headers=headers, params=params)
    
    def post(self,url,headers=None,data=None):
         return self._retry_logic(requests.post, url, headers=headers, data=data)   
            
