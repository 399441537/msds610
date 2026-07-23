"""thefuck — a private practice package for MSDS610."""

from thefuck.confusables import CONFUSABLES
from thefuck.codec import register

# Importing the package registers the source codec.
register()

__version__ = "0.4.0"
__all__ = ["CONFUSABLES", "register", "__version__"]
