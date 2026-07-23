from thefuck import CONFUSABLES


def test_maps_to_single_ascii_chars():
    for wrong, right in CONFUSABLES.items():
        assert wrong != right
        assert len(right) == 1
        assert ord(right) < 128  # the target is plain ASCII


def test_known_entries():
    assert CONFUSABLES["（"] == "("
    assert CONFUSABLES["，"] == ","
    assert CONFUSABLES["“"] == '"'
