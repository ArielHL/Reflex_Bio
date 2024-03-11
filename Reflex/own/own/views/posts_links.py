import reflex as rx
from own.components.post_item import post_item
from own.modules.database import dataItem 

from own.styles import styles 
import own.constants as const
from own.api.api import live, get_data
from own.states.pages_state import PageState



def posts_links (data:list[dataItem]) -> rx.Component:
    
   return rx.chakra.box(
           
            rx.cond(
                data,
                rx.chakra.responsive_grid(
                    rx.foreach(
                        data,
                        post_item
                    ),
                    columns=[2,4],
                    spacing=styles.Size.MEDIUM.value,
                    margin_top=styles.Size.BIG.value,
                )
            ),
          
        )

