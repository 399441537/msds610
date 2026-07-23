"""A source codec that rewrites full-width / Chinese punctuation to ASCII.

This is the Python analog of C's ``#define``. A file opts in with a
``# coding: thefuck`` cookie on its first or second line; Python then hands the
file's raw bytes to this codec to decode, and we swap the confusable
characters for their ASCII look-alikes *before* the parser ever sees them. The
file on disk is never modified -- the substitution happens only in memory at
load time.
"""

from __future__ import annotations

import codecs
from encodings import utf_8

from thefuck.confusables import CONFUSABLES

# Each confusable maps 1 char -> 1 ASCII char, so line/column offsets in
# tracebacks stay correct after the substitution.
_TABLE = str.maketrans(CONFUSABLES)


def _transform(text: str) -> str:
    return text.translate(_TABLE)


def decode(data: bytes, errors: str = "strict") -> tuple[str, int]:
    text, length = utf_8.decode(data, errors)
    return _transform(text), length


class IncrementalDecoder(codecs.BufferedIncrementalDecoder):
    def _buffer_decode(self, data, errors, final):
        if not final:
            return "", 0
        text, length = utf_8.decode(data, errors)
        return _transform(text), length


class StreamReader(utf_8.StreamReader):
    def decode(self, data, errors="strict"):  # type: ignore[override]
        return decode(data, errors)


_utf8 = codecs.lookup("utf-8")

_CODEC_INFO = codecs.CodecInfo(
    name="thefuck",
    encode=_utf8.encode,
    decode=decode,
    incrementalencoder=_utf8.incrementalencoder,
    incrementaldecoder=IncrementalDecoder,
    streamreader=StreamReader,
    streamwriter=_utf8.streamwriter,
)


def _search(name: str):
    if name.replace("-", "_").lower() == "thefuck":
        return _CODEC_INFO
    return None


_registered = False


def register() -> None:
    """Register the ``thefuck`` source codec. Safe to call multiple times."""
    global _registered
    if not _registered:
        codecs.register(_search)
        _registered = True


# Register on import so that `import thefuck.codec` (e.g. from the .pth file)
# is enough to activate the codec.
register()
