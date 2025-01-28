import requests
from time import sleep


class Requester():
    def __init__(self,max_retries=3,backoff_factor=2,status_forcelist=[429, 500, 502, 503, 504]):
            self.max_retries=max_retries
            self.backoff_factor=backoff_factor
            self.status_forcelist=status_forcelist
    def retri_logic(self,requests_type,url,**kwargs):
            for i in range(self.max_retries):
                   try:
                        response = requests_type(url,**kwargs)
                        if response.status_code in self.status_forcelist:
                              return response
                        else:
                              print(f"HTTP {response.status_code}: {response.text}")
                   except requests.RequestException as e:
                         print(f"Request error: {e}")

                   sleep(self.backoff_factor * (2 ** (i - 1)))

    def get(self, url, headers=None, data=None, params=None):
          return self.retri_logic(requests.get,url,headers=headers,params=params)
    
    def post(self, url, headers=None, data=None, params=None):
      return self.retri_logic(requests.post, url, headers=headers, data=data, params=params)

         