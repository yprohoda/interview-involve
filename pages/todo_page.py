from time import sleep

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TodoPage(BasePage):
    URL = "https://todomvc4tasj.herokuapp.com/"
    HEADER = By.ID, "header"
    TEXT_FIELD = By.ID, "new-todo"
    NOTE = By.ID, "todo-list"
    TO_DO_COUNT = By.XPATH, '//*[@id="todo-count"]'
    DESTROY_BTN = By.CSS_SELECTOR, ".destroy"
    CREATED_NOTE = By.XPATH, '//*[@id="todo-list"]/li/div/input'
    CHECK_BTN = By.CLASS_NAME, "toggle"
    CHECK_ALL_BTN = By.ID, "toggle-all"
    ACTIVE_NOTES_TAB_LINK = "#/active"
    COMPLETED_NOTES_TAB_LINK = "#/completed"
    ALL_NOTES_TAB_LINK = "#/"
    CLEAR_COMPLETED_BTN = By.ID, "clear-completed"

    def go_to_page(self):
        self.browser.get(self.URL)
        header = self.wait_visible(self.HEADER)
        assert header.is_displayed()

    def enter_note(self, text):
        text_field = self.wait_clickable(self.TEXT_FIELD)
        text_field.send_keys(text)
        sleep(1)
        text_field.send_keys(Keys.RETURN)
        sleep(0.5)

    def get_text_note(self):
        return self.get_text(self.NOTE)

    def get_count_text(self):
        return self.get_text(self.TO_DO_COUNT)

    def hover_mouse_on_the_note(self):
        self.move_to_element(self.NOTE)

    def delete_note(self):
        self.move_to_element_and_click(self.DESTROY_BTN)

    def get_empty_note_text(self):
        return self.get_empty_text(self.NOTE)

    def click_on_note_to_edit(self):
        self.move_to_element_with_offset(self.CREATED_NOTE)
        self.double_click()

    def enter_text_clicked_note(self, text):
        active_el = self.switch_to_active_element()
        active_el.send_keys(text)
        active_el.send_keys(Keys.RETURN)

    def mark_first_note(self):
        el = self.wait_clickable(self.CHECK_BTN)
        el.click()

    def check_all_notes(self):
        el = self.wait_clickable(self.CHECK_ALL_BTN)
        el.click()

    def open_active_notes(self):
        el = self.find_link(self.ACTIVE_NOTES_TAB_LINK)
        el.click()

    def open_completed_notes(self):
        el = self.find_link(self.COMPLETED_NOTES_TAB_LINK)
        el.click()

    def open_all_notes(self):
        el = self.find_link(self.ALL_NOTES_TAB_LINK)
        el.click()

    def click_clear_completed_btn(self):
        el = self.wait_clickable(self.CLEAR_COMPLETED_BTN)
        el.click()
