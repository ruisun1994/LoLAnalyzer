# Define all the shared constants among the scripts

import configparser
import os
from collections import OrderedDict


class Base_Mode:
    def __init__(self, image=False):
        self.image = image

        # Downloader+
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.DATABASE = self.config['PARAMS']['database']
        self.PATCHES_TO_DOWNLOAD = self.config['PARAMS']['download_patches'].split(',')
        self.LEAGUES = {league: enabled == 'yes' for (league, enabled) in self.config['LEAGUES'].items()}
        self.REGIONS = self.config['REGIONS']

        # Extractor+
        self.DATA_LINES = 100000
        self.GAME_FILES = os.listdir(os.path.join(self.DATABASE, 'patches'))
        self.CHAMPIONS_ID = OrderedDict([(champ_name, int(champ_id)) for (champ_name, champ_id) in self.config['CHAMPIONS'].items()])
        self.CHAMPIONS_LABEL = self.config['PARAMS']['sortedChamps'].split(',')

        # Processing+
        self.SAVE = 1000
        self.PATCHES = list(map(lambda x: x.replace('.', '_'), os.listdir(os.path.join(self.DATABASE, 'patches'))))
        self.CHAMPIONS_SIZE = len(self.CHAMPIONS_LABEL)
        self.PATCHES_SIZE = len(self.PATCHES)
        self.OUTPUT_SIZE = 1

        # LEARNING+
        self.CKPT_DIR = os.path.join(self.DATABASE, 'models')

    def __str__(self):
        return 'Base_{}'.format(self.image)

    def __repr__(self):
        return 'Base_Mode(*{!r})'.format(self.image)


class ABOTJMCS_Mode(Base_Mode):
    def __init__(self, image=False):
        super().__init__(image)
        self.EXTRACTED_FILE = os.path.join(self.DATABASE, 'extracted_ABOTJMCS.txt')
        self.EXTRACTED_DIR = os.path.join(self.DATABASE, 'extracted_ABOTJMCS')
        self.PREPROCESSED_DIR = os.path.join(self.DATABASE, 'data_ABOTJMCS')
        self.SHUFFLED_DIR = os.path.join(self.DATABASE, 'shuffled_ABOTJMCS')

        self.COLUMNS = self.CHAMPIONS_LABEL[:]
        self.COLUMNS.append('patch')
        self.COLUMNS.append('team')
        self.COLUMNS.append('win')
        self.COLUMNS.append('file')
        self.DTYPE = {champ: str for champ in self.CHAMPIONS_LABEL}
        self.DTYPE['patch'] = str
        self.DTYPE['team'] = int
        self.DTYPE['win'] = int
        self.DTYPE['file'] = str
        self.CHAMPIONS_STATUS = ['A', 'B', 'O', 'T', 'J', 'M', 'C', 'S']
        if not self.image:
            self.INPUT_SIZE = len(self.CHAMPIONS_LABEL) * len(self.CHAMPIONS_STATUS) + len(self.PATCHES) + 1
        else:
            self.INPUT_SIZE = len(self.CHAMPIONS_LABEL) * (len(self.CHAMPIONS_STATUS) + len(self.PATCHES) + 1)

    def __str__(self):
        return 'ABOTJMCS_{}'.format(self.image)

    def __repr__(self):
        return 'ABOTJMCS_Mode(*{!r})'.format(self.image)


class ABOT_Mode(Base_Mode):
    def __init__(self, image=False):
        super().__init__(image)
        self.EXTRACTED_FILE = os.path.join(self.DATABASE, 'extracted_ABOT.txt')
        self.EXTRACTED_DIR = os.path.join(self.DATABASE, 'extracted_ABOT')
        self.PREPROCESSED_DIR = os.path.join(self.DATABASE, 'data_ABOT')
        self.SHUFFLED_DIR = os.path.join(self.DATABASE, 'shuffled_ABOT')

        self.COLUMNS = self.CHAMPIONS_LABEL[:]
        self.COLUMNS.append('patch')
        self.COLUMNS.append('team')
        self.COLUMNS.append('win')
        self.COLUMNS.append('file')
        self.DTYPE = {champ: str for champ in self.CHAMPIONS_LABEL}
        self.DTYPE['patch'] = str
        self.DTYPE['team'] = int
        self.DTYPE['win'] = int
        self.DTYPE['file'] = str
        self.CHAMPIONS_STATUS = ['A', 'B', 'O', 'T']
        if not self.image:
            self.INPUT_SIZE = len(self.CHAMPIONS_LABEL) * len(self.CHAMPIONS_STATUS) + len(self.PATCHES) + 1
        else:
            self.INPUT_SIZE = len(self.CHAMPIONS_LABEL) * (len(self.CHAMPIONS_STATUS) + len(self.PATCHES) + 1)

    def __str__(self):
        return 'ABOT_{}'.format(self.image)

    def __repr__(self):
        return 'ABOT_Mode(*{!r})'.format(self.image)


class BR_Mode(Base_Mode):
    def __init__(self, image=False):
        super().__init__(image)
        self.EXTRACTED_FILE = os.path.join(self.DATABASE, 'extracted_BR.txt')
        self.EXTRACTED_DIR = os.path.join(self.DATABASE, 'extracted_BR')
        self.PREPROCESSED_DIR = os.path.join(self.DATABASE, 'data_BR')
        self.SHUFFLED_DIR = os.path.join(self.DATABASE, 'shuffled_BR')

        self.COLUMNS = self.CHAMPIONS_LABEL[:]
        self.COLUMNS.append('patch')
        self.COLUMNS.append('win')
        self.COLUMNS.append('file')
        self.DTYPE = {champ: str for champ in self.CHAMPIONS_LABEL}
        self.DTYPE['patch'] = str
        self.DTYPE['win'] = int
        self.DTYPE['file'] = str
        self.CHAMPIONS_STATUS = ['B', 'R']
        if not self.image:
            self.INPUT_SIZE = len(self.CHAMPIONS_LABEL) * len(self.CHAMPIONS_STATUS) + len(self.PATCHES)
        else:
            self.INPUT_SIZE = len(self.CHAMPIONS_LABEL) * (len(self.CHAMPIONS_STATUS) + len(self.PATCHES))

    def __str__(self):
        return 'BR_{}'.format(self.image)

    def __repr__(self):
        return 'BR_Mode(*{!r})'.format(self.image)