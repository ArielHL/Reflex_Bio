import reflex as rx 
from own.styles import styles
from own.styles.colors import Color , TextColor
from own.components.icon_button_radit import icon_button_radit



def link_cards_inline( header:str,
                        footer:str,
                        body:str,
                        image:str,
                        url:str = None,
                        is_external:bool=True) -> rx.Component:
    
        return rx.hstack(
                    rx.vstack(
                        rx.box(
                            rx.chakra.text( header,
                                            font_size=[styles.Size.DEFAULT.value,
                                                       styles.Size.LARGE.value], 
                                            color=TextColor.HEADER.value,
                                            margin_bottom=styles.Size.VERY_SMALL.value
                            ),
                            rx.chakra.text( footer,
                                            font_size=[styles.Size.MEDIUM.value,
                                                       styles.Size.DEFAULT.value], 
                                            color=TextColor.BODY.value
                            ),
                            rx.chakra.text( body,
                                            font_size=[styles.Size.SMALL.value,
                                                       styles.Size.MEDIUM.value], 
                                            color=TextColor.BODY.value
                            ),
                        ),
                        rx.hstack(
                            icon_button_radit(
                                text="Go to Project",
                                icon="link",
                                url=url, 
                                size="1",
                                stroke_width=3
                            ),
                        ),
                        padding=styles.Size.MEDIUM.value,
                        width=["53%","70%"]
                    ),
                    rx.flex(
                        rx.image(
                                src=image,
                                alt=header,
                                style=styles.image_style,
                                width="100%",
                                height="auto",
                                max_width="100%",
                                max_height=["135px","160px"] 
                        ),
                        width=["47%","30%"]
                    ),
                    spacing='2',
                    justify_content="space-between",
                    align_item="center",
                    width="100%",
                    border_radius=styles.Size.MEDIUM.value,
                    box_shadow="5px 5px 5px 5px rgba(58, 62, 93, 0.2)",
                    background_color=Color.BUTTON_COLOR.value,
                    max_height=["135px","160px"]
        )
                