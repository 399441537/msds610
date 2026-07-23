import codecs

import thefuck  # noqa: F401 - importing registers the "thefuck" codec
from thefuck.codec import _transform


def test_decode_replaces_fullwidth():
    raw = "（a，b）".encode("utf-8")
    assert codecs.decode(raw, "thefuck") == "(a,b)"


def test_transform_is_length_preserving():
    s = "（）“”，：；"
    assert len(_transform(s)) == len(s)


def test_ascii_is_untouched():
    assert _transform("x = (1, 2)") == "x = (1, 2)"
