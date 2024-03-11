
import os
import dotenv
import requests
import time
from supabase import create_client, Client
from own.modules.database import dataItem


class SupabaseAPI:
    
    dotenv.load_dotenv()
    
    SUPABASE_URL = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
    
    
    def __init__(self) -> None:
        if self.SUPABASE_URL != None and self.SUPABASE_KEY != None:
            self.supabase: Client = create_client(
                self.SUPABASE_URL, self.SUPABASE_KEY
            )
    
        
    
    def get_table(self) -> list[dataItem]:
        
        try:
            response = self.supabase.table('posts').select("*").execute()    
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            print("Error: ")
            response = None
        
        posts_data =[]
        
        if len(response.data)>0:
            for post in response.data:
                posts_data.append(dataItem(
                                    title=post['title'], 
                                    image=post['image'], 
                                    url=post['url']
                                    )
                                  )
        else:
            posts_data.append(dataItem(title="No data", image="No data", url="No data"))
                
        return posts_data