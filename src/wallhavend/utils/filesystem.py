"""Filesystem utilities for file and directory operations."""

from pathlib import Path


def ensure_directory(directory: str | Path) -> Path:
    """
    Ensure a directory exists, creating it if necessary.
    
    Args:
        directory: Path to the directory
    
    Returns:
        Path object for the directory
    
    Raises:
        OSError: If directory creation fails
    """
    path = Path(directory)
    path.mkdir(parents=True, exist_ok=True)
    return path


def directory_exists(directory: str | Path) -> bool:
    """
    Check if a directory exists.
    
    Args:
        directory: Path to check
    
    Returns:
        True if directory exists, False otherwise
    """
    return Path(directory).exists() and Path(directory).is_dir()


def save_binary_file(filepath: str | Path, data: bytes) -> None:
    """
    Save binary data to a file.
    
    Args:
        filepath: Path where the file should be saved
        data: Binary data to write
    
    Raises:
        IOError: If file writing fails
    """
    path = Path(filepath)
    
    # Ensure parent directory exists
    path.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        with open(path, "wb") as f:
            f.write(data)
    except IOError as e:
        raise IOError(f"Failed to write file {filepath}: {e}") from e


def get_output_directory(base_path: str = "./out") -> Path:
    """
    Get the output directory path, creating it if necessary.
    
    Args:
        base_path: Base path for output directory
    
    Returns:
        Path object for output directory
    """
    return ensure_directory(base_path)
