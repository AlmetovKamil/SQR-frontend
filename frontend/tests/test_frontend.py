import pytest
from streamlit.testing.v1 import AppTest

at = AppTest.from_file("../app/main.py").run()


def test_selected_rating():
    at.sidebar.slider[0].set_value(0.45).run()

    assert at.sidebar.slider[0].value == 0.45


def test_selected_genre():
    at.sidebar.selectbox[0].select_index(0)

    assert at.sidebar.selectbox[0].value == 'All'


def test_selected_book():
    at.button(key='10000').run()

    assert at.title != "Book Review Platform (BRP)"
