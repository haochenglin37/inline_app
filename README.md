# inline_app

This repository contains a simple helper script for automating bookings on
[inline.app](https://inline.app/).

## `auto_booking.py`

A command-line tool that uses Selenium to open the booking page, fill in the
form and submit it. The script supports:

* specifying desired date, time and number of guests
* optional backup date if the preferred date fails
* delaying execution until a specific time (`--start-after`)

### Requirements

* Python 3.8+
* `selenium` package
* ChromeDriver installed and available on `PATH`

### Usage

```bash
pip install selenium
python auto_booking.py \
    --url "https://inline.app/booking/..." \
    --date 2025-09-06 \
    --time 18:30 \
    --people 2 \
    --backup-date 2025-09-07 \
    --start-after "2025-09-05 23:55"
```

Update the CSS selectors in `auto_booking.py` after inspecting the booking page,
as they are placeholders in this example.
