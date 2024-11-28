import reflex as rx

from rxconfig import config


class State(rx.State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1



app = rx.App()
app.add_page(index)
