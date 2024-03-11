import reflex as rx 
import datetime
from own.styles import styles
from own.styles.colors import TextColor as TextColor
import own.constants as const
from own.components.ant_components import float_button
from own.components.float_button import custom_float_button


year = datetime.datetime.today().year

def footer() -> rx.Component:
    return rx.chakra.box(

                rx.chakra.flex(
                    rx.chakra.image(
                            src='/images/DeepBlueLogo.png',
                            height=styles.Size.VERY_BIG.value,
                            weight=styles.Size.VERY_BIG.value,       
                            alt='Logotipo de Ariel Limes' 
                            ),
                    rx.chakra.vstack(
                        rx.chakra.link(
                                f'© 2014-{year} DEEPBLUE BY Ariel Limes V3.',
                                href="",
                                is_external=True,
                                font_size=styles.Size.DEFAULT.value,
                                color=TextColor.BODY.value,
                                ), 
                        rx.chakra.link(
                             rx.chakra.hstack(
                                rx.chakra.image(
                                    src="/icons/github.svg",
                                    height=styles.Size.LARGE.value,
                                    weight=styles.Size.LARGE.value,
                                ),        
                                rx.chakra.text(
                                    'Building Software with ♥ from Madrid to the World.',
                                    font_size=styles.Size.DEFAULT.value,
                                    margin_top=styles.Size.ZERO.value,
                                    color=TextColor.BODY.value,
                                    ),
                            ),
                            href=const.REPO_URL,
                            is_external=True,
                        ),
                        padding=styles.Size.MEDIUM.value,
                        ),
                        custom_float_button(
                            src="/icons/whatsapp.png",
                            url=const.WHATSAPP_URL
                        ),
                    direction=['column', 'row'],
                    justify_content='center',
                    align_items='center',
                    margin_y=styles.Size.BIG.value,
                    color=TextColor.FOOTER.value,
                    width='100%'
                ),
       
             )
    