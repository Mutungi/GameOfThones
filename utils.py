import csv
import os

# Utility Object For File Output Operations
class FileOpener:

    def __init__(self,  csv_file, mode):
        self.csv_file      = csv_file
        self.mode          = mode
        self.instance_list = []

    # Opens any file and reads it with a specified mode
    def open_csv(self):
        with open(self.csv_file, self.mode) as user_file:
            spam_reader = csv.DictReader(user_file)
            for row in spam_reader:
                self.instance_list.append(row)
        return self.instance_list

# Utility Object To Bundle Up the GOT Character with episodes in which they appeared
class CharacterEpisodeBundler:
    def __init__(self, characters, appearances):
        self.characters  = characters
        self.appearances = appearances
        self.user_appearance = []
        self.character_episodes = []

    #bundling method for the utility class that returns a list object
    def bundle_characters_per_episodes(self):
        for character in self.characters:
            name = character.get('name')
            for appearance in self.appearances:
                if appearance.get('user') == name:
                    self.character_episodes.append("%s Episodes in Season %s" %
                                        (appearance.get('no of episodes'), appearance.get('season')))
                    if int(appearance.get('died in this season')):
                        character['Death Season'] = appearance.get('season')
            character['Episodes Per Season'] = self.character_episodes
        return self.character_episodes

#Utility Class Object that builds the table row structure dynamically and return a list object
class TableBuilder:
    def __init__(self, character_episodes):
        self.page_data          = []
        self.character_episodes = character_episodes
        
    #builder method
    def build(self):
        for character in self.character_episodes:
            data = "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>Season %s</td></tr>" % \
                (character.get('name'), character.get('district'), character.get('mothers name') or 'Unidentified',
                    character.get('fathers name') or 'Unidentified', character.get('date registered'),
                    ',&ensp;'.join(character.get('Episodes Per Season')), character.get('Death Season'))
            self.page_data.append(data)
        return self.page_data


        
