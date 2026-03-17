from neo4j import GraphDatabase

class GraphUtils:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def add_node(self, node_id, properties):
        with self.driver.session() as session:
            session.write_transaction(self._add_node, node_id, properties)

    @staticmethod
    def _add_node(tx, node_id, properties):
        query = (
            "CREATE (n:Node {id: $node_id, properties: $properties})"
        )
        tx.run(query, node_id=node_id, properties=properties)

    def add_relationship(self, from_id, to_id, relationship_type):
        with self.driver.session() as session:
            session.write_transaction(self._add_relationship, from_id, to_id, relationship_type)

    @staticmethod
    def _add_relationship(tx, from_id, to_id, relationship_type):
        query = (
            "MATCH (a:Node {id: $from_id}), (b:Node {id: $to_id}) "
            "CREATE (a)-[r:" + relationship_type + "]->(b)"
        )
        tx.run(query, from_id=from_id, to_id=to_id)

    def query_graph(self, query, parameters=None):
        with self.driver.session() as session:
            result = session.read_transaction(self._query_graph, query, parameters)
        return result

    @staticmethod
    def _query_graph(tx, query, parameters):
        return list(tx.run(query, parameters))