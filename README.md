# Cynbit AI Inquiry & Lead Intelligence Assistant

A proof of concept for the Cynbit AI/ML Engineer Intern assessment. The app retrieves relevant facts from a small public-source knowledge base, classifies inquiry intent, explains a rule-based lead-priority score, and optionally uses an LLM to draft a context-grounded response.

## Important scope note

This is an independent prototype based on publicly available pages, not an official Cynbit product. It does not use internal data or prove business impact. Review the knowledge base and source links before submission.

## Features

- TF-IDF and cosine-similarity retrieval over `data/cynbit_knowledge.json`
- Optional Groq-hosted LLM response using retrieved context
- Retrieval-only fallback if no API key is configured
- Rule-based inquiry intent classification
- Explainable heuristic lead-priority score (not a trained prediction model)
- Source links and JSON download
- Basic unit tests

## Requirements

- Python 3.10+ recommended
- Git
- Optional Groq API key for LLM-generated responses

## Windows PowerShell setup

```powershell
git clone https://github.com/YOUR-USERNAME/cynbit-ai-inquiry-assistant.git
cd cynbit-ai-inquiry-assistant
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

If PowerShell blocks activation, use Command Prompt instead:

```bat
.venv\Scripts\activate.bat
pip install -r requirements.txt
streamlit run app.py
```

## Optional Groq API configuration

1. Copy `.env.example` to `.env`.
2. Put your own API key in `.env` as `GROQ_API_KEY=your_key_here`.
3. The app loads the `.env` file automatically. Alternatively, you can set the key in PowerShell before starting the app:

```powershell
$env:GROQ_API_KEY="your_key_here"
$env:GROQ_MODEL="llama-3.1-8b-instant"
streamlit run app.py
```

Never commit a real API key. The `.env` file is excluded by `.gitignore`. Without a key, retrieval fallback still works.

## Run tests

```powershell
python -m unittest discover -s tests -v
```

## Public information sources

- https://www.cynbit.in/
- https://www.cynbit.in/services
- https://www.cynbit.in/contact

The included knowledge file is a starter snapshot. Verify every statement and update it if the official website changes.

## Reports

- `reports/ai_opportunity_report.md`
- `reports/technical_approach_report.md`

## Limitations

TF-IDF retrieval is lexical rather than fully semantic. Intent classification uses keyword rules. Lead scoring is a transparent heuristic, not a trained model or conversion probability. The optional LLM can still make mistakes and should be evaluated. No internal CRM integration is included.

## Suggested future work

- Compare TF-IDF retrieval with sentence-transformer embeddings.
- Build a labelled evaluation set and report retrieval and classification metrics.
- Add stakeholder-approved content ingestion and freshness checks.
- Add access control, privacy review, monitoring, and human-reviewed CRM integration.
