# interpret.py


class Tools:

    # for consistency when called in assign
    from operator import add

    @staticmethod
    def get_list(*arg):  # variable len
        tokens = []
        for a in arg:
            if isinstance(a, list):
                tokens.append(interpret(a))
            else:
                tokens.append(a)
        return tokens

    @staticmethod
    def get_first(*arg):
        """
        Called with sliced list containing list
        Param unpacking results in tuple containing list
        """
        subarray = arg[0]
        return subarray[1]  # arg[0] is cmd


# assign is probably better as
# interpret param or Tools member var
# instead of global

assign = {
"first" : Tools.get_first,
"list": Tools.get_list,
"+" : Tools.add
}


def interpret(arg):
    """
    Does not unpack arg since
    first called with list of tokens.

    Unpacks arg passed to assigned function
    since slice returns a single list.
    """
    global assign
    cmd = arg[0]
    return assign[arg[0]](*arg[1:])
