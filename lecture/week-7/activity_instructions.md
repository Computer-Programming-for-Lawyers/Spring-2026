
## Week 8 In Class Activity Instructions

*April 6, 2026*

Working with Copilot or your chosen LLM, scrape [job postings from electionline](https://electionline.org/electionline-weekly/#tab-10). **Your goal is to write code that takes the electionline Weekly URL as its sole input, and exports the job postings on that page as a spreadsheet.**

First, open [the website](https://electionline.org/electionline-weekly/#tab-10) and use your browser's Inspect tool to examine how the site is structured. For example, focus on elements like `<div>`, `<p>`, and `<a>`, and check where the job titles, descriptions, and links are located.

Second, write a script that extracts information about the job postings from the website. It should store the following information about the job postings in a Pandas Dataframe. Pandas is a Python package that lets you make tables, which are called Dataframes. 

The Dataframe should have the job postings stored in these 3 columns of information: : `job_title`, `job_url`, and `job_description`. And the number of rows should be equal to the number of job postings on the page.

Once you feel good about what you've scraped, add it to a Google Sheet and:
- File > Share > Publish to Web
- Set the options Link, Entire Document, Comma-separated values, hit Publish
- Copy the link and email it to will@wtadler.com

*Hint: You may want to write your pandas df to a csv, download that csv, and import into Google Sheets to avoid copy/paste issues.*

### Extra credit
If you finish early, try the following:

* Have your scraper go back in time to scrape job descriptions from all previous electionline Weeklys. All job descriptions should still just go into one big DataFrame. Make sure that the date in the `date` column corresponds to the date on which the job was posted.
* If you finish **all** of that and still have time left over, try using the `gspread` package to write your DataFrame directly to a Google Sheet.s
