## Week 8 In-Class Activity: Group A — Fetching Live Data with an API Key

*April 13, 2026*

### Step 1: Get your API key (do this first)

Go to **[api.open.fec.gov/developers](https://api.open.fec.gov/developers/)** and click "Get an API Key." Fill in your name and email — your key appears on the page immediately.

Then store it as a repository secret so it's available in Codespaces without ever appearing in your code:
- Go to your repo on GitHub → **Settings** → **Secrets and variables** → **Codespaces** → **New repository secret**
- Name it `FEC_API_KEY`, paste your key as the value, and save
- Restart your Codespace (or open a new one) for the secret to appear

In your script, read it with `os.environ.get("FEC_API_KEY")` — no `.env` file needed.

### Step 2: Fetch something

The FEC API ([docs](https://api.open.fec.gov/developers/)) exposes campaign finance data — contributions, candidates, committees, and filings. Some starting points:

- **Who raised the most in 2024?**  
  `GET /v1/candidates/totals/?office=P&election_year=2024&sort=-receipts`

- **Who donated to a specific candidate?**  
  `GET /v1/schedules/schedule_a/?committee_id=<id>&per_page=100`  
  (Find a committee ID by searching a candidate name in the candidates endpoint first)

- **What's a given state's total contributions?**  
  `GET /v1/schedules/schedule_a/?contributor_state=TX&per_page=100`

Use `requests.get()` with `params={"api_key": api_key, ...}`. Look at what comes back, pick a few fields that are interesting, and either print them or load them into a DataFrame.

### If you finish early

Keep pulling. Try a different endpoint, a different candidate, a different state, a different time range — the FEC API has a lot of surface area. Then pick one of these next steps:
- **Visualize it.** Load your results into a DataFrame and make a chart. What does the fundraising picture look like across candidates or over time?
- **Set up a GitHub Action.** Write a workflow that runs your script on a schedule and commits the output to your repo. Your key is already stored as a secret — wiring it into a workflow is the next step.

### At the end of class

One person from your group shares their screen: what did you ask for, what came back, and what did you find?
