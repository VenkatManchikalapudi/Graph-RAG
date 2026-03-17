# Backend (FastAPI)

## Features

- Graph-based RAG workflows
- Neo4j integration for storing and querying relationships
- Ollama (Llama2) integration for summarization and Q&A
- **Persistent graph storage** (Neo4j database)
- **In-memory query cache** (per session)

## Endpoints

- `POST /add-document` – Add a document to the graph
- `POST /generate-response` – Generate a response using the RAG pipeline

## Setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Architecture

See `../architecture.md` and `../architecture-flow.txt` for diagrams and flow.

## Notes

- Graph data is stored in Neo4j
- All uploaded data is stored in `uploads/`

# Graph RAG System – Backend

This is the backend implementation for the Graph RAG System. It provides RESTful APIs for adding data to the graph, querying the graph, and generating responses using AI models.

## Features

- Add data to the graph and define relationships
- Query the graph for relevant context
- Generate responses using the RAG pipeline
- FastAPI-based, modular, and production-ready
- Unit and integration tests with pytest

## Tech Stack

- **FastAPI** – API framework
- **Neo4j** – Graph database for relationships
- **Py2Neo** – Python library for Neo4j
- **Ollama** – AI model for summary and Q&A
- **pytest** – Testing

## Project Structure

```
backend/
├── app/
│   ├── api/           # API route definitions
│   ├── models/        # Pydantic schemas
│   ├── services/      # Business logic (Graph RAG, etc.)
│   ├── utils/         # Utility functions (Neo4j, etc.)
│   ├── config.py      # Configuration
│   ├── db.py          # Database models and setup
│   └── main.py        # FastAPI app entrypoint
├── static/            # (Optional) Static files
├── tests/             # Unit and integration tests
├── uploads/           # Uploaded data files
├── requirements.txt   # Python dependencies
├── main.py            # Entrypoint (imports app/main.py)
└── README.md          # This file
```

## Setup & Usage

1. **Install dependencies**
   ```sh
   cd backend
   pip install -r requirements.txt
   ```
2. **Start Ollama** (ensure the model is running, e.g., llama2)
3. **Run the API server**
   ```sh
   uvicorn main:app --reload
   ```
4. **API Docs**: Visit [http://localhost:8000/docs](http://localhost:8000/docs)

## API Endpoints

- `POST /upload` – Upload a PDF file
- `GET /pdfs` – List all uploaded PDFs
- `GET /pdf/{pdf_id}` – Get PDF metadata and chunks
- `DELETE /pdf/{pdf_id}` – Delete a PDF and its chunks
- `POST /summarize` – Generate a summary for a PDF
- `POST /qa` – Ask a question about a PDF

## Testing

Run all tests with:

```sh
pytest
```

## Environment Variables

See `app/config.py` for configuration options (database path, chunk size, etc.).

## Notes

- Ollama must be running locally for summary and Q&A endpoints.
- For production, consider Dockerizing and adding authentication (JWT/OAuth).

---

For architecture and full-stack details, see the root `architecture.md`.
