class PyForgeError(Exception):
    """
    Base exception for all PyForge exceptions.
    """


class ConfigurationError(PyForgeError):
    """
    Raised when configuration is invalid.
    """


class ValidationError(PyForgeError):
    """
    Raised when request validation fails.
    """