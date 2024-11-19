import pytest
from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.pytest import create_app_fixture
from shiny.run import ShinyAppProc

from app import UIState, helper

app = create_app_fixture("../app.py")


@pytest.mark.parametrize(
    ("x", "y", "expected"),
    [
        [1, 1, 2],
        [2, 6, 8],
    ],
)
def test_add_numbers(x, y, expected):
    assert helper(x, y) == expected


def test_UIState():
    x = 5
    state = UIState(n=x)
    assert state.n == x


def test_app_basic(page: Page, app: ShinyAppProc):
    page.goto(app.url)
    txt = controller.OutputText(page, "txt")
    slider = controller.InputSlider(page, "n")
    slider.set("20")
    txt.expect_value("n*2 + 4 is 44")
