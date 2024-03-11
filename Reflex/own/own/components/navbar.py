import reflex as rx 
from own.styles import styles
from own.styles.colors import TextColor as TextColor
from own.styles.colors import Color as Color
from own.routes import Route
from own.components.ant_components import float_button
from own.utils import logo



def navbar(live:bool=False) -> rx.Component:
    return rx.chakra.hstack(
                rx.chakra.link(
                    rx.chakra.hstack(
                        rx.chakra.avatar(
                            name="Your Names",
                            size="md",
                            color=TextColor.BODY.value,
                            bg=Color.CONTENT.value,
                            src=logo,
                            padding='2px',
                            border="2px solid",
                            border_color=Color.PRIMARY.value,
                            margin_right=styles.Size.VERY_SMALL.value,
                            ),
                        rx.chakra.span('Your',color=Color.PRIMARY.value),
                        rx.chakra.span('Name',color=Color.PRIMARY.value),
                        style=styles.navbar_title_style,
                        
                    ),
                    href=Route.INDEX.value,
                ),
                rx.chakra.spacer(),
                rx.desktop_only(
                  rx.chakra.link(
                        "My Projects",
                        href=Route.PROJECTS.value,
                        color=Color.PRIMARY.value,
                        margin_right=styles.Size.BIG.value,
                    ),
                    # rx.chakra.link(
                    #     "My Posts",
                    #     href=Route.POSTS.value,
                    #     color=Color.PRIMARY.value,
                    #     margin_right=styles.Size.BIG.value,
                    # ),    
                    rx.chakra.link(
                        "About me",
                        href=Route.ABOUT.value,
                        color=Color.PRIMARY.value,
                        margin_right=styles.Size.BIG.value,
                        ), 
                ),
                rx.mobile_and_tablet(
                    rx.chakra.menu(
                        rx.chakra.menu_button(
                            rx.chakra.icon(tag='hamburger',color=Color.PRIMARY.value, width=styles.Size.BIG.value, height=styles.Size.BIG.value)
                            ),
                        rx.chakra.menu_list(
                            rx.chakra.menu_item(
                                        rx.chakra.link(
                                            "My Projects",
                                            href=Route.PROJECTS.value                                         
                                            ), 
                                        background_color=Color.CONTENT.value,
                                        color='white', 
                                        ),
                            # rx.chakra.menu_item(
                            #             rx.chakra.link(
                            #                 "My Posts",
                            #                 href=Route.POSTS.value                                         
                            #                 ), 
                            #             background_color=Color.CONTENT.value,
                            #             color='white', 
                            #             ),
                            rx.chakra.menu_divider(),
                            rx.chakra.menu_item(
                                rx.chakra.link(
                                    "About Me",
                                    href=Route.ABOUT.value
                                ),
                                background_color=Color.CONTENT.value, 
                                color='white', 
                                ),
                            background_color=Color.CONTENT.value

                        ),
                        style=styles.navbar_title_style,
                        placement="left-start",
                    ),
                ),
                position='sticky',
                bg=Color.NAVBAR.value,
                width='100%',
                padding_x=styles.Size.BIG.value,
                padding_y=styles.Size.DEFAULT.value,
                z_index='100',
                top='0px',
                display='flex',
                align_items='center',
            )    