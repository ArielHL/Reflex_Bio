import reflex as rx 
from own.styles import styles



def icon_button_radit ( icon:str, 
                        url:str, 
                        is_external:bool=True,
                        color:str=styles.BUTTON_BASE_COLOR,
                        variant:str = "ghost",
                        text:str="",
                        size:str="1",
                        **kwargs
                             )-> rx.Component:
                
               
    return rx.link( 
                rx.button(
                    rx.icon(icon,size=16),
                    text,
                    variant=variant,
                    color_scheme=color,
                    size=size,
                    **kwargs
                ),
                href=url,
                is_external=is_external     
            )

                