import reflex as rx 
from own.styles import styles
from own.styles.colors import Color , TextColor



def link_cards( header:str,
                footer:str,
                body:str,
                background:str,
                scroll:bool=False,
                url:str = None,
                is_external:bool=True) -> rx.Component:
    
        return rx.chakra.link(
                        rx.chakra.card(
                                rx.chakra.text(body,
                                               font_size=["16px","13px"] if scroll else ["12px","13px"]),
                                header = rx.chakra.text(header,
                                                        font_size=["18px","20px"] if scroll else ["15px","20px"]),
                                footer = rx.chakra.text(footer,
                                                        font_size=["13px","12px"] if scroll else ["10px","12px"]),
                                align="start",
                                justify="center",
                                background_image=f"url({background})",
                                style=styles.card_style if scroll else styles.card_style_no_scroll,
                                height= styles.RESPONSIVE_HEIGHT,
                                
                        ),
                        href=url if url else "#",
                        is_external=is_external if url else False,

                )