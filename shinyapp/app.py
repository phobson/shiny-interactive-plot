from dataclasses import dataclass
from typing import TypeVar

from shiny import App, Inputs, Outputs, Session, reactive, render, ui

from utils.misc import add_numbers, try_to_read


@dataclass
class UIState:
    n: int

    @classmethod
    def from_ui(cls, user_in: Inputs):
        return cls(n=try_to_read(user_in.n, 0) or 0)


T = TypeVar("T", int, float)

app_ui = ui.page_fluid(
    ui.panel_title("Hello Shiny!"),
    ui.input_slider("n", "N", 0, 100, 20),
    ui.output_text_verbatim("txt"),
)


def helper(x: T, y: T) -> T:
    return add_numbers(x, y)


def server(user_in: Inputs, output: Outputs, session: Session):
    @reactive.calc
    def get_state():
        return UIState.from_ui(user_in)

    @render.text
    def txt():
        state = get_state()
        result = helper(state.n * 2, 4)
        return f"n*2 + 4 is {result}"


app = App(app_ui, server)
