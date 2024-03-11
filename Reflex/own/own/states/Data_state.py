import reflex as rx
from own.modules.database import dataItem
from own.api.api import live, get_data





class DataState(rx.State):
    
    data_list: list[dataItem]

    async def get_posts(self):
        
        data =  await get_data()
        
        if data:
            self.data_list = data
        else:
            self.data_list = [dataItem(title="No data found", 
                                       image="https://kinsta.com/es/wp-content/uploads/sites/8/2018/08/divertido-404-page.jpg",
                                       url="No data found")]

        

