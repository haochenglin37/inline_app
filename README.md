# inline_app

This repository contains a simple helper script for automating bookings on
[inline.app](https://inline.app/).

## `auto_booking.py`

A command-line tool that uses Selenium to open the booking page, fill in the
form and submit it. The script supports:

* specifying desired date, time and number of guests
* optional backup date if the preferred date fails
* delaying execution until a specific time (`--start-after`)
* custom CSS selectors loaded from a JSON config (`--selector-config` and
  `--profile`)

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
    --start-after "2025-09-05 23:55" \
    --selector-config selectors.example.json \
    --profile LESbsL9bsZtLcRHgaeq
```

Inspect the booking page and update the selectors in the JSON file. An
example configuration is provided in `selectors.example.json` with a profile
named `LESbsL9bsZtLcRHgaeq` corresponding to
`https://inline.app/booking/-LESbsL9bsZtLcRHgaeq/-LESbsL9bsZtLcRHgaer?language=zh-tw`.
