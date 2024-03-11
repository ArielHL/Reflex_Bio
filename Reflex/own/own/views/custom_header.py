import reflex as rx 
from own.components.link_icon import link_icon
from own.components.info_text import info_text
from own.styles import styles
from own.components.title import title
from own.styles.colors import TextColor as TextColor
from own.styles.colors import Color as Color    
import own.constants as const
import datetime
from own.states.index_state import ColorState 
from own.states.focus_state import ImageFocusState



def custom_header (image:str) -> rx.Component:
    return rx.chakra.flex(
        rx.chakra.image(src=image,
                 width=["100%","75%"],
                 height=["200px","280px","280px","380px"],
                 box_shadow="0px 0px 3px 3px",
                 border_radius=styles.Size.MEDIUM.value,
                 
                 ),
        width="100%",
        align_items="center",
        justify_content="center",
        margin_bottom=styles.Size.DEFAULT.value,
        



    )
        
    