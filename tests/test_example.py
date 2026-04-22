"""
Simple Playwright test — visits example.com and asserts the page title.
Run with:  pytest tests/test_example.py --headed
"""
import re
from playwright.sync_api import Page, expect


def test_example_page_title(page: Page):
    page.goto("https://example.com")
    expect(page).to_have_title(re.compile("Example Domain"))


def test_example_heading(page: Page):
    page.goto("https://example.com")
    heading = page.locator("h1")
    expect(heading).to_have_text("Example Domain")
