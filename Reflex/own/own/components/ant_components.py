import reflex as rx
from own.styles.colors import Color


class FloatButton(rx.Component):
    library = "antd"
    tag = "FloatButton"
    icon: rx.Var[rx.chakra.Image]
    href: rx.Var[str]
    target = "_blank"
    badge = {"dot": True, "color": Color.PRIMARY.value}
    


float_button = FloatButton.create