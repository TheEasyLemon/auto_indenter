def auto_indent(cd):
    """ (str) => (str)
    Takes a string of characters without any tabs and newlines, and correctly indents it.
    :return str:
    """
    TABS = True

    if TABS:
        INDENT = "\t"
    else:
        INDENT = "  "

    formatted = ""

    # keeps track of indent level
    indent_level = 0

    for i, char in enumerate(cd):
        # TODO: Recognize semicolons in for blocks
        if char == ";":
            # insert newline after semicolon and appropriate indentation
            formatted += char
            formatted += ("\n" + INDENT * indent_level)
            continue
        if char == "{":
            indent_level += 1
            # insert newline after left bracket
            formatted += char
            formatted += "\n" + INDENT * indent_level
            continue
        if char == "}":
            indent_level -= 1

            # insert newline before and after right bracket
            formatted += "\n" + INDENT * indent_level
            formatted += char
            formatted += "\n" + INDENT * indent_level
            continue

        formatted += char

    return formatted


if __name__ == "__main__":
    with open("js_auto_indent/code.txt", "r") as file:
        # removes all tabs and newlines
        CODE = "".join(("".join(file.read().split("\t"))).split("\n"))
    complete = auto_indent(CODE)
    print(complete)
