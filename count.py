from collections import Counter
from xml.etree.ElementTree import iterparse

import csv
import fnmatch
import os
import re
import time

## Note: you can add your keywords here 
words = ["work-from-home", "work_from_home", "work from home:", "work from home: yes", "work from home: no"]

## convert all words into lowercase
words = list(map(lambda x: x.lower(), words))

## You should not need to touch the code below
def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    # Skip the root element
    next(doc)

    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass
def count_stats(filepath, filename):
    start = time.time()
    print('\nStart processing file ', filepath) 
    data = parse_and_remove(filepath, 'Job')

    results = []
    count = 1 
    stats = {}

    for word in words:
        stats[word] = 0

    for job_node in data:

        # 1. cast all text to lower case
        job_text = job_node.findtext('JobText').lower()

        for word in words:
            stats[word] += 1 if word in job_text else 0

        if count % 10000 == 0:
            print('processed ', count, ' jobs...') 

        count += 1

    results.append(stats)

    end = time.time()
    duration = end - start

    for key in stats:
        print(key, ':', stats[key])

    print('Finished processing ', count, ' in total for ', filepath) 
    print('Total time:', duration)

    ## write to stats.csv
    # output_filepath = 'output/' + filename + '-count_stats.csv' 
    # with open(output_filepath, 'w', newline='') as csvfile:
    #     fieldnames = words + multi_words
    #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    #     writer.writeheader()
    #     for job in results:
    #         writer.writerow(job)

d = "data"
for path in os.listdir(d):
    full_path = os.path.join(d, path)
    if os.path.isfile(full_path) and fnmatch.fnmatch(full_path, '*.xml'):
        count_stats(full_path, path)

