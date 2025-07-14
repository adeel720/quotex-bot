from pyppeteer import launch

async def main():
    browser = await launch(headless=False, args=['--no-sandbox', '--disable-dev-shm-usage'])
    page = await browser.newPage()
    await page.goto('https://market-qx.pro/en/sign-in')
    await page.type('input[name="email"]', 'adeelhr2024@outlook.com')
    await page.type('input[name="password"]', 'Malik@S123')  # اپنا پاس ورڈ یہاں لگاؤ
    await page.click('.modal-sign__block-button')
    await page.waitForNavigation()
    await page.goto('https://market-qx.pro/en/trade')
    print("پیج لوڈ ہو گیا:", await page.url())
    html = await page.content()
    print("پیج کا ابتدائی HTML:", html[:500])  # صرف 500 حروف دکھائیں
    await browser.close()

import asyncio
asyncio.run(main())
