# Two not Tounch (2nt) Printer

Gets Numpy array of Two Not TOuch Boards. Create SVG graphics of game
boards.

## Game board

Is a 10x10 Numpy matrix, like:

```python
mrx = np.array(
    [
        [1, 1, 1, 2, 2, 2, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 3, 3, 4, 4, 1, 5, 5, 5, 6],
        [3, 3, 4, 4, 4, 7, 6, 6, 5, 6],
        [4, 4, 4, 8, 7, 7, 7, 6, 6, 6],
        [4, 4, 4, 8, 7, 7, 7, 6, 9, 6],
        [4, 4, 8, 8, 7, 7, 6, 6, 9, 9],
        [4, 8, 8, 8, 9, 9, 9, 9, 9, 9],
        [4, 8, 8, 9, 9, 9, 9, 9, 9, 9],
        [8, 8, 8, 9, 10, 10, 10, 9, 9, 9],
    ]
)
return mrx - 1  # Az eredeti mátrix 0009 tartalmaz0
```

0..9 ten different sets of disjunct shapes.

## SVG graphics

Constants:

 - `BS`: Border space, between printed 10x10 squares.
 - `SW`: Square Width, one cell element of the 10x10 squares.
 
Dynamic:

 - `HG`: Height, nr of 10x10 puzzles in a column
 - `WI`: Width,  nr of 10x10 puzzles in a row
 
Overall `HG` x `WI` pieces of puzzles processed.

Canvas size:

 - `X`: `BS + (BS + 10 * SW) * WI`
 - `Y`: `BS + (BS + 10 * SW) * HG`
 
## Cell borders

 - Outer borders are thick lines
 - Inter shape lines are thin
 - Borders between different shpaes are thick

