import codecs

import simple_eda  # noqa: F401 - importing registers the source codec
from simple_eda.codec import _transform


def test_decode_replaces_fullwidth():
    raw = "（a，b）".encode("utf-8")
    assert codecs.decode(raw, "simple_eda") == "(a,b)"


def test_thefuck_alias_still_works():
    raw = "（a，b）".encode("utf-8")
    assert codecs.decode(raw, "thefuck") == "(a,b)"


def test_transform_is_length_preserving():
    s = "（）“”，：；"
    assert len(_transform(s)) == len(s)


def test_ascii_is_untouched():
    assert _transform("x = (1, 2)") == "x = (1, 2)"
