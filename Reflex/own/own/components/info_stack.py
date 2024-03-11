import reflex as rx
from own.components.icon_button_radit import icon_button_radit 
from own.styles import styles
from own.styles.colors import Color , TextColor



def info_stack( title:str,
                description:str,
                body:str,
                image:str,
                url:str = None,
                is_external:bool=True) -> rx.Component:
    
        return rx.hstack(
                    rx.vstack(
                        rx.mobile_only(
                            rx.flex(
                                rx.image(
                                        src=image,
                                        alt=title,
                                        style=styles.image_style,
                                        width="100%",
                                       
                                ),
                            width="100%"
                            )   
                        ),
                        rx.icon("code",size=16,color="white"),
                        rx.box(
                            rx.chakra.text( title,
                                            font_size=[styles.Size.DEFAULT_PLUS.value,
                                                       styles.Size.LARGE.value], 
                                            color=TextColor.HEADER.value,
                                            margin_bottom=styles.Size.VERY_SMALL.value
                            ),
                            rx.chakra.text( description,
                                            font_size=[styles.Size.DEFAULT.value,
                                                       styles.Size.DEFAULT.value], 
                                            color=TextColor.BODY.value,
                                            margin_bottom=styles.Size.SMALL.value
                            ),
                            rx.chakra.text( body,
                                            font_size=[styles.Size.MEDIUM.value,
                                                       styles.Size.MEDIUM.value], 
                                            color=TextColor.BODY.value
                            ),
                        ),
                        padding=styles.Size.MEDIUM.value,
                        width="100%"
                    ),
                    rx.tablet_and_desktop(
                        rx.flex(
                            rx.image(
                                    src=image,
                                    alt=title,
                                    style=styles.image_style,
                                    width="100%",
                                    height="165px"
                            ),
                            width="100%"
                        )
                    ),
                    spacing='2',
                    justify_content="space-between",
                    align_item="center",
                    width="100%",
                    border_radius=styles.Size.MEDIUM.value,
                    box_shadow="5px 5px 5px 5px rgba(58, 62, 93, 0.2)",
                    background_color=Color.BUTTON_COLOR.value,
                    
        )