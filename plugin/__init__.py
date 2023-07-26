from abc import ABC, abstractmethod

class PluginInterface(ABC):

    @abstractmethod
    def load_data_source(self, file_name: str) -> str:
        """Load raw data source from file"""
        pass

    @abstractmethod
    def extract_data(self, data: str) -> list:
        """Extract text from the currently loaded file."""
        pass

