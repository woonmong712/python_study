// playwright/tests/example.spec.ts

import { test, expect } from "@playwright/test";

test("basic test" , async ({ page })=> {
    // playwright 공식페이지로 이동 - goto(url)
    await page.goto("https://palywright.dev/");

    // 페이지에서 클래스를 찾고, 변수에 저장 - locator("태그 or 클래스 or ID")
    const title = page.locator(".navbar__inner .navbar__title");

    // 저장된 부분에 "Playwright"문자열이 들어있는지 테스트 하고 결과 보여주기 - expect
    await expect(title).toHaveText("Playwright");
});
