# Langchain Neo4j Knowledge Graph Demo

This project aims to demonstrate the potential use of Neo4j graph database as memory of Langchain agent, which contains

1. An implementation of entity graph similar to `NetworkxEntityGraph`, with Neo4j as storage
2. An implementation of `BaseChatMemory` which make use Neo4j knowledge graph, extending existing `ConversationKGMemory` which uses `NetworkxEntityGraph` (in memory entity graph implemented with NetworkX)