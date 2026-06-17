class PyForgeError(Exception):
    """Base exception for PyForge."""


class ValidationError(PyForgeError):
    """Raised when validation fails."""


class ConfigurationError(PyForgeError):
    """Raised when configuration is invalid."""