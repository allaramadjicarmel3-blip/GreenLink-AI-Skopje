# GreenLink AI — Geospatial RAG Assistant for Skopje's Green Infrastructure

**GenAI for Good Challenge: Cities Edition (IEEE & UNDP)**  
**Selected Use Case:** Green Infrastructure AI Assistant (Skopje, North Macedonia)

## Overview
**GreenLink AI** is an open-source Generative AI assistant built on the **GENIE.AI framework**. It bridges Skopje's scattered municipal archives (historical permits, field inspection reports, botanical surveys in Macedonian and English) with its Digital Green Cadastre, enabling urban planners and environmental inspectors to retrieve source-backed, parcel-level insights in seconds.

## Core Architecture
- **GENIE.AI Native Microservices:** Leverages the ChatQnA reference architecture (`Dataprep`, `Retriever`, and `LLM Orchestrator`).
- **Multimodal OCR & Layout Parser:** Extracts structured text, tables, and stamps from scanned administrative PDFs.
- **Hybrid Geospatial Storage:** Combines **PostgreSQL/PostGIS** (cadastral parcel IDs and geometries) with **FAISS/Qdrant** (multilingual semantic embeddings via `BAAI/bge-m3`).
- **Citation-Backed Conflict Detection:** Grounds every response strictly in retrieved municipal records with clickable source citations while flagging discrepancies between historical permits and current protection statuses.

## Repository Structure
- `rag_pipeline.py`: Prototype pipeline demonstrating multilingual document chunking, hybrid vector indexing, and grounded citation retrieval.
- `README.md`: Project overview and architectural documentation.

## Team
- **Allaramadji Carmel** — Project Lead & AI Engineer
- **Mbaïnguemsi Japhet** — Data Engineer & Quality Assurance Engineer

## License
Released under an open-source permissive license (Apache 2.0 / MIT).
