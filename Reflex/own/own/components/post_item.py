import reflex as rx
from own.styles import styles
from own.modules.database import dataItem 

def post_item (item:dataItem) -> rx.Component:
    return  rx.chakra.link(
                rx.chakra.image(
                    src=item.image,
                    style=styles.image_style,
                    ),
                rx.chakra.text(
                    item.title,
                    color=styles.Color.SECONDARY.value,
                    margin_top=styles.Size.SMALL.value,
                    ),
                href=item.url,
                is_external=True,
    )