from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("#")
    page.get_by_role("link", name="직원").click()
    page.get_by_placeholder("아이디").click()
    page.get_by_placeholder("아이디").fill("qa")
    page.get_by_placeholder("아이디").press("Tab")
    page.get_by_placeholder("패스워드").fill("1!")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_placeholder("패스워드").press("Enter")
    page.get_by_placeholder("아이디").click()
    page.get_by_placeholder("아이디").fill("qa")
    page.get_by_placeholder("아이디").press("Tab")
    page.get_by_placeholder("패스워드").fill("1!")
    page.get_by_placeholder("패스워드").press("Enter")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("link", name="코드 받기").click()
    page.locator("#authkey").click()
    page.locator("#authkey").fill("000000")
    page.get_by_role("link", name="확인").click()
    page.get_by_role("link", name="닫기").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
