import argparse
import logging

import tnp.boardprinter as bp


def parse_log_level(level: str) -> str:
    """Function to validate and return the log level"""
    aliases = {"d": "DEBUG", "i": "INFO", "w": "WARNING", "e": "ERROR", "c": "CRITICAL"}
    return aliases.get(level.lower(), level.upper())


def config_logging(level: str) -> None:
    """Configure logging

    Args:
        level (str): Log level
    """
    # Logger
    # create logger with 'tnt'
    logger = logging.getLogger("tnp")
    logger.setLevel(level)
    # create file handler which logs even debug messages
    fh = logging.FileHandler("log/tnp.log", mode="w")
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.WARNING)
    # create formatter and add it to the handlers
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)


def main() -> None:
    """Main entry point for SVG creation"""
    parser = argparse.ArgumentParser(
        description="Two not touch puzzle printer",
        epilog="Creates SVG representation of puzzles.",
    )
    parser.add_argument(
        "-c", "--col", type=int, default=1, help="Nr of puzzles in a column"
    )
    parser.add_argument(
        "-r", "--row", type=int, default=1, help="Nr of puzzles in a row"
    )
    parser.add_argument(
        "--log", type=parse_log_level, default="INFO", help="Set the logging level"
    )

    args = parser.parse_args()
    config_logging(level=args.log)
    bp.main(height=int(args.row), width=int(args.col))


if __name__ == "__main__":
    main()
