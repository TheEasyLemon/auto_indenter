import unittest
from js_auto_indent import format_code, auto_indent, INDENT


class MyTestCase(unittest.TestCase):
    def test_remove_tabs_and_newlines(self):
        """
        Tests if the format_code method can remove all tabs and newlines
        :return:
        """

        test_strs = {
            f"{INDENT}read\n {INDENT}everyday!\n": "read everyday!",  # removes tabs and newlines
            "  here!  ": "here!",  # removes two or more spaces
            "var x=10;": "var x=10;"  # doesn't remove single spaces
        }

        for bef, aft in test_strs.items():
            result = format_code(bef)
            self.assertEqual(result, aft)

    def test_for_loop(self):
        """
        Tests if the auto_indent method correctly formats a JS for loop
        :return:
        """

        test_strs = {
            "for(var e=0;e<5;e++){console.log(e)}": "for(var e=0;e<5;e++) {\n{0}console.log(e)\n}".format(INDENT)
        }

        for bef, aft in test_strs.items():
            result = auto_indent(bef)
            self.assertEqual(result, aft)

    def test_if_stmt(self):
        """
        Tests if the auto_indent method correctly formats a JS if statement
        :return:
        """

        test_strs = {
            "if(!s||o){i()}": "if(!s||o) {\n" + INDENT + "i()\n}"
        }

        for bef, aft in test_strs.items():
            result = auto_indent(bef)
            self.assertEqual(result, aft)


if __name__ == '__main__':
    unittest.main()
