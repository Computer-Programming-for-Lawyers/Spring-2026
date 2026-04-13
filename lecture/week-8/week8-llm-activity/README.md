## Week 8 In-Class Activity: Group C — Extracting Information from Proposed Rules

*April 13, 2026*

The `files/` folder contains 74 proposed federal rules published in the last few weeks, pulled directly from the Federal Register. They span tax law, financial regulation, crypto, nuclear security, environmental policy, labor, healthcare, and more. Browse the filenames and pick one that interests you.

### Step 1: Get an API key

**Use GitHub Models — free with your GitHub Education account.**

Browse available models at [github.com/marketplace?type=models](https://github.com/marketplace?type=models) and try one in the playground first.

To use it from Python:
- Go to [github.com/settings/tokens](https://github.com/settings/tokens) → Generate new token (fine-grained), no special permissions needed
- Store it as a Codespaces secret: repo → **Settings** → **Secrets and variables** → **Codespaces** → **New repository secret**, name it `GITHUB_TOKEN`
- Restart your Codespace, then read it with `os.environ.get("GITHUB_TOKEN")`
- GitHub Models uses an OpenAI-compatible API — install `openai` and ask Copilot to show you a minimal working example pointed at `https://models.inference.ai.azure.com`

Already have a Claude or OpenAI key for PS7? Store it the same way and use that instead.

### Step 2: Extract the PDF text and send it to the model

Install `pdfplumber` to extract text from the PDF, then send it to the model. Ask Copilot to help you wire these two things together.

### Step 3: Decide what to extract

You're writing a prompt — so you decide what comes out. Think about what a lawyer working in this area would want to know from a proposed rule at a glance:

- What is the rule proposing to change, in plain English?
- Who is affected, and how?
- When does the comment period close?
- What are the stated justifications?
- What compliance obligations does it create?

Pick one document, get something useful out of it, then try a second one with the same prompt. Does it hold up across documents?

### If you finish early

Pull the documents yourself. The Federal Register has a free API — no key required — that returns proposed rules with direct PDF links. Write a script that queries it, filters to an agency or topic you care about, and downloads the PDFs automatically. The endpoint to start with:

```
https://www.federalregister.gov/api/v1/documents.json?conditions[type][]=PRORULE&per_page=20&order=newest
```

### At the end of class

One person from your group shares: which rule did you look at, what did you ask the model to extract, and how well did it do?
