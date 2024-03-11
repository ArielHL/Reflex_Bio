import reflex as rx


def custom_float_button(url:str,src:str) -> rx.Component:
    return rx.box(
        rx.link(
                rx.image(
                    src=src,
                    width="50px",
                    height="50px",
                    borderRadius="50%",
                    ),
            href=url,
            is_external=True,
        ),
        style={
            "position": "fixed",
            "bottom": "20px",
            "right": "20px",
            }
        )