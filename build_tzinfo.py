#!/usr/bin/python
import os
import sys
import json

os.system('wget ftp://ftp.iana.org/tz/tzdata-latest.tar.gz')
os.system('tar -C ./tzdata -xvf tzdata-latest.tar.gz')
os.system('for file in ./tzdata/*; do zic -d ./tzdata/out $file; done')

timezones = {}

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
                if tz_string:
                    timezones[zone_name] = tz_string

with open('tzinfo', 'w+') as f:
    f.write(json.dumps(timezones))
