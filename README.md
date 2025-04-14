# InsightEdgeChatBot

InsightEdge Knowledge Base Assistant is a lightweight, local AI-powered Q&A tool that allows users to query InsightEdge documentation stored in markdown (`.md`) files. It uses semantic search to return the most relevant answers from your documentation.

---
## Features

- Supports question answering using `.md` files
- Fast semantic search with cosine similarity
- Easy ingestion of markdown content
- Simple Flask-powered web interface
- Expandable system with modular architecture

---

## Tech Stack

- **Frontend**: HTML, CSS (optional styling)
- **Backend**: Python + Flask
- **Storage**: JSON (`database.json`)

## Project Structure
- Konowledge_base
   - about_InsightEdge.md
   - account_setup.md
   - api_intro.md
   - billing_info.md
   - collaborations_and_sharing.md
   - common_issues.md
   - creat_database.md
   - faq.md
   - features_overview.md
   - integration_guide_google_sheets.md
   - pricing_plans.md
   - product_overview.md
   - security.md
   - workflow_templates.md
-Templates
   - index.html
- app.py
- config.py
- indexer.py
- ingestion.py
- llm.py
- retrival.py
- search.py
- storage.py
- utiles.py
- database.json

## Setup Instructions
- Clone the Repository
- Create a Virtual Environment
- Install Required Packages
- Add Markdown Files
- Ingest Data and Generate Database (python ingestion.py)
- Launch the App (python app.py)

## Prompt Engineering Approach
- Structured Prompts: Markdown sub-headings (e.g. ## How to connect) are treated as "questions", and their associated body content is used as the "answer".
- Retrieval Strategy: Cosine similarity is calculated between the user’s question embedding and all stored question embeddings to find the most relevant answer.

## Limitations
- Returns only the top matched result (no multiple or ranked answers).
- Works best with consistently structured markdown.
- Does not perform deep reasoning or cross-document synthesis.
- Cannot handle vague or ambiguous queries well.
- Static content — does not paraphrase or summarize across sources.

## Future Improvements
- Add chat interface with history and source highlighting
- Fallback response system for unmatched queries
- Admin dashboard to track usage and common questions
