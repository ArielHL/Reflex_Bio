import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font, FontWeigth
from own.states.image_state import ImageSwapState

# Constants
MAX_WIDTH="1100px"
RESPONSIVE_HEIGHT = ["55vw","42vw","37vw","24vw"]
BUTTON_BASE_COLOR = "blue"

# Sizes
class Size(Enum):
    ZERO = "0px !important"
    VERY_SMALL = "0.2em"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    DEFAULT_PLUS = "1.2em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"
    
STYLESHEETS =[
   "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&dipslay=swap" ,
   "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"

]

# styles
BASE_STYLES = {
    # Global styles
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeigth.LIGHT.value,
    "background_color":Color.BACKGROUND.value,
    
    # Specific styles
    rx.chakra.Heading: {
    "color": TextColor.HEADER.value,
    "font_family": Font.TITLE.value,
    "font_weight": FontWeigth.MEDIUM.value,

    },
    rx.chakra.Button: {
        "width": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color": Color.BUTTON_COLOR.value,
        "border": f"3px solid {Color.BUTTON_BORDER_COLOR.value}",
        "white_space": "normal",
        "text_align": "left",
        
        "_hover": {
            "background_color": Color.SECONDARY.value
        }
    
    },
    
    rx.chakra.Card: {
        "padding": Size.VERY_SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "white_space": "normal",
        "text_align": "left",
        "transition":  "background-color 0.3s",
        "overflow": "hidden",
        
        "_hover": {
            "background_color": Color.SECONDARY.value,
        }   
    },
    

    rx.chakra.Link:{
        "text_decoration":"none",
        "_hover":{}
    },
    
}

navbar_title_style = dict(
   font_family = Font.LOGO.value,
   font_wight = FontWeigth.MEDIUM.value,
   font_size = Size.LARGE.value,
   color=Color.PRIMARY.value
)

title_style = dict(
    width="100%",
)

button_title_style = dict(
    font_family = Font.TITLE.value,
    font_wight = FontWeigth.LIGHT.value,
    font_size = Size.MEDIUM.value,
    color = TextColor.HEADER.value
)

button_body_style = dict(
    font_family = Font.DEFAULT.value,
    font_wight = FontWeigth.LIGHT.value,
    font_size = Size.MEDIUM.value,
    color=TextColor.BODY.value,
)

background_image = dict(
        background_size= "cover",
        background_position= "center",
        background_blend_mode= "multiply",
       
        )


card_container_style = dict(
    display="flex",
    overflow_x="auto",
    overflow_y="hidden",
    spacing=Size.MEDIUM.value,
    scroll_snap_type="x mandatory",
    webkit_overflow_scrolling="touch",
    scroll_behavior="smooth",

)
    
card_style = dict(
    display="flex",
    scroll_snap_align="start",
    flex_shrink="0",
    background_size= "cover",
    background_position= "center",
    background_blend_mode= "multiply",


)


card_style_no_scroll = dict(
    display="flex",
    background_size= "cover",
    background_position= "center",
    background_blend_mode= "multiply",
    width="100%",
    max_height="250px",

)


image_style = dict(
    display="flex",
    width="250px",
    height="250px",
    border_radius=Size.DEFAULT.value,
    object_fit="cover",
    object_position="center",
    
)

image_swap_style = {
        "width":"240px",
        "height":"220px",
        "border_radius":"5%",
}