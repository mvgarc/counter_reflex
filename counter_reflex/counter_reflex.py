import reflex as rx

from rxconfig import config


class State(rx.State):
    count: int = 0



app = rx.App()
app.add_page(index)
