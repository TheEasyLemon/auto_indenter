import re


def auto_indent(cd):
    """ (str) => (str)
    Takes a string of characters without any tabs and newlines, and correctly indents it.
    :return str:
    """
    # removes all tabs and newlines
    no_tabs = "".join(cd.split("\t"))
    no_newlines = "".join(no_tabs.split("\n"))
    start = re.sub(r"\s{2,}", "", no_newlines)

    TABS = True

    if TABS:
        INDENT = "\t"
    else:
        INDENT = "  "

    formatted = ""

    # keeps track of indent level
    indent_level = 0
    # keeps track of whether or not we're in a for block
    in_for = False

    for i, char in enumerate(start):
        # recognize the starting of for blocks
        if char == "f" and start[i:i+4] == "for(":
            in_for = True
        # recognize ending of for blocks
        if char == ")" and in_for:
            in_for = False

        if char == ";" and not in_for:
            # insert newline after semicolon and appropriate indentation
            formatted += char
            formatted += ("\n" + INDENT * indent_level)
            continue
        if char == "{":
            indent_level += 1
            # insert newline after left bracket
            formatted += char
            formatted += " \n" + INDENT * indent_level
            continue
        if char == "}":
            indent_level -= 1

            # insert newline before and after right bracket
            formatted += "\n" + INDENT * indent_level
            formatted += char

            # If there is a right paren or semicolon after, don't make another newline
            if start[i + 1] != ")" and start[i + 1] != ";":
                formatted += "\n" + INDENT * indent_level
            continue

        formatted += char

    return formatted


if __name__ == "__main__":
    with open("code.txt", "r") as file:
        CODE = file.read()
    complete = auto_indent(CODE)
    print(complete)
