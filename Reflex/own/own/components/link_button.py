import reflex as rx 
from own.styles import styles



def link_button (title:str,
                 body:str,
                 image:str,
                 url:str,
                 is_external=True) -> rx.Component:
    return rx.chakra.link( 
                rx.chakra.button(
                    rx.chakra.hstack(
                        rx.chakra.image(
                            src=image,
                            width=styles.Size.LARGE.value,
                            height=styles.Size.LARGE.value,
                            margin=styles.Size.MEDIUM.value,
                            alt=title
                ),
                        rx.chakra.vstack(
                            rx.chakra.text(title,style=styles.button_title_style),
                            rx.chakra.text(body,style=styles.button_body_style),
                            align_items='start',
                            spacing=styles.Size.SMALL.value,
                            padding_y=styles.Size.VERY_SMALL.value,
                            margin=styles.Size.ZERO.value,
                            padding_rigth=styles.Size.SMALL.value,
                            
                            ),
                        width='100%',
                        justify_content='start',
                    ),
                    background_color=styles.Color.BACKGROUND.value,
                    border="none !important",
                    width='auto',
                ),
                href=url,
                is_external=is_external,
                width='100%',
                 ) 