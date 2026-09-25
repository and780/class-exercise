import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def inspect_file(filepath_str):
    path = Path(filepath_str)

    if not path.is_file():
        #Log the error before raising the exception
        logger.error(f"File not found: {filepath_str}")
        raise FileNotFoundError(f"File not found: {filepath_str}")

    return {"filename":path.name,"extension":path.suffix}


def inspect_extension(file_info):
    """Confirm that the file uses a supported text extension."""
    supported_extension = ".txt"

    # TODO 4: If file_info["extension"] does not equal
    #         supported_extension:
    #         Log an ERROR message (e.g. unsupported format).
    #         Raise ValueError.

    # TODO 5: Return file_info.

    if file_info["extension"] not in supported_extension:
            logger.error("Unsupported format")
            raise ValueError(f"{file_info["extension"]}")

    return file_info
    