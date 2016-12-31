from unittest import TestCase
from main import get_file_names

class TestGet_file_names(TestCase):
    def test_gets_filenames(self):
        names = get_file_names("../test_images")
        self.assertEquals(True, "../test_images/flavortown.jpg" in names)
        self.assertEquals(True, "../test_images/flavortown_copy.jpg" in names)
        self.assertEquals(True, "../test_images/trump is not :shoegazi:.jpg" in names)
        self.assertEquals(3, len(names))
