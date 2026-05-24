# Disney Accelerator Tracker

A full-stack AWS web application for tracking and analyzing Disney Accelerator portfolio companies across all cohorts from 2014–2025.

**Live demo:** https://main.d1e74dieu7z9xm.amplifyapp.com/
## What it does

- Browse all Disney Accelerator companies with filtering by cohort year, tech category, and Disney vertical
- Visualizes the growth of AI & Synthetic Media companies over time — supporting the thesis that Disney is systematically investing in tools that compress the content production pipeline
- Suggests category tags for new companies based on a rules-based engine built from my own analysis of Disney's investment patterns
- Allows adding new companies to the database for future cohort tracking

## My thesis

Disney's accelerator isn't just "open to AI" — it's systematically investing in tools that collapse the cost and time of content production at each layer of the stack: animation (Animaj), voice (ElevenLabs), audio (AudioShake), environments (Promethean AI), and characters (Inworld). The investment thesis maps directly to Disney's business units, with Studio & Animation and DTC & Streaming as the primary collaboration targets.

## Tech stack

- **DynamoDB** — NoSQL database storing all company records with flexible schema
- **Lambda** — Serverless functions for GET and POST endpoints
- **API Gateway** — REST API exposing endpoints to the frontend
- **Amplify** — Frontend hosting with continuous deployment from GitHub
- **IAM** — Least-privilege roles scoped to DynamoDB access only

## Why each technology choice

- DynamoDB over RDS because startup metadata is unstructured — some companies have more fields than others and a flexible schema fits better than rigid SQL tables
- Lambda over EC2 because the app has low, spiky traffic — pay-per-request makes more sense than running a server 24/7
- PAY_PER_REQUEST billing mode to avoid charges during low-traffic periods

## API

- `GET /companies` — returns all companies
- `POST /companies` — adds a new company to the database

## Built by

Althea Aguel — ECE junior at Princeton University
