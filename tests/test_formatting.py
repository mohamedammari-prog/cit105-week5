from fetch_data import format_country

SAMPLE = {
    "name": {"common": "Tunisia"}, "capital": ["Tunis"],
    "population": 12000000, "region": "Africa", "currencies": {"TND": {"name": "Tunisian dinar"}}
}


def test_formats_saved_country():
    output = format_country(SAMPLE)
    assert "Tunisia" in output
    assert "Tunis" in output
    assert "12,000,000" in output
    assert "Africa" in output
    assert "TND" in output


def test_missing_fields_do_not_crash():
    output = format_country({"name": {"common": "Example"}})
    assert "Example" in output
    assert output.count("Unknown") == 4
