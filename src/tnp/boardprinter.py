"""SVG converter for boards"""

import logging
import random

import numpy as np
import numpy.typing as npt
import svg

from tnp import __version__

# create logger
BP_LOGGER = logging.getLogger("tnp.boarprinter")
BS = 200  # Border space, between printed 10x10 squares.
SW = 100  # Square Width, one cell element of the 10x10 squares.
SB = 5  # stroke_width for border
SI = 1  # stroke_width for inner lines


class Boards:
    """Board definitions"""

    boards: npt.NDArray[np.int_]
    boardorder: list[int]

    @classmethod
    def init(cls, iname: str) -> None:
        """Initialize boards

        Args:
            iname (str): input file name
        """
        bo = np.fromfile(file=iname, dtype=np.int_)
        nrofboards = int(bo.shape[0] / 100)
        cls.boards = bo.reshape(nrofboards, 10, 10)
        cls.boardorder = list(range(nrofboards))
        random.shuffle(cls.boardorder)

    @classmethod
    def get(cls, boardnr: int) -> tuple[int, npt.NDArray[np.int_]]:
        """Gets one board from the array

        Args:
            boardnr (int): One of the boards from the array
        Returns:
            boardnr, npt.NDArray[np.int_]: One board
        """
        boardidx = cls.boardorder[boardnr]
        return boardidx, cls.boards[boardidx]


class Puzzle:
    """
    Definiction of one game board

    Representation is a 10x10 matrix with elements 0..9
    """

    board: npt.NDArray[np.int_]
    xpos: int
    ypos: int
    boardidx: int

    def __init__(self, x: int, y: int, boardnr: int) -> None:
        """Init a puzzle

        Args:
            x (int): X position
            y (int): Y position within the sheet
            boardnr (int): One of the boards from the array
        """
        self.xpos = x
        self.ypos = y
        self.boardidx, self.board = Boards.get(boardnr)
        self.logger = logging.getLogger("tnp.boarprinter.Puzzle")

    def tosvg(self) -> list:
        """Returns a list of SVG elements representing the puzzle

        Returns:
            list: SVG rectanles and lines
        """
        rli = [
            svg.Rect(
                x=BS + (BS + 10 * SW) * (self.xpos - 1),
                y=BS + (BS + 10 * SW) * (self.ypos - 1),
                width=10 * SW,
                height=10 * SW,
                stroke="black",
                fill="transparent",
                stroke_width=SB,
            )
        ]
        self.logger.info(
            "Adding Puzzle %d,%d NR %d", self.xpos, self.ypos, self.boardidx
        )

        return rli


class Sheet:
    """Class representing the SVG sheet of puzzles"""

    height: int
    width: int
    canvas: svg.SVG

    def __init__(self, height: int, width: int) -> None:
        """SVG Sheet object creation

        Args:
            height (int): nr of puzzlesd in a column
            width (int): nr of puzzlesd in a row
        """
        self.height = height
        self.width = width
        self.logger = logging.getLogger("tnp.boarprinter.Sheet")

    def tosvg(self) -> svg.SVG:
        """Convert the sheet items to SVG"""
        self.logger.info("Adding sheet for %d x %d Puzzles", self.height, self.width)
        elms = []
        for x in range(self.width):
            for y in range(self.height):
                pu = Puzzle(x + 1, y + 1, 1)
                puzsvg = pu.tosvg()
                self.logger.debug("Adding %d,%d : %s", x, y, puzsvg)
                elms += puzsvg
        self.canvas = svg.SVG(
            width=BS + (BS + 10 * SW) * self.width,
            height=BS + (BS + 10 * SW) * self.height,
            elements=elms,
        )
        return self.canvas


def main(
    height: int = 1,
    width: int = 1,
    iname: str = "data/tnt.np",
    oname: str = "/tmp/boards.svg",
) -> None:
    """Entry point for creating a sheet of puzzles

    Args:
        height (int, optional): Nr of puzzles in a columnn. Defaults to 1.
        width (int, optional): Nr of puzzles in a row. Defaults to 1.
        iname (str, optional): Input file name of exported Numpy boards. Defaults to "data/tnt.np".
        oname (str, optional): Output filename. Defaults to "/tmp/boards.svg".
    """
    BP_LOGGER.info(
        "TNP (Two Not Touch Printer) %s -> %s for %d x %d %s starting...",
        iname,
        oname,
        height,
        width,
        __version__,
    )
    Boards.init(iname)
    sh = Sheet(height, width)
    with open(oname, "w") as f:
        f.write(str(sh.tosvg()))  # type: ignore


if __name__ == "__main__":
    main()
