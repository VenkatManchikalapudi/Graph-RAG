# Updated Architecture Flow (Mermaid)

Below is the updated Mermaid diagram representing the high-level flow of the Graph RAG System:

```mermaid
flowchart LR
    subgraph User
        U1["User Uploads Data"]
        U2["User Views Results"]
        U3["User Asks Questions"]
    end
    subgraph Frontend
        FE["React App"]
    end
    subgraph Backend
        BE["FastAPI Server"]
        UPLOADS["Uploads Folder"]
        GRAPHDB["Graph Database (Neo4j)"]
        QUERY["Graph Query (Cypher)"]
        CONTEXT["Context Retrieval"]
    end
    subgraph LLM
        OLLAMA["Ollama LLM (Llama2)"]
    end

    U1-->|Upload|FE
    FE-->|REST API|BE
    BE-->|Save Data|UPLOADS
    BE-->|Store in Graph|GRAPHDB
    GRAPHDB-->|Query|QUERY
    QUERY-->|Retrieve Context|CONTEXT
    CONTEXT-->|Send Context|BE
    BE-->|Generate Response|OLLAMA
    OLLAMA-->|Response|BE
    BE-->|Results|FE
    FE-->|Show|U2

    FE-->|Ask Question|BE
    BE-->|Query Graph|GRAPHDB
    GRAPHDB-->|Relevant Context|BE
    BE-->|Answer|OLLAMA
    OLLAMA-->|Answer|BE
    BE-->|Display|FE
```

**Legend:**

- User interacts with the React frontend (upload, view results, ask questions)
- Frontend communicates with FastAPI backend
- Backend processes data, stores in a graph database, manages context retrieval and response generation
- Ollama LLM is used for generating responses
- Results are returned to the user via the frontend

---

For more details, see the rest of this `architecture.md` and the backend `README.md`.
