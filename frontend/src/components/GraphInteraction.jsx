import React, { useState } from "react";
import { addDocument, generateResponse } from "../api";

const GraphInteraction = () => {
  const [docId, setDocId] = useState("");
  const [content, setContent] = useState("");
  const [relationships, setRelationships] = useState([]);
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");

  const handleAddDocument = async () => {
    try {
      await addDocument(docId, content, relationships);
      alert("Document added successfully!");
    } catch (error) {
      console.error("Error adding document:", error);
    }
  };

  const handleGenerateResponse = async () => {
    try {
      const data = await generateResponse(query);
      setResponse(data.response);
    } catch (error) {
      console.error("Error generating response:", error);
    }
  };

  return (
    <div>
      <h2>Graph Interaction</h2>

      <div>
        <h3>Add Document</h3>
        <input
          type="text"
          placeholder="Document ID"
          value={docId}
          onChange={(e) => setDocId(e.target.value)}
        />
        <textarea
          placeholder="Content"
          value={content}
          onChange={(e) => setContent(e.target.value)}
        />
        <button onClick={handleAddDocument}>Add Document</button>
      </div>

      <div>
        <h3>Generate Response</h3>
        <input
          type="text"
          placeholder="Query"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button onClick={handleGenerateResponse}>Generate Response</button>
        <p>Response: {response}</p>
      </div>
    </div>
  );
};

export default GraphInteraction;
