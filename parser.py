from collections import Counter
from xml.etree.ElementTree import iterparse

import csv
import fnmatch
import os
import re
import time

## Note: you can add your keywords here 
words = ["Physician", "Engineer"]
multi_words = ["work from home"]

## convert all words into lowercase
words = list(map(lambda x: x.lower(), words))
multi_words = list(map(lambda x: x.lower(), multi_words))

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

    for job_node in data:
        job = {}

        # 1. cast all text to lower case
        job_text = job_node.findtext('JobText').lower()
        # 2. replace all non words characters to space
        job_text = re.sub('[^a-zA-Z0-9]', ' ', job_text)
        # 3. replace multiple spaces with single space 
        job_text = ' '.join(job_text.split())

        job['bgtjobid'] = job_node.findtext('JobID') 
        job['jobdate'] = job_node.findtext('JobDate')

        tokens = re.findall(r"[\w]+", job_text)
        token_map = dict.fromkeys(tokens, True)

        for word in words:
            job[word] = 1 if word in token_map else 0

        for word in multi_words:
            job[word] = 1 if word in job_text else 0


        if count % 10000 == 0:
            print('processed ', count, ' jobs...') 

        count += 1
        results.append(job)

    end = time.time()
    duration = end - start
    print('Finished processing ', count, ' in total for ', filepath) 
    print('Total time:', duration)

    ## write to stats.csv
    output_filepath = 'output/' + filename + '.csv' 
    with open(output_filepath, 'w', newline='') as csvfile:
        fieldnames = ['bgtjobid', 'jobdate'] + words + multi_words
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for job in results:
            writer.writerow(job)

d = "data"
for path in os.listdir(d):
    full_path = os.path.join(d, path)
    if os.path.isfile(full_path) and fnmatch.fnmatch(full_path, '*.xml'):
        count_stats(full_path, path)

