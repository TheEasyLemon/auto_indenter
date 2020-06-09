import re
INDENT = "\t"


def format_code(cd):
    """(str) => (str)
    Takes a string of JS code and removes all the tabs, newlines,
    and spaces (except for single spaces)
    :param cd:
    :return:
    """
    no_tabs = "".join(cd.split("\t"))
    no_newlines = "".join(no_tabs.split("\n"))
    no_spaces = re.sub(r"\s{2,}", "", no_newlines)

    return no_spaces


def auto_indent(cd):
    """ (str) => (str)
    Takes a string of JS code and correctly indents it.
    :param cd:
    :return str:
    """
    # removes all tabs and newlines
    start = format_code(cd)

    # eventual return string
    formatted = ""

    # keeps track of indent level
    indent_level = 0
    # keeps track of whether or not we're in a for block
    in_for = False
    # keeps track of whether or not we're declaring a case block
    decl_case = False

    for i, char in enumerate(start):
        # recognize the starting of for blocks
        if char == "f" and start[i:i+4] == "for(":
            in_for = True
        # recognize ending of for blocks
        if char == ")" and in_for:
            in_for = False

        # recognize in case block
        if (char == "c" and start[i:i+4] == "case") or (char == "d" and start[i:i+7] == "default"):
            decl_case = True
        # indent once we enter the case block
        if char == ":" and decl_case:
            decl_case = False
            indent_level += 1
            formatted += char
            formatted += "\n" + INDENT * indent_level
            continue
        # recognize ending of case block
        if char == "k" and start[i-4:i+1] == "break":
            indent_level -= 1

        if char == ";" and not in_for:
            # insert newline after semicolon and appropriate indentation
            formatted += char
            formatted += ("\n" + INDENT * indent_level)
            continue
        if char == "{":
            indent_level += 1
            # insert space before left bracket
            formatted += " " + char
            # insert newline after left bracket
            formatted += "\n" + INDENT * indent_level
            continue
        if char == "}":
            indent_level -= 1

            # insert newline before and after right bracket
            formatted += "\n" + INDENT * indent_level
            formatted += char

            # If there is a right paren, semicolon, or comma after, don't make another newline
            # first condition necessary to avoid IndexError
            if (i + 1) < len(start) and start[i + 1] not in ");,}":
                formatted += "\n" + INDENT * indent_level
            continue

        formatted += char

    return formatted


if __name__ == "__main__":
    with open("code.txt", "r") as file:
        CODE = file.read()
    complete = auto_indent(CODE)
    print(complete)
