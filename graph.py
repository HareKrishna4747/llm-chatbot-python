import streamlit as st

# Connect to Neo4j
import os
from dotenv import load_dotenv


# tag::graph[]
from langchain_neo4j import Neo4jGraph

graph = Neo4jGraph(
    url="neo4j+s://d9c46fd0.databases.neo4j.io",
    username="neo4j",
    password="lqvXmMRMadUfXDtcSPs1W-FS7korC8_xs4GaXct91eY"
)

#end::graph[]