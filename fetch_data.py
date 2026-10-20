"""Country lookup with helpful API failure messages."""
import requests

API_URL = "https://restcountries.com/v3.1/name/{}"


def fetch_country(name, timeout=5, base_url=API_URL):
    """Fetch one country; return (data, error message)."""
    try:
        response = requests.get(base_url.format(requests.utils.quote(name)), timeout=timeout)
        if response.status_code == 404:
            return None, "Country not found (404). Check the name and try again."
        if 500 <= response.status_code <= 599:
            return None, "Country service is temporarily unavailable (server error). Try later."
        if response.status_code != 200:
            return None, f"Country service returned HTTP {response.status_code}. Try again later."
        try:
            data = response.json()
        except ValueError:
            return None, "Country service returned invalid JSON. Try again later."
        if not isinstance(data, list) or not data or not isinstance(data[0], dict):
            return None, "Country service returned an unexpected response."
        return data[0], None
    except requests.exceptions.Timeout:
        return None, "The country service took too long to respond. Try again."
    except requests.exceptions.ConnectionError:
        return None, "Could not reach the country service. Check your internet connection and try again."
    except requests.exceptions.RequestException:
        return None, "The request failed. Please try again later."


def format_country(country):
    """Format a saved country dictionary without making any network calls."""
    common = country.get("name") or {}
    name = common.get("common", "Unknown") if isinstance(common, dict) else "Unknown"
    capitals = country.get("capital") or []
    capital = ", ".join(capitals) if isinstance(capitals, list) and capitals else "Unknown"
    population = country.get("population")
    population = f"{population:,}" if isinstance(population, (int, float)) else "Unknown"
    currencies = country.get("currencies") or {}
    currency = ", ".join(currencies.keys()) if isinstance(currencies, dict) and currencies else "Unknown"
    fields = [("Country", name), ("Capital", capital), ("Population", population),
              ("Region", country.get("region") or "Unknown"), ("Currency", currency)]
    width = max(len(label) for label, _ in fields)
    return "\n".join(f"{label:<{width}} : {value}" for label, value in fields)


def main():
    name = input("Enter a country name: ").strip()
    if not name:
        print("Please enter a country name.")
        return
    data, error = fetch_country(name)
    print(error if error else format_country(data))


if __name__ == "__main__":
    main()
