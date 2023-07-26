"""Represents a input load class"""

from typing import Protocol

class PluginInterface(Protocol):
    """Basic representation of a input load class"""

    def load_data_source(self, file_name: str) -> str:
        """Load raw data source from file"""
        pass

    def extract_data(self, data: str) -> list:
        """Extract text from the currently loaded file."""
        pass