import reflex as rx 
from own.components.navbar import navbar
from own.views.header import header
from own.components.footer import footer
from own.views.info_detail import info_detail
from own.styles import styles
from own import utils as utils
from own.states.pages_state import PageState 
from own.routes import Route



@rx.page(
    route=Route.ABOUT.value,
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.index_meta,
)
def about () -> rx.Component:
    return  rx.chakra.box (
                utils.lang(),
                navbar(live=PageState.is_live),
                rx.chakra.center(
                    rx.chakra.vstack(
                        header(details=True),
                        info_detail(),
                        max_width=styles.MAX_WIDTH,
                        width='100%',
                        margin_y=styles.Size.BIG.value,
                        padding=styles.Size.BIG.value,
                    )
                ),
                footer()   
         )
    
    
