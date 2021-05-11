<p align="center"><img src="imgs/aoc18.png"></p>

**2018 | [2019](https://github.com/gosiqueira/advent-of-code-2019) | [2020](https://github.com/gosiqueira/advent-of-code-2020)**

Here lies my solutions to [Advent of Code 2018](https://adventofcode.com/2018), an Advent calendar full of programming puzzles from December 1st all the way to Christmas.

2018 was my first year participating, and although I did follow the challenges every day for the first half or so, unfortunately I ended up not having the time nor discipline to finish it before December 25th. Thus, I decided to complete it before the start of the 2019 edition, and post each day as if it was released exactly a year after.

## Inputs and Outputs

All inputs are read from `inputs\input-XX.txt`, with `XX` being the zero-padded day. As per the creator's request, they are not available in this repository and should be downloaded directly from the event website.

The only outputs for all days are exactly what should be pasted in the puzzle answer textbox, followed by the total runtime of both parts combined (via Python's `time.time()`), no more and no less. The only exception is when the answer is drawn on a grid-like formation, then that is printed instead of OCR. In some cases, helpful debugging code or other verbose messages are simply commented out, and can be manually toggled to better understand the code inner workings.

## Implementation Goals

The solutions posted here are cleaned-up versions of the actual code written when aiming for the leaderboards. For all solutions, the main implementation goals were, in descending order:

* **Readability:** Clean, readable, self-explanatory and commented code above all else.
* **Input Generalization:** Should work not only for my input but for anyone's, with some assumptions made about it, which are noted when appropriate.
* **Modularity:** Avoid duplicate code where possible, allowing for easy modification by making heavy use of classes and functions. 
* **Speed:** Use efficient algorithms, keeping runtime reasonably low without extreme micro-optimizations.
* **Minimal Imports:** Refrain from `import`s besides utilities (`sys`, `time`) and basic standard libraries (`math`, `itertools`, `collections`). When the knowledge of functions and structures are considered vital to the problem solution (graphs, trees, linked lists, union-find, etc.), reimplement them.

## Thanks!

Many thanks to [Eric Wastl](http://was.tl/), who creates Advent of Code, as well as to the amazing community over at [/r/adventofcode](https://www.reddit.com/r/adventofcode/)!
Also to my friend [Gabriel Kanegae](http://github.com/KanegaeGabriel), who motiovated me to start Advent of Code and I+ stole this repo description. 😁