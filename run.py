# run.py


from parse import Parse
from interpret import interpret


def main():
    print("\nEnter code to parse:")
    string = input()
    ast = Parse.build_ast(Parse.prepare(string))
    print("\nAbstract syntax tree:", ast, sep="\n")
    print("\nResult:", interpret(ast))


if __name__ == "__main__":
    main()
