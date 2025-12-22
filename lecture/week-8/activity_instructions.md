
## Week 8 In Class Activity Instructions

*April 7, 2025*

Work with a partner to scrape [job postings from electionline](https://electionline.org/electionline-weekly/#tab-9). **Your goal is to write code that takes the electionline Weekly URL as its sole input, and exports the job postings on that page as a spreadsheet.**

First, open [the website](https://electionline.org/electionline-weekly/#tab-9) and use your browser's Inspect tool to examine how the site is structured. For example, focus on elements like `<div>`, `<p>`, and `<a>`, and check where the job titles, descriptions, and links are located.

Second, write a script that extracts information about the job postings from the website. It should store the following information about the job postings in a Pandas Dataframe. Pandas is a Python package that lets you make tables, which are called Dataframes. They're just like spreadsheets in Excel!

The Dataframe should have the job postings stored in these 3 columns of information: : `job_title`, `job_url`, and `job_description`. And the number of rows should be equal to the number of job postings on the page.

We've provided some code to get you started; this will download and parse the information on the page. But it doesn't do anything to try to extract the specific information about job postings. You'll need to write that part (or use an AI to help you write it)!

### Starter code
``` python
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Electionline Weekly job postings page
url = "https://electionline.org/electionline-weekly"

# Header to prevent 403 error
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Send a GET request to fetch the content of the page
response = requests.get(url, headers=headers)

# Parse the page content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")
```

*Hint: To extract the jobs, you will need to write code that parses the content within the `div` element that contains the text `Job Postings This Week`.*

After this, we will explore how to extract useful information from the job descriptions.

Once you feel good about what you've scraped, add it to a Google Sheet and:
- File > Share > Publish to Web
- Set the options Link, Entire Document, Comma-separated values, hit Publish
- Copy the link and email it to will@wtadler.com

*Hint: You may want to write your pandas df to a csv, download that csv, and import into Google Sheets to avoid copy/paste issues.*

### Extra credit
If you finish early, try the following:

* Use a `for` or `while` loop to scrape job descriptions from previous electionline Weeklys. All job descriptions should still just go into one big DataFrame. Make sure that the date in the `date` column corresponds to the date on which the job was posted.
* If you finish **all** of that and still have time left over, try using the `gspread` package to write your DataFrame directly to a Google Sheet.

**After ~15 minutes of work, we'll ask students to volunteer to share their screens and show us what they accomplished, troubleshooting together as needed.**
