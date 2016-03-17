####lisp interpreter for rc pairing interview

`run.py` calls parse and interpret on input string.

works on simple inputs and not rigorously tested

example output from `python3 run.py`

    Enter code to parse:
    (first (list 1 (+ 2 3) 9))

    Abstract syntax tree:
    ['first', ['list', 1, ['+', 2, 3], 9]]

    Result: 1
