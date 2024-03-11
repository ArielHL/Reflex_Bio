import reflex as rx 
from own.components.navbar import navbar
from own.views.header import header
from own.views.index_links import index_links
from own.components.footer import footer
from own.styles import styles
from own import utils as utils
from own.api.api import repo, live
from own.states.pages_state import PageState
from own.states.image_state import ImageSwapState



@rx.page(
    title=utils.index_title,
    description=utils.index_description,
    image=utils.logo,
    meta=utils.index_meta,
    
    
    
)
def index () -> rx.Component:
    return  rx.chakra.box (
                utils.lang(),
                navbar(live=PageState.is_live),
                rx.chakra.center(
                    rx.chakra.vstack(
                        header(details=True),
                        index_links(),
                        max_width=styles.MAX_WIDTH,
                        width='100%',
                        margin_y=styles.Size.BIG.value,
                        padding=styles.Size.BIG.value,
                    )
                ),
                footer()   
         )
    
    
