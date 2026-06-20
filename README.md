# Redrob Candidate Ranker

A candidate ranking system designed to identify and prioritize the most relevant applicants for a Senior AI Engineer role based on professional experience, technical expertise, career progression, and role alignment.

## Overview

This project processes candidate profiles and generates a ranked list of recommendations.

The ranking approach evaluates multiple signals such as:

- Relevant work experience
- Technical skills
- Career progression
- Product and engineering exposure
- Retrieval and ranking expertise
- Overall role fit

The final output is a CSV file containing candidates ordered from most suitable to least suitable.

---

## Features

- Candidate profile analysis
- Multi-factor scoring framework
- Experience-based ranking
- Skill relevance evaluation
- Career trajectory assessment
- Explainable ranking decisions
- CSV output generation
- Submission validation

---

## Usage

Generate rankings:

```bash
python rank.py --candidates data/candidates.jsonl --out submission.csv
```

Validate the generated submission:

```bash
python validate_submission.py submission.csv
```

---

## Ranking Methodology

The ranking system considers a combination of signals, including:

- AI and machine learning experience
- Retrieval and search systems expertise
- Recommendation and ranking systems experience
- Vector databases and embeddings
- Production deployment experience
- Technical leadership indicators
- Career growth and role progression
- Product-focused engineering background
- Location and availability factors

Each candidate receives a weighted score based on these dimensions.

---

## Output

The generated CSV follows the required submission format.

Example:

```csv
candidate_id,rank
12345,1
98765,2
54321,3
```

---

## Requirements

- Python 3.10+
- Candidate dataset in JSONL format
- Dependencies listed in `requirements.txt`

---

## Running the Complete Workflow

```bash
python rank.py --candidates data/candidates.jsonl --out submission.csv

python validate_submission.py submission.csv
```

If validation succeeds, the generated file is ready for submission.

---
