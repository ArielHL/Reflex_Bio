import reflex as rx
from own.api.api import live, get_data
from typing import Dict, List

USER = 'mouredev'



class PageState(rx.State):

    is_live: bool 
    # items: rx.Var[List[item]] = rx.Var()
    
    async def check_live(self) -> bool:
        self.is_live = await live(USER)
    

    
  
        
        
        
