with "code.txt" as file:
    CODE = file.read()

TABS = True

if TABS:
    INDENT = "\t"
else:
    INDENT = "  "


def auto_indent(cd):
    """ (str) => (str)
    Takes a string of characters without whitespace, and correctly indents it.
    :return str:
    """
    clean = "".join("".join(cd.split("\n")).split("\t"))

    formatted = ""

    # keeps track of indent level
    indent_level = 0

    for i, char in enumerate(clean):
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
    complete = auto_indent(CODE)
    print(complete)
