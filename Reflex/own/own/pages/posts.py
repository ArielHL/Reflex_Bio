import reflex as rx 
from own.components.navbar import navbar
from own.views.header import header
from own.views.posts_links import posts_links
from own.components.footer import footer
from own.styles import styles
from own import utils as utils
from own.routes import Route
from own.states.Data_state import DataState
from own.views.custom_header import custom_header
from own.components.title import title



@rx.page(
    route=Route.POSTS.value,
    title=utils.projects_title,
    description=utils.projects_description,
    image=utils.preview,
    meta=utils.projects_meta,
    on_load=DataState.get_posts,
    
)
def posts () -> rx.Component:
    return  rx.chakra.box (
                utils.lang(),
                navbar(),
                rx.chakra.center(
                    rx.chakra.vstack(
                        custom_header(image="/images/posts_image.webp"),
                        rx.hstack(
                            title('Posts'),
                            rx.button(
                                rx.icon("refresh-cw", size=22,stroke_width=3), 
                                on_click=DataState.get_posts, 
                                variant='ghost',
                                color_scheme='blue',
                                size='2',
                            ),
                            display='flex',
                            width='100%',
                            justify_content='space-between',
                            align_items='center',
                         ),
                        rx.divider(),
                        posts_links(DataState.data_list),
                        max_width=styles.MAX_WIDTH,
                        width='100%',
                        margin_y=styles.Size.BIG.value,
                        padding=styles.Size.BIG.value,
                    )
                ),
                footer()   
         )
    
    
