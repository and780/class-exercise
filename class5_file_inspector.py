import argparse
import logging
import sys
from pathlib import Path
from class5_file_utils import inspect_file, inspect_extension

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Inspect a text file"
    )
    parser.add_argument(
        "--input",
        "-i",
        required=True,
        help="Path to a .txt file"
    )
    args = parser.parse_args()

    # TODO 1: Call inspect_file() inside a try block.

    # TODO 2: Catch FileNotFoundError.
    #         Log an ERROR message (e.g. file not found), and 
    #         exit with sys.exit(1).

    # TODO 3: Call inspect_extension() inside a separate try block.

    # TODO 4: Catch ValueError.
    #         Log an ERROR message (e.g. unsupported format), and 
    #         exit with sys.exit(1).

    # TODO 5: Log an INFO message containing the
    #         file name and extension.
    try:
        file_info = inspect_file(args.input)
    except FileNotFoundError as error:
        logging.error(f"Unable to find:{error}")
        sys.exit(1)

    # 3 & 4: Inspect extension and catch ValueError
    try:
        inspect_extension(file_info)
    except ValueError:
        logging.error("Unsupported format")
        sys.exit(1)

    # 5: Log file name and extension
    path = Path(args.input)

    logging.info(
        f"File name: {path.name}, extension: {path.suffix}"
    )

if __name__ == "__main__":
    main()