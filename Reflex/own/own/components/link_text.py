import reflex as rx 
from own.styles import styles


def link_text(text:str,url:str,is_extenal:bool=True) -> rx.Component:
    return rx.chakra.link( 
            rx.chakra.heading(
            text,
            size='md',
            style=styles.title_style,
            ),
            href=url,
            is_external=is_extenal
    )

