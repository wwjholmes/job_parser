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
