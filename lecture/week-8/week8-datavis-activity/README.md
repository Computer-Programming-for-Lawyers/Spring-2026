## Week 8 In-Class Activity: Group B — Visualizing Toxic Release Data

*April 13, 2026*

The EPA's [Toxics Release Inventory](https://www.epa.gov/toxics-release-inventory-tri-program) tracks how much of each toxic chemical U.S. facilities release into the environment each year. The `us_20XX/` folders contain that data for 2020–2024. Each year's data is in `US_1a_20XX.txt`.

### Loading the data

These are tab-separated files, not comma-separated — you'll need to tell pandas that. You'll probably also hit an error on your first load attempt. Read the error message carefully: it tells you exactly what's wrong and where. Google the error type with "pandas read_csv" to find the fix.

Once one year loads, try combining all five into a single DataFrame.

### Useful columns

There are 282 columns. The ones worth focusing on: year, facility name, state, chemical name, whether the chemical is a carcinogen, whether it's a PFAS compound, and total on-site release in pounds. Print `df.columns.tolist()` and `df.head()` to orient yourself — the column names are numbered and the ones you want are roughly in the middle of the list.

### Your goal

Pick any question the data can answer and make a chart that shows it. It doesn't have to be one of these — if something else about toxic releases interests you, go for it. Some starting points:

- Which states have the highest total toxic releases? Has that changed from 2020 to 2024?
- Are carcinogen releases going up or down over time?
- PFAS ("forever chemicals") reporting was expanded recently — how has reported PFAS release volume changed year over year?
- Which facilities are the largest releasers in a given state?
- Pick a specific chemical — lead compounds, mercury, arsenic — and look at where it's being released and how much.


### What to aim for

At least one labeled, titled chart that answers a specific question (or your own!).

### If you finish early

Go back to the source. The data you loaded was downloaded manually from the EPA website. Write a script that does that automatically — fetches the zip files for each year directly from [the TRI data page](https://www.epa.gov/toxics-release-inventory-tri-program/tri-basic-plus-data-files-calendar-years-1987-present), extracts them, and saves the files locally. That way, next year's data can be pulled with a single command instead of a manual download.


### At the end of class

One person from your group shares their screen: what question did you ask, what does the chart show, and did anything surprise you?
