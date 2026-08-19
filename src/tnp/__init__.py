# src/tnt/__init__.py
import importlib.metadata

try:
    __version__ = importlib.metadata.version("tnp")  # the [project] name
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.0.0"  # Fallback for an uninstalled source tree

print(f"Version:{__version__}")
