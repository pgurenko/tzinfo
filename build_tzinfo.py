#!/usr/bin/python
import os
import sys
import json
import re

os.system('wget ftp://ftp.iana.org/tz/tzdata-latest.tar.gz')
os.system('mkdir ./tzdata')
os.system('tar -C ./tzdata -xvf tzdata-latest.tar.gz')
os.system('for file in ./tzdata/*; do zic -d ./tzdata/out $file; done')

timezones = {}

pattern = re.compile('(?:\<[\+\-0-9]+\>)?([\+\-\,\.\/A-Z0-9]*)')

tzdata_dir = './tzdata/out/'
for root, dirs, files in os.walk(tzdata_dir):
    for filename in files: 
        filepath = os.path.join(root,filename)
        zone_name = filepath[len(tzdata_dir):]

        with open(filepath, 'r') as f:
            lines = f.read().split()
            magic_version = lines[0][0:5]
            if magic_version == 'TZif2':
                tz_string = lines[-1]
                tz_match = pattern.match(tz_string)
                if tz_match:
                    timezones[zone_name] = tz_match.group(1)

with open('tzinfo', 'w+') as f:
    f.write(json.dumps(timezones))
