"""SVG converter for boards
"""
import logging

from tnp import __version__

# create logger
BP_LOGGER = logging.getLogger("tnp.boarprinter")


def main(height:int=1, width:int=1, iname:str ="data/tnt.np", oname:str = '/tmp/boards.svg') -> None:
    BP_LOGGER.info(
        "TNP (Two Not Touch Printer) %s -> %s for %d x %d %s starting...", iname, oname, height, width, __version__
    )


if __name__ == "__main__":
    main()
