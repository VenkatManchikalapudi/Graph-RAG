from app.utils.graph_utils import GraphUtils
from app.services.ollama_service import OllamaService

class GraphRAGService:
    def __init__(self, graph_uri, graph_user, graph_password):
        self.graph = GraphUtils(graph_uri, graph_user, graph_password)
        self.ollama = OllamaService()

    def add_document(self, doc_id, content, relationships):
        # Add document as a node
        self.graph.add_node(doc_id, {"content": content})
        
        # Add relationships
        for rel in relationships:
            self.graph.add_relationship(doc_id, rel["to_id"], rel["type"])

    def generate_response(self, query):
        # Query the graph for relevant nodes
        graph_query = """
        MATCH (n:Node)
        WHERE n.properties.content CONTAINS $query
        RETURN n
        """
        relevant_nodes = self.graph.query_graph(graph_query, {"query": query})

        # Extract context from nodes
        context = "\n".join([node["n"]["properties"]["content"] for node in relevant_nodes])

        # Generate response using the language model
        return self.ollama.generate_response(query, context)

    def close(self):
        self.graph.close()