import reflex as rx 
from own.components.link_button import link_button
from own.components.title import title
from own.components.link_cards import link_cards
from own.components.link_cards_outline import link_cards_outline
from own.components.box_container import box_container
from own.components.icon_button import icon_button
from own.styles import styles 
import own.constants as const
from own.routes import Route



def index_links () -> rx.Component:
    return rx.chakra.vstack(
        title(text='{ Projects : Cool Stuff to use }',url=Route.PROJECTS.value,arrow=True),
        rx.chakra.responsive_grid(
            *[
                link_cards_outline(
                    header=item['header'],
                    body=item['body'],
                    footer=item['footer'],
                    image=item['image'],
                    url=item['url'],
                )
                for item in const.PROJECTS_LIST
            ],
            columns=[2,4],
            width="100%",
            spacing=styles.Size.SMALL.value,
            justify_content="center",
            align_item="center"
        ), 
        title("{ Skills : Let's get Technical }"),
        rx.chakra.responsive_grid(
            box_container(
                "Frontend",
                icon_button(
                    title="React",
                    image="/icons/react.png",  
                ),
                icon_button(
                    title="Javascript",
                    image="/icons/js.png",
                )
            ),
            box_container(
                "Backend",
                icon_button(
                    title="NodeJS",
                    image="/icons/nodejs.svg",
                ),
                icon_button(
                title="Python",
                image="/icons/python.svg",
            )
            ),
            box_container(
                "Data Science",
                icon_button(
                    title="TensorFlow",
                    image="/icons/tensorflow.png",
                )
            ),
            box_container(
                "Databases",
                icon_button(
                    title="MongoDB",
                    image="/icons/mongodb.svg",
                ),
                icon_button(
                title="SQL",
                image="/icons/SQL.png",
            )
            ),
            columns=[2,3,4],
            width="100%",
            spacing=styles.Size.SMALL.value,
            justify_content="center",
            align_item="center"
           
        ),
        title(" { Certified : Sure! }"),
        rx.chakra.responsive_grid(

            *[
                link_cards(
                    header=item['header'],
                    body=item['body'],
                    url=item['url'],
                    background=item['image'],
                    footer=item['footer'],
                    scroll=False
                )
                for item in const.CERTIFICATIONS_LIST
            ],
    
            columns=[2,4],
            width="100%",
            spacing=styles.Size.SMALL.value,
            justify_content="center",
            align_item="center"
        ),
        title("{ What next?: Get in Touch }"),
        link_button(
            title="Email",
            body=const.EMAIL,
            image="/icons/email.svg",
            url=f"mailto:{const.EMAIL}"
        ),
        width='100%',
        spacing=styles.Size.DEFAULT.value,
        
    )