"""SVG converter for boards"""

import logging

import numpy as np
import numpy.typing as npt
import svg

from tnp import __version__

# create logger
BP_LOGGER = logging.getLogger("tnp.boarprinter")
BS = 20  # Border space, between printed 10x10 squares.
SW = 10  # Square Width, one cell element of the 10x10 squares.
SB = 5  # stroke_width for border
SI = 1  # stroke_width for inner lines

class Puzzle:
    """
    Definiction of one game board

    Representation is a 10x10 matrix with elements 0..9
    """

    board: npt.NDArray[np.int_]
    xpos:int
    ypos:int
    def __init__(self, x: int, y: int, boardnr: int) -> None:
        """Init a puzzle

        Args:
            x (int): X position
            y (int): Y position within the sheet
            boardnr (int): One of the boards from the array
        """
        self.xpos = x
        self.ypos = y

    def tosvg(self) -> list:
        """Returns a list of SVG elements representing the puzzle

        Returns:
            list: SVG rectanles and lines
        """
        rli =[svg.Rect(
                x=BS + (BS + 10 * SW) * self.xpos, y=BS + (BS + 10 * SW) * self.ypos,
                width=10 * SW, height=10 * SW,
                stroke="black",
                fill="transparent",
                stroke_width=SB,
            )]
        return rli


class Sheet:
    """Class representing the SVG sheet of puzzles"""

    height: int
    width: int
    canvas: svg.SVG

    def __init__(self, height: int, width: int) -> None:
        """SVG Sheet object

        Args:
            height (int): nr of puzzlesd in a column
            width (int): nr of puzzlesd in a row
        """
        self.height = height
        self.width = width
        self.canvas = svg.SVG(
            width=BS + (BS + 10 * SW) * self.width,
            height=BS + (BS + 10 * SW) * self.height,
            elements=[],
        )
        self.logger = logging.getLogger("tnp.boarprinter.Sheet")


def main(
    height: int = 1,
    width: int = 1,
    iname: str = "data/tnt.np",
    oname: str = "/tmp/boards.svg",
) -> None:
    BP_LOGGER.info(
        "TNP (Two Not Touch Printer) %s -> %s for %d x %d %s starting...",
        iname,
        oname,
        height,
        width,
        __version__,
    )


if __name__ == "__main__":
    main()
