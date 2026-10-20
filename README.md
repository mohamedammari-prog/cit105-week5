# CIT 105 Module 5 — Public API Consumption

A Python command-line country lookup using the free REST Countries API (no API key).

- **Endpoint:** `https://restcountries.com/v3.1/name/{name}`
- **Extracted fields:** country common name, capital, population, region, currency codes.
- **Dependencies:** Python 3.10+, `requests`, `pytest`.

## Run

```bash
python -m pip install -r requirements.txt
python fetch_data.py
python -m pytest -q
```

Enter a country name such as `Tunisia`. The program uses `requests.get(..., timeout=5)`, checks status before reading JSON, handles malformed data, and formats missing fields as `Unknown`. `fetch_country` performs the network call; `format_country` performs presentation without networking.

## Failure Modes

The following outputs were **actually captured** on October 20, 2026 in the development environment. Outbound access to REST Countries was unavailable here, so these captures demonstrate the connection-error handler but **do not yet establish** the required HTTP bad-path or timeout behavior. Repeat those experiments on a machine with working internet and replace the respective captures before submission.

### Bad path attempt (network prevented HTTP response)

Called `fetch_country('Tunisia', base_url='https://restcountries.com/v3.1/not-a-real-path/{}')`:

```text
Could not reach the country service. Check your internet connection and try again.
```

### Tiny timeout attempt (network failure happened first)

Called `fetch_country('Tunisia', timeout=0.000001)`:

```text
Could not reach the country service. Check your internet connection and try again.
```

### Network unavailable

Called `fetch_country('Tunisia')` with the development environment's outbound API access unavailable:

```text
Could not reach the country service. Check your internet connection and try again.
```

### Local verification

```text
2 passed in 0.03s
```

## AI disclosure

ChatGPT assisted in writing the code, tests, and README. The local tests were run in the development environment. The failure demonstrations above were captured there, and the remaining two network-dependent demonstrations still need to be repeated on a machine with internet access.
