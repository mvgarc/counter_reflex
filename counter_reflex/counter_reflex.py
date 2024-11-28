import reflex as rx

from rxconfig import config


class State(rx.State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

def index():
    return rx.hstack(
        rx.button(
            "Decrement",
            color_scheme="ruby"
            on_click=State.decrement,
        ),
        rx.heading(State.count, font_size="2em")
    )



app = rx.App()
app.add_page(index)
