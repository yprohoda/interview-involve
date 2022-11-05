import pytest
from pages.todo_page import TodoPage


@pytest.fixture(autouse=True)
def env(capsys):
    page = TodoPage()
    page.go_to_page()

    yield page

    page.browser.close()


def test_create_one_note(env):
    """Create note with letter diff case, symbols, numbers"""
    TEXT = 'My password is "xqzsssX59!qEobe7s"'

    page = env
    page.enter_note(TEXT)

    assert page.get_text_note() == TEXT
    assert page.get_count_text() == "1 item left"


@pytest.mark.xfail
def test_create_long_note(env):
    """Create note with letter diff case, symbols, numbers"""
    page = env
    TEXT = "1234567890123456789012345678901234567890"
    page.enter_note(TEXT)

    assert page.get_text_note() == "123456789012345678901234567890123456\n7890"
    assert page.get_count_text() == "1 item left"


def test_create_several_notes(env):
    """Create 3 notes with letter diff case, symbols, numbers"""
    page = env
    page.enter_note("DS^Nm9rQM5U89g")
    page.enter_note("F$eqtmG8hJENy!")
    page.enter_note("@N$m*k9#@ycreb")

    assert page.get_text_note() == "DS^Nm9rQM5U89g\nF$eqtmG8hJENy!\n@N$m*k9#@ycreb"
    assert page.get_count_text() == "3 items left"


def test_delete_note(env):
    """Create and delete note"""
    TEXT = 'My password is "5$yb5#nLLNq3bU"'
    page = env

    page.enter_note(TEXT)
    page.hover_mouse_on_the_note()
    page.delete_note()

    assert page.get_empty_note_text() == ""


def test_edit_note(env):
    """Create and edit note"""
    TEXT = 'My password is "5$yb5#nLLNq3bU"'
    page = env

    page.enter_note(TEXT)
    page.click_on_note_to_edit()
    page.enter_text_clicked_note(page.URL)

    assert page.get_text_note() == page.URL


def test_mark_note(env):
    """Create note and check it"""

    TEXT = 'Мой пароль "5$yb5#nLLNq3bU"'
    page = env

    page.enter_note(TEXT)
    page.mark_first_note()
    assert page.get_text_note() == TEXT
    assert page.get_count_text() == "0 items left"


def test_mark_all_notes(env):
    """Create 3 notes and check them all"""
    page = env
    page.enter_note("DS^Nm9rQM5U89g")
    page.enter_note("F$eqtmG8hJENy!")
    page.enter_note("@N$m*k9#@ycreb")

    assert page.get_text_note() == "DS^Nm9rQM5U89g\nF$eqtmG8hJENy!\n@N$m*k9#@ycreb"
    assert page.get_count_text() == "3 items left"

    page.check_all_notes()
    assert page.get_count_text() == "0 items left"


def test_clear_completed(env):
    """Create, check and clear completed note"""

    TEXT = 'Мой пароль "5$yb5#nLLNq3bU"'
    page = env

    page.enter_note(TEXT)
    page.mark_first_note()
    page.click_clear_completed_btn()

    assert page.get_empty_note_text() == ""


def test_clear_not_all_notes(env):
    """Create 2 notes, check first note, and clear completed notes"""

    page = env

    page.enter_note('Мой пароль1')
    page.enter_note('Мой пароль2')
    page.mark_first_note()
    page.click_clear_completed_btn()

    assert page.get_text_note() == 'Мой пароль2'
    assert page.get_count_text() == "1 item left"


def test_tabs_selection(env):
    """Create, check note, and move to different tabs"""

    TEXT = 'Мой пароль "5$yb5#nLLNq3bU"'
    page = env

    page.enter_note(TEXT)
    page.mark_first_note()

    page.open_active_notes()
    assert page.get_empty_note_text() == ""
    assert page.get_count_text() == "0 items left"

    page.open_completed_notes()
    assert page.get_text_note() == TEXT
    assert page.get_count_text() == "0 items left"

    page.open_all_notes()
    assert page.get_text_note() == TEXT
    assert page.get_count_text() == "0 items left"

# to run parallel browsers: pytest -n auto
