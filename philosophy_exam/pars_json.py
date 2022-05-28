# ФАЙЛ ДЛЯ ИЗМЕНЕНИЯ КОДИРОВКА JSON C W-1251 НА UTF-8

import json
with open('db.json', encoding='windows-1251') as fh:
    data = json.load(fh)

with open('db_utf.json', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile)