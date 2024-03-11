import reflex as rx 

from own.states.image_state import ImageSwapState

def image_swap() -> rx.Component:
    return rx.container(
        style=ImageSwapState.image_style,
        rx.if_(
            ImageSwapState.show_image_a,
            rx.image(src=ImageSwapState.orig_image, width="240px", height="220px", border_radius="5%"),
            rx.image(src=ImageSwapState.gpt_image, width="240px", height="220px", border_radius="5%"
            
        )
    )