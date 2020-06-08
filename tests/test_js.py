import unittest
from js_auto_indent import auto_indent


class MyTestCase(unittest.TestCase):
    def test_remove_tabs_and_newlines(self):
        """
        Test that it can remove all tabs and newlines
        :return:
        """

        test_strs = {
            "\tread\n \teveryday!\n": "read everyday!",  # removes tabs and newlines
            "  here!  ": "here!",  # removes two or more spaces
            "var x=10;": "var x=10;\n"  # doesn't remove single spaces
        }

        for bef, aft in test_strs.items():
            result = auto_indent(bef)
            self.assertEqual(result, aft)

    def test_for_loop(self):
        """
        Test that it correctly formats a JS for loop
        :return:
        """

        test_strs = {
            "for(var e=0;e<5;e++){console.log(e)}": "for(var e=0;e<5;e++){\n\tconsole.log(e)\n}\n"
        }

        for bef, aft in test_strs.items():
            result = auto_indent(bef)
            self.assertEqual(result, aft)


if __name__ == '__main__':
    unittest.main()
