import reflex as rx 
from own.components.link_cards_inline import link_cards_inline
from own.components.title import title
from own.styles import styles 
import own.constants as const
from own.routes import Route


def projects_links () -> rx.Component:
    return rx.chakra.vstack(
        title('{ Projects : Take a Look}'),
        rx.chakra.vstack(
            *[  
                link_cards_inline(
                    header=item['header'],
                    body=item['body'],
                    footer=item['footer'],
                    image=item['image'],
                    url=item['url'],
                )
                for item in const.PROJECTS_LIST
            ],
            direction="column",
            width="100%",
            justify_content="start",
            spacing=styles.Size.MEDIUM.value,
            ),
        width='100%',
        spacing=styles.Size.DEFAULT.value,
    )