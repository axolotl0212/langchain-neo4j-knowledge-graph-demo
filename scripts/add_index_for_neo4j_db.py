import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

# Load env var from .env
load_dotenv()


def main():
    driver = GraphDatabase.driver(
        uri=os.getenv("NEO4J_DB_URI"),
        auth=(os.getenv("NEO4J_DB_USER"), os.getenv("NEO4J_DB_PASS")),
        database=os.getenv("NEO4J_DB_NAME"),
    )

    with driver.session() as session:
        session.run(
            "CREATE TEXT INDEX idx_node_entity_name IF NOT EXISTS FOR (n:Entity) ON (n.name)"
        )
        session.run(
            f"CREATE FULLTEXT INDEX {os.getenv('NEO4J_ENTITY_NAME_FULLTEXT_INDEX_NAME')} IF NOT EXISTS "
            + "FOR (n:Entity) "
            + "ON EACH [n.name] "
            + "OPTIONS {indexConfig: {`fulltext.analyzer`: 'cjk'}}"
        )


# Run the main function of the app
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Keyboard interrupt, quitting")
        pass
