import reflex as rx

# Común
def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='en'")


preview = ""
logo = "/icons/Logo.webp"
    
_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"name": "twitter:site", "content": "@ariellimes"}
]

# ******************************************************* Index ******************************************************* #

index_title = "Ariel Limes | Connecting People with Technology"
index_description = "Facilitating Connectivity: Empowering Communities through Technological Solutions."

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
index_meta.extend(_meta)

# ******************************************************* Projects ******************************************************* #

projects_title = "Projects | Ariel Limes"
projects_description = "Listado de proyectos realizados"

projects_meta = [
    {"name": "og:title", "content": projects_title},
    {"name": "og:description", "content": projects_description},
]
projects_meta.extend(_meta)

# ******************************************************* About ******************************************************* #

about_title = "About Me | Ariel Limes"
about_description = "Who I am"

about_meta = [
    {"name": "og:title", "content": about_title},
    {"name": "og:description", "content": about_description},
]
about_meta.extend(_meta)