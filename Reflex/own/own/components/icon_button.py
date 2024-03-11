import reflex as rx 
from own.styles import styles



def icon_button (title:str,
                 image:str,
                )-> rx.Component:
    return rx.chakra.button(
                    rx.chakra.hstack(
                        rx.chakra.image(
                            src=image,
                            width=styles.Size.DEFAULT.value,
                            height=styles.Size.DEFAULT.value,
                            margin=styles.Size.MEDIUM.value,
                            alt=title
                        ),
                        rx.chakra.text(title,style=styles.button_title_style,
                            align_items='start',
                            margin=styles.Size.ZERO.value,
                            ),
                        width='100%',
                        justify_content='start',
                    ),
                    height=styles.Size.DEFAULT.value,
                    border='none !important',
            )

                