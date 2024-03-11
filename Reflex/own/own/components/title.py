import reflex as rx 
from own.styles import styles


def title(text:str,url:str=None,arrow:bool=False) -> rx.Component:
    return rx.chakra.hstack(
                rx.chakra.heading(
                    text,
                    font_size=['1.1em','1.5em'],
                    width="auto",
                   
                    
                ),
                rx.cond(
                    arrow,
                    rx.chakra.link(
                        rx.chakra.hstack(
                            rx.chakra.icon(tag="arrow_forward", 
                                    size=styles.Size.LARGE.value, 
                                    color=styles.Color.PRIMARY.value),
                                    border="solid",
                                    border_color=styles.Color.PRIMARY.value,
                                    border_radius=styles.Size.SMALL.value,
                                    padding=styles.Size.SMALL.value,
                                    
                        ),                    
                        href=url if url else "#",
                    )
                ),
                justify_content="start",
                align_items="center",
                width="100%",
                spacing=styles.Size.DEFAULT.value,
                padding_top=styles.Size.DEFAULT.value,
                margin_bottom=styles.Size.DEFAULT.value
             
            ) 


