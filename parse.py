# parser.py


log = False

def p(*arg):
    global log
    if log: print(" ".join(str(a) for a in arg))


class Parse:

    @staticmethod
    def prepare(string):
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
                whole = "".join(word)
                tokens.append(int(whole) if whole.isdigit() else whole)
                word = []
            elif char != " ": # single char like 1
                word.append(char)
        return tokens


    @staticmethod
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
                sub_tree, index = Parse.parse(tokens, index)
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


    @staticmethod
    def build_ast(tokens):
        """
        param:
        ['(', 'first', '(', 'list', '1', '(', '+', '2', '3', ')', '9', ')', ')']

        return:
        ["first", ["list", 1, ["+", 2, 3], 9]]
        """
        p("\n", len(tokens), "TOKENS\n")
        ast, index = Parse.parse(tokens, 0)
        return ast
