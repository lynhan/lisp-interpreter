"""
# lisp_parser.py

Example output:
Enter code to parse:

(first (list 1 (+ 2 3) 9))
['first', ['list', '1', ['+', '2', '3'], '9']]
"""



log = False

def p(*arg):
    global log
    if log: print(" ".join(str(a) for a in arg))



def treat(string):
    """
    Split input by () and spaces.

    param:
    (first (list 1 (+ 2 3) 9))

    return:
    ['(', 'first', '(', 'list', '1', '(', '+', '2', '3', ')', '9', ')', ')']
    """
    tokens = []
    word = []
    for index, char in enumerate(string):
        if char in ["(", ")"]:
            tokens.append(char)
        elif string[index+1] in [" ", ")"]:
            word.append(char)
            tokens.append("".join(word))
            word = []
        elif char != " ":
            word.append(char)
    return tokens



def build_ast(tokens):
    p("\n", len(tokens), "TOKENS\n")
    """
    param:
    ['(', 'first', '(', 'list', '1', '(', '+', '2', '3', ')', '9', ')', ')']

    return:
    ["first", ["list", 1, ["+", 2, 3], 9]]
    """
    ast, index = parse(tokens, 0)
    return ast



def parse(tokens, index):
    """
    Recursively populate results.
    """
    result = []

    while index < len(tokens):

        p("\nINDEX", index, "TOKEN", tokens[index])
        token = tokens[index]

        if token == "(" and result:
            p("recursing")
            sub_tree, index = parse(tokens, index)
            result.append(sub_tree)
            p("returned", result)

        elif token == ")":
            return result, index

        elif token != "(":
            result.append(token)
            p("appended", result)

        else:
            p("skipping ( at index", index)

        index += 1

    return result, index



def interpret(ast):
    pass



def main():
    print("Enter code to parse:\n")
    string = input()
    ast = build_ast(treat(string))
    print(ast)
    interpret(ast)



if __name__ == "__main__":
    main()
