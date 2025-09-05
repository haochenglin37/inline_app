import argparse
import datetime as dt
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def wait_until(target: dt.datetime) -> None:
    """Block until the current time reaches ``target``."""
    while dt.datetime.now() < target:
        time.sleep(1)


def book(driver: webdriver.Remote, date: str, time_str: str, people: int) -> None:
    """Fill booking form and submit.

    The CSS selectors in this function are placeholders. Inspect the booking
    page to find the correct selectors for the date, time, people and submit
    elements.
    """
    wait = WebDriverWait(driver, 20)

    date_input = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='date']"))
    )
    date_input.clear()
    date_input.send_keys(date)

    time_input = driver.find_element(By.CSS_SELECTOR, "input[name='time']")
    time_input.clear()
    time_input.send_keys(time_str)

    people_input = driver.find_element(By.CSS_SELECTOR, "input[name='people']")
    people_input.clear()
    people_input.send_keys(str(people))

    submit_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    submit_btn.click()



def main() -> None:
    parser = argparse.ArgumentParser(description="Inline booking helper")
    parser.add_argument("--url", required=True, help="Booking page URL")
    parser.add_argument("--date", required=True, help="Preferred date YYYY-MM-DD")
    parser.add_argument("--time", required=True, help="Preferred time HH:MM")
    parser.add_argument("--people", required=True, type=int, help="Number of guests")
    parser.add_argument("--backup-date", help="Optional backup date YYYY-MM-DD")
    parser.add_argument(
        "--start-after", help="Wait until YYYY-MM-DD HH:MM before booking"
    )
    args = parser.parse_args()

    if args.start_after:
        target = dt.datetime.strptime(args.start_after, "%Y-%m-%d %H:%M")
        wait_until(target)

    options = Options()
    # Remove headless if you want to watch the browser.
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(args.url)
        try:
            book(driver, args.date, args.time, args.people)
        except Exception:
            if args.backup_date:
                book(driver, args.backup_date, args.time, args.people)
            else:
                raise
        # Add any additional confirmation logic here if needed.
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
