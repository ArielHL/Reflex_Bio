import reflex as rx 
from own.styles import styles
from own.styles.colors import Color , TextColor



def box_container(  text:str,
                    *children:rx.Component,
                    **kwargs
                    ) -> rx.Component:
    
        return rx.chakra.container(
                    rx.chakra.text(text,
                                   font_size= ["3vw","2vw","1.5vw"],
                                   color=TextColor.HEADER.value,
                                   margin_bottom=styles.Size.MEDIUM.value,
                                   ),
                    rx.chakra.vstack(
                        *children,
                        spacing=styles.Size.SMALL.value,
                    ),
                    padding=styles.Size.SMALL.value,
                    align="start",
                    justify="center",
                    border_radius=styles.Size.MEDIUM.value,
                    box_shadow="5px 5px 5px 5px rgba(58, 62, 93, 0.2)",
                    background_color=Color.BUTTON_COLOR.value,
                    height=["23vw","16vw","11vw"],
                    width="100%",
                    **kwargs 
                )                        
        
        
