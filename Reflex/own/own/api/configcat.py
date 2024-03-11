import reflex as rx 
import configcatclient
import os
import dotenv


class ConfigCatAPI:
    
    dotenv.load_dotenv()
    
    PROD_CONFIGCAT_SDK = os.getenv('PROD_CONFIGCAT_SDK')
    TEST_CONFIGCAT_SDK = os.getenv('TEST_CONFIGCAT_SDK')
    
    
    def __init__(self) -> None:
        self.configcat_client is None
    
    def generate_client(self):
        if self.configcat_client is None:
            self.configcat_client = configcatclient.get(self.EST_CONFIGCAT_SDK)
    
    def schedule(self) -> str:
        if self.configcat_client is None:
            self.generate_client() 
        
        return self.configcat_client.get_value("schedule","")