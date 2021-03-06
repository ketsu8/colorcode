from gettext import translation
from os import listdir
from os.path import dirname, join
from sys import argv

from PySide2.QtCore import QSettings

path = dirname(argv[0])
translations_path = join(path, 'translations')
settings = QSettings('settings.ini', QSettings.IniFormat)

languages = []
for language in listdir(translations_path):
    if language.startswith('__'): continue
    languages.append(language)

from random import choice, randint
language = settings.value('interface/language', 'en_EN')
toolBarEnable = True if settings.value('interface/toolBarEnable', 'true') == 'true' else False
buttomPanelEnable = True if settings.value('interface/buttomPanelEnable', 'false') == 'true' else False
statusBarEnable = True if settings.value('interface/statusBarEnable', 'true') == 'true' else False
autoCompleteEnable = True if settings.value('interface/autoCompleteEnable', 'false') == 'true' else False
name = settings.value('personal/name', '{alias}user{id}'.format(alias=choice(['super', 'mega', 'ultimate', 'alpha', 'beta', 'ultra']), id=str(randint(100000, 999999))))
email = settings.value('personal/email', '')
country = settings.value('personal/country', 'Russia')
preReleasesEnable = True if settings.value('updates/allowPreReleases', 'false') == 'true' else False

def returnLanguage(language):
    return translation('prettycode', translations_path, [language]).gettext