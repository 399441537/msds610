"""Confusable punctuation: full-width / Chinese characters vs. ASCII.

The Python cousin of the classic C prank ``#define true false``: characters
that *look* almost identical but are different code points. When a Chinese IME
is left in full-width mode, these sneak into source code and cause
``SyntaxError`` even though the line looks perfectly fine on screen.

This module is just data (no functions yet): a mapping from each confusable
character to the ASCII character it is usually mistaken for.
"""

# Chinese / full-width punctuation  ->  the ASCII character it looks like
CONFUSABLES = {
    "（": "(",   # U+FF08 full-width left parenthesis
    "）": ")",   # U+FF09 full-width right parenthesis
    "［": "[",   # U+FF3B full-width left square bracket
    "］": "]",   # U+FF3D full-width right square bracket
    "｛": "{",   # U+FF5B full-width left curly brace
    "｝": "}",   # U+FF5D full-width right curly brace
    "“": '"',   # U+201C left double quotation mark
    "”": '"',   # U+201D right double quotation mark
    "‘": "'",   # U+2018 left single quotation mark
    "’": "'",   # U+2019 right single quotation mark
    "，": ",",   # U+FF0C full-width comma
    "。": ".",   # U+3002 ideographic full stop
    "、": ",",   # U+3001 ideographic comma
    "：": ":",   # U+FF1A full-width colon
    "；": ";",   # U+FF1B full-width semicolon
    "！": "!",   # U+FF01 full-width exclamation mark
    "？": "?",   # U+FF1F full-width question mark
    "％": "%",   # U+FF05 full-width percent sign
    "＝": "=",   # U+FF1D full-width equals sign
    "＋": "+",   # U+FF0B full-width plus sign
    "－": "-",   # U+FF0D full-width hyphen-minus
    "＊": "*",   # U+FF0A full-width asterisk
    "／": "/",   # U+FF0F full-width solidus
    "＜": "<",   # U+FF1C full-width less-than sign
    "＞": ">",   # U+FF1E full-width greater-than sign
    "　": " ",   # U+3000 ideographic (full-width) space
}
