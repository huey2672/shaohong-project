#!/usr/bin/python
#encoding=utf-8

import ConfigParser
import glob
import os
import csv

cp = ConfigParser.SafeConfigParser()
cp.read('settings.conf')

src_file_pattern = cp.get('local', 'src_file_pattern')
dst_directory = cp.get('local', 'dst_directory')
dst_file_prefix = cp.get('local', 'dst_file_prefix')
dst_file_suffix = cp.get('local', 'dst_file_suffix')
csv_file = cp.get('local', 'csv_file')
starting_number = cp.getint('local', 'starting_number')

src_files = glob.glob(src_file_pattern)

csv_data = []

for src_file in src_files: 
    dst_file = dst_directory + dst_file_prefix + str(starting_number).zfill(4) + dst_file_suffix
    os.rename(src_file, dst_file)
    csv_data.append([os.path.basename(src_file), os.path.basename(dst_file)])
    starting_number = starting_number + 1

with open(csv_file, 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(csv_data) 