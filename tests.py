import csv
import os
import unittest

from utils import FileOpener as Fo, CharacterEpisodeBundler as Cb,  TableBuilder as Tb

class Step1TestCase(unittest.TestCase):
    
    def setUp(self):

        self.characters_obj        = Fo('characters.csv', 'rb')
        self.characters            = self.characters_obj.open_csv()

        self.appearances_obj       = Fo('episode_per_season.csv', 'rb')
        self.appearances           = self.appearances_obj.open_csv()

        self.character_episodes_obj = Cb(
            self.characters, self.appearances
        )

        self.character_episodes     = self.character_episodes_obj.bundle_characters_per_episodes()

        self.builder_object         = Tb(self.characters)
        self.page_data              = self.builder_object.build()
    
    # Testing whether the object returned is a list 
    def test_list_instance(self):
        self.assertIsInstance(self.characters, list)

    # Testing whether the object returned is a str 
    def test_str_instance(self):
        self.assertIsInstance(
            ''.join(self.page_data), str)


if __name__ == '__main__':
    unittest.main()