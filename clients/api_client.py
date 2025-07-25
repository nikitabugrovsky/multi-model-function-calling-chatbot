# clients/api_client.py
from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

class ApiClient(ABC):
    """Abstract base class for API clients."""

    def __init__(self, model: str):
        """Initializes the client and any conversation history."""
        self.model = model
        self.history = []

    @abstractmethod
    def generate_content(self, user_input: str, function_execution_result: dict | None) -> None:
        """
        Sends user input to the model and stores the response.
        """
        pass

    @abstractmethod
    def get_function_call(self) -> Optional[Dict[str, Any]]:
        """
        Extracts a function call from the last response, if present.
        Should return a dictionary with 'name' and 'arguments'.
        """
        pass

    @abstractmethod
    def get_text_response(self) -> Optional[str]:
        """
        Extracts the text (non-function-call) response from the last response.
        """
        pass
