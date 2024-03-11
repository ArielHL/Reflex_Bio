import dotenv
import os
import requests
import time

class TwitchAPI:
    
    dotenv.load_dotenv()
    
    def __init__(self):
        self.client_id = os.environ.get('TWITCH_CLIENT_ID')
        self.client_secret = os.environ.get('TWITCH_CLIENT_SECRET')
        self.token = None
        self.token_exp = 0
        self.response = None
        self.response_code = None
        
    def generate_token(self):
        response = requests.post(
                                "https://id.twitch.tv/oauth2/token",
                                data = {
                                        "client_id":self.client_id,
                                        "client_secret":self.client_secret,
                                        "grant_type":"client_credentials"          
                                }
        )
        
        self.response_code = response.status_code
        
        if response.status_code == 200:
            
            self.token=  response.json()['access_token']
            self.token_exp = time.time() + response.json()['expires_in']
            
        else:
            self.token = None
            self.token_exp = 0
            raise Exception("Error in generating token")
        
    def token_valid(self) -> bool:
        return self.token and time.time() < self.token_exp
        
    
    def live(self,user:str) -> bool:
        
        if not self.token_valid():
            self.generate_token()
            
        response = requests.get(
                    "https://api.twitch.tv/helix/streams?user_login={user}",
                    headers = {
                            "Client-ID":self.client_id,
                            "Authorization": f"Bearer {self.token}"
                    }
        )
        
        if response.status_code == 200 and response.json()['data']:
            data = response.json()['data']
            print(data)
            return True
        
        return False
        