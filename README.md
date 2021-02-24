# Directory stucture

Your directory should have the following structure 

data - put all your source xml files in the "data" subfolder
output - all output stats files will be saved in "output" subfolder.

```
.
├── parser.py
├── data 
│   ├── US_XML_AddFeed_20100101_20100107.xml
│   └── US_XML_AddFeed_20100101_20100108.xml
│   └── ...
├── output 
│   ├── US_XML_AddFeed_20100101_20100107.xml.csv
│   ├── US_XML_AddFeed_20100101_20100108.xml.csv
```

# How to run the script
1. Open terminal 
2. `cd /Users/wenfengwang/Wen_Work\ Dropbox/Wen-Feng\ Wang/Wenfeng_Data/BG_XML/Code/job_parser`
3. `python3 parser.py`


4. similary, you can run `python3 count.py` to get a stats of words list against xml files. Notice that there is no pre-processing. We do a simple exact match for counting
```
Start processing file  data/US_XML_AddFeed_20200101_20200107.xml
...
work-from-home : 210
work_from_home : 0
work from home: : 614
work from home: yes : 88
work from home: no : 289
Finished processing  718961  in total for  data/US_XML_AddFeed_20200101_20200107.xml
```

# Usage
1. with a JobText like below 
```
<JobText>working-from-home, working_from_home, working from home, Physician, Engineer From: Company: </JobText> 
```
2. Assume your keywords list is (no special characters in keywords list)
words = ["Physician", "Engineer"]
multi_words = ["working from home"]


3. We expect the output would be
```
bgtjobid,jobdate,physician,engineer,working-from-home,working_from_home,working from home
311017520,2010-01-01,1,1,1,1,1
```  
