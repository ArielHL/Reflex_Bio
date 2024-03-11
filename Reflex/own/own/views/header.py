import reflex as rx 
from own.components.link_icon import link_icon
from own.components.info_text import info_text
from own.components.icon_button_radit import icon_button_radit
from own.styles import styles
from own.components.title import title
from own.styles.colors import TextColor as TextColor
from own.styles.colors import Color as Color    
import own.constants as const
import datetime
from own.states.index_state import ColorState 
from own.states.focus_state import ImageFocusState
from own.states.image_state import ImageSwapState

def experience_finance() -> int:
    return datetime.date.today().year - 1999

def experience_data() -> int:
    return datetime.date.today().year - 2019

def header (details=True) -> rx.Component:
    return rx.chakra.vstack(
                    rx.chakra.flex(
                        rx.chakra.flex(
                            rx.chakra.vstack(
                                rx.chakra.heading(
                                    ImageSwapState.active_message,
                                    style=styles.button_body_style,
                                    align="center",
                                    width="100%",
                                    margin_bottom=styles.Size.MEDIUM.value,
                                ),
                            
                                rx.chakra.image(
                                    src=ImageSwapState.active_src,
                                    width="240px",
                                    height="220px",
                                    border_radius="5%",
                            
                                ),
                                on_click=ImageSwapState.swap_images,
                                align_items="center",
                                justify_content="center",
                            ),
                            rx.chakra.flex(
                                rx.chakra.heading(
                                    "Ariel Limes",
                                    size='lg',
                                    on_click=ColorState.next_color,
                                    color=ColorState.color,
                                    _hover={"cursor": "pointer"}
                                ),
                                rx.chakra.text(
                                    "@arielimes",
                                    margin_top=styles.Size.ZERO.value,
                                    color=Color.PRIMARY.value,
                                ),
                                rx.chakra.hstack(
                                        icon_button_radit(
                                            icon="github",
                                            url=const.GITHUB_URL,
                                            variant="ghost",
                                            is_external=True,
                                        ),
                                        icon_button_radit(
                                            icon="linkedin",
                                            url=const.LINKEDIN_URL,
                                            variant="ghost",
                                            is_external=True,
                                        ),
                                        icon_button_radit(
                                            icon="file-text",
                                            url=const.RESUME_URL,
                                            variant="ghost",
                                            is_external=True,
                                            color="sky",
                                            
                                        ),
                                        spacing=styles.Size.LARGE.value,
                                        margin_top=styles.Size.SMALL.value,
                                ),
                                direction="column",
                                aling_items="start",
                                width=["225px","40%"],
                                margin=styles.Size.MEDIUM.value,
                                
                            ),
                            width="100%",
                            direction=["column","row"],
                            align="center",

                        ),
                        rx.cond(
                            details,
                            rx.chakra.flex(
                                info_text(f"0{experience_data()}+", "Years of experience in Data Science"),
                                rx.chakra.spacer(),
                                info_text(f"{experience_finance()}+", "Years of experience in Finance"),
                                rx.chakra.spacer(),
                                info_text("10+", "Projects"),
            
                                direction="column",
                                padding=styles.Size.VERY_SMALL.value,
                                margin=styles.Size.SMALL.value,
                                width="100%",
                            )
                        ),
                        spacing=styles.Size.MEDIUM.value,   
                        direction=["column","row"],
                        width="100%",
                        justify="space-around",
                        align="center",
                    ),
                    rx.cond(
                        details,
                            rx.vstack(
                                title('{ Self: About Me }'),
                                rx.chakra.text(
                                    f"""
                                    I am a professional in Data Science with {experience_finance()} years of experience in Finance and {experience_data()} years in Data Science. 
                                    Currently, I work as a freelance full-stack developer in ReactJS, Node.JS, Django, and Reflex. 
                                    As well as a Data Scientist in Machine Learning and Deep Learning projects, mainly in NLP.
                                    """,
                                    color=TextColor.BODY.value,
                                    font_size=styles.Size.DEFAULT.value,
                                    padding="2px"
                                )
                            )
                    ),
                    spacing=styles.Size.LARGE.value,
                    width="100%",
                    align_items="start",
                    margin_bottom=styles.Size.MEDIUM.value,
                    # padding_x=styles.Size.MEDIUM.value,
            )
      
        
    