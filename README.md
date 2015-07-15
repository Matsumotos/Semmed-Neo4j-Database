# Semmed-Neo4j-Database

This contains files for loading the Predication_Aggregate table from SemMedDB into Neo4j.  In order to run, the files should be in the Neo4j directory, along with the Predication_Aggregate table, which should be named p_a.csv and be tab delimited.

The neo4j_data file will create new files that have the subject, object, and predicate information.  It gets the data from the table, sorts and filters it, and then runs the following three python scripts:

  coalesce_phrase_types.py: This checks if the subject or object is repeated.  If so, it adds the type of the word to a list of types associated with that word.  It writes a new file with the types for each word listed and no repeated words.

  remove_repeated_types.py: This checks if any of the types are repeated for each word.  If a type is repeated, it is removed from the list.

  preds.py: This checks if a relationship is repeated.  If so, it adds the PMID citation from the repeated relationship to a list of PMID associated with that relationship.  It writes a file with the PMIDs for each relationship listed and no repeated relationships.

The neo4j_import file runs a script to import the data into Neo4j.  It creates a database named graph.db.  If there is already a database with this name, the import will fail.  The subjects and objects are ndoes labeled "PHRASE," and the predicates are relationships, labeled with the predicate, linking the subjects and objects.
phrase_label.csv and sub_to_object.csv contain the headers to label the nodes and relationships, respectively.

###Format of the Database

Subjects and Objects are nodes (vertices) with label "PHRASE."  The type of the relationship is the predicate.  Nodes have three properties: phrase, type, and cui.  The phrase is the subject or object.  The type is a list of the semantic type abbreviations that apply to the phrase.  The cui is the identification number for the subject or object.

Predicates are relationships (edges).  The relationships have two properties: predicate and pmid.  The predicate is the predicate; it is the same as the relationship type.  The pmid is a list of PMID for articles in which the relationship was found.

###Quick Guide to Neo4j

Please also refer to the Neo4j Manual: neo4j.com/docs/stable/

Find what ngly1 causes:

    match (s {phrase:'ngly1'})-[r:causes]->(o) return o;

Multistep relationships (3-4 steps):
    match (s)-[r*3..4]-(o) return s,r,o skip 1000 limit 5;

Multistep relationships (2 step relationships of type "inhibits"):
    match (s)-[r:inhibits*2]->(o) return s,r,o limit 3;
Find a node with the substring "cancer":

    match (s) where s.phrase =~ '.\*cancer.\*' return s;

Find the shortest path between ngly1 and a node with the substring "cancer":

    match (s {phrase:'ngly1'}), (o) where o.phrase =~ '.*cancer.*'
    match p = shortestPath((s)-[*]-(o))
    return p limit 3;

###Web Accessible Instance of Neo4j

To allow anyone to access the database in the Neo4j browser uncomment
    org.neo4j.server.webserver.address=0.0.0.0
in con/neo4j-server.properties.

For more detail, see the Neo4j Manual, section 24.2 (neo4j.com/docs/stable/server-configuration.html)

For security information, see section 27.1 (neo4j.com/docs/stable/security-server.html)