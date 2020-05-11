import os.path
import unittest
from bs4 import BeautifulSoup

from gourmet.plugins.import_export.website_import_plugins import foodnetwork_plugin

class DummyImporter(object):
    class MenuAndAdStrippingWebParser(object):
        def preparse(dummy):
            pass


class TestFoodnetworkPlugin(unittest.TestCase):

    url = "http://www.foodnetwork.com/recipes/ask-aida/pan-roasted-chicken-with-oranges-and-rosemary-recipe/index.html"

    def _read_html(self):
        filename = os.path.join(os.path.dirname(__file__),
                        'recipe_files',
                        (os.path.splitext(os.path.basename(__file__))[0])[5:-7]+".html")
        with open(filename, encoding="utf8") as infile:
            data = infile.read()
        return data

    def setUp(self):
        self.text = self._read_html()
        self.plugin = foodnetwork_plugin.FoodNetworkPlugin()

    def test_url(self):
        self.assertEqual(self.plugin.test_url(self.url, self.text), 5)
        self.assertEqual(self.plugin.test_url("http://www.foodnetwork.com/rec", self.text), 5)
        self.assertEqual(self.plugin.test_url("http://foodnetwork.com/rec", self.text), 5)
        self.assertEqual(self.plugin.test_url("http://www.foodnetwork.com", self.text), 5)
        self.assertEqual(self.plugin.test_url("http://www.foodnetwork.net", self.text), 0)
        self.assertEqual(self.plugin.test_url("http://google.com", self.text), 0)

    def test_parse(self):
        # Setup
        parser = self.plugin.get_importer(DummyImporter)()
        parser.soup = BeautifulSoup(self.text, "lxml")
        # Do the parsing
        parser.preparse()
        # Pick apart results
        result = parser.preparsed_elements

        # Result is a list of tuples (text, keyword) and we are searching for the current
        # keyword. On success we retrieve the text itself and add it to the list.
        # For the name we create a list, but have only one text which we retrieve.
        ingredients = [r[0] for r in result if r[1] == "ingredients"]
        name = [r for r in result if r[1] == "title"][0][0]
        instructions = [r[0] for r in result if r[1] == "recipe"]

        # Check results
        self.assertEqual(len(ingredients), 8)

        self.assertTrue('Pan-Roasted Chicken with Oranges and Rosemary' in name)

        self.assertTrue('Heat oven to 450 degrees F and arrange rack in middle.' in instructions)

        # The text to check for is part of a list element, not the full list element.
        # Therefore we are creating a single string with the instructions for this check.
        self.assertTrue('Let rest 5 minutes before serving.' in "\n".join(instructions))

        self.assertFalse('You must be logged in to review this recipe.' in instructions)



if __name__ == '__main__':
    unittest.main()