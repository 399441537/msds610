"""Minimal setup shim.

All package metadata lives in ``pyproject.toml``. This file exists only to
install ``thefuck.pth`` into site-packages so the source codec auto-registers
at interpreter startup (the piece declarative config can't express portably).
"""

import os
import sysconfig

from setuptools import setup

# site-packages, expressed relative to the wheel "data" scheme root so it lands
# in the right place in whatever environment pip builds/installs into.
_paths = sysconfig.get_paths()
_site_packages = os.path.relpath(_paths["purelib"], _paths["data"])

setup(data_files=[(_site_packages, ["thefuck.pth"])])
