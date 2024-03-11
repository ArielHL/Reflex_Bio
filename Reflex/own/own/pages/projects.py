import reflex as rx 
from own.components.navbar import navbar
from own.views.header import header
from own.views.projects_links import projects_links
from own.components.footer import footer
from own.styles import styles
from own import utils as utils
from own.routes import Route
from own.states.pages_state import PageState
from own.views.custom_header import custom_header



@rx.page(
    route=Route.PROJECTS.value,
    title=utils.projects_title,
    description=utils.projects_description,
    image=utils.preview,
    meta=utils.projects_meta,
    
)
def projects () -> rx.Component:
    return  rx.chakra.box (
                utils.lang(),
                navbar(PageState.is_live),
                rx.chakra.center(
                    rx.chakra.vstack(
                        custom_header(image="/images/projects_back_image.webp"),
                        projects_links(),
                        max_width=styles.MAX_WIDTH,
                        width='100%',
                        margin_y=styles.Size.BIG.value,
                        padding=styles.Size.BIG.value,
                    )
                ),
                footer()   
         )
    
    
