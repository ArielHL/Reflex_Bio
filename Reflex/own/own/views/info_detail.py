import reflex as rx 
from own.components.link_button import link_button
from own.components.title import title
from own.components.link_cards import link_cards
from own.components.info_stack import info_stack
from own.components.box_container import box_container
from own.components.icon_button import icon_button
from own.styles import styles 
import own.constants as const
from own.routes import Route



def info_detail () -> rx.Component:
    return rx.chakra.vstack(
        title(text="{ Experience : My Past and Present }"),
        rx.chakra.vstack(
            *[
                info_stack(
                    title=item['title'],
                    description=item['description'],
                    body=item['body'],
                    image=item['image']
                   
                )
                for item in const.EXPERIENCE_LIST
            ],
            direction="column",
            width="100%",
            justify_content="start",
            spacing=styles.Size.MEDIUM.value,
            ),
            width='100%',
        )
    