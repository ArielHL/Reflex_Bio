import reflex as rx 
from own.styles import styles
from own.pages.index import index
from own.pages.projects import projects
from own.pages.about import about
from own.api.api import repo, live, get_data
from own.pages.posts import posts



app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLES
    
    )

app.api.add_api_route("/api/repo", repo)
app.api.add_api_route("/api/data", get_data)


