import reflex as rx 
from own.styles import styles
from own.styles.colors import Color , TextColor



def link_cards_outline( header:str,
                    footer:str,
                    body:str,
                    image:str,
                    url:str = None,
                    is_external:bool=True) -> rx.Component:
    
        return rx.link(
                rx.chakra.responsive_grid(
                    rx.chakra.image(src=image,
                                    alt=header,
                                    object_fit="cover",
                                    height=["22vw","16vw","12vw"],
                                    width="100%",
                                    border_radius=styles.Size.MEDIUM.value,),
                    rx.chakra.responsive_grid(
                        rx.chakra.text(header,font_size= ["1.0em","1.0em","1.2em"],color=TextColor.HEADER.value),
                        rx.chakra.text(body,font_size= ["0.7em","0.7em","1em"],color=TextColor.BODY.value, margin_top=styles.Size.SMALL.value),
                        rx.chakra.text(footer,font_size= ["0.6em","0.6em","0.8em"],color=TextColor.BODY.value, margin_top=styles.Size.MEDIUM.value),
                        margin_top=styles.Size.SMALL.value,
                    ),
                    padding=styles.Size.SMALL.value,
                    border_radius=styles.Size.MEDIUM.value,
                    box_shadow="5px 5px 5px 5px rgba(58, 62, 93, 0.2)",
                    background_color=Color.BUTTON_COLOR.value,
                    height= styles.RESPONSIVE_HEIGHT,
                    width="100%",
                ),
                href=url if url else "#",
                is_external=is_external if url else False
                )