# Graph RAG System Architecture

## Overview

The Graph RAG System is a full-stack application that integrates a graph database to enable Retrieval-Augmented Generation (RAG) workflows. Users can upload data, query the graph for relevant context, and generate responses using AI models. The project is organized into two main parts:

- **Backend**: FastAPI, Python, Neo4j, Ollama AI
- **Frontend**: React

## Directory Structure

```
Graph RAG System/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── config.py
│   │   ├── db.py
│   │   ├── main.py
│   ├── static/
│   ├── tests/
│   ├── uploads/
│   ├── requirements.txt
│   ├── README.md
│   └── architecture.md
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   ├── README.md
│   └── vite.config.js
├── README.md
└── architecture.md
```

## Backend Architecture

- **FastAPI**: REST API for graph-based RAG workflows
- **Neo4j**: Graph database for storing and querying relationships
- **Ollama**: AI model for generating responses
- **Py2Neo**: Python library for interacting with Neo4j
- **Tests**: Pytest for unit and integration tests

## Frontend Architecture

- **React**: User interface for uploading data, querying the graph, and viewing results
