# README

## What is this ?

This is a python code to get referrer url using Google Search Console API. You need to get access to Google Search Console first before using this code.

## How to use

1. Install package `pip install requirements.txt`
2. Put your Google Search Console auth json file into this project, change the name into `google.json`
3. Open `main.py` and edit the `SITE_URL`, add your Google Search Console domain. If you want to run it via domain property, add `sc:` before your domain.
4. Run the script via `python main.py`

If you want to get only the domain of referring page, just `get_domain.py`. It will use file `404_errors_with_referring_pages.csv` by default.

## Template file

### File Table.csv for main.py

```csv
URL,Last crawled
this-is-url,this-is-last-crawled
```

### File 404_errors_with_referring_pages.csv for get_domain.py

```csv
URL,Referring Pages
this-is-your-url,this-is-referring-page
```
