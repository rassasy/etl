from neo4j import GraphDatabase


driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))

def insert_restaurant_links(restaurants):
    with driver.session() as session:
        for restaurant in restaurants:
            print(f"Adding {restaurant.name}'s relationships to Neo4j")
            restaurant.toNeo4j(session)
        driver.close()