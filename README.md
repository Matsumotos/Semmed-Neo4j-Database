# Semmed-Neo4j-Database

This contains files for loading the Predication_Aggregate table from SemMedDB into Neo4j.  In order to run, the files should be in the Neo4j directory, along with the Predication_Aggregate table, which should be named p_a.csv and be tab delimited.

The neo4j_data file will create new files that have the subject, object, and predicate information.  It sorts and filter data from the table and then runs the following three python scripts:

  coalesce_phrase_types.py: This checks if the subject or object is repeated.  If so, it adds the semantic type abbreviation of the word to a list of types associated with that word.  It writes a new file with the types for each word listed and no repeated words.

  remove_repeated_types.py: This checks if any of the types are repeated for each word.  If a type is repeated, it is removed from the list.

  preds.py: This checks if a relationship is repeated.  If so, it adds the PMID citation from the repeated relationship to a list of PMIDs associated with that relationship.  It writes a file with the PMIDs for each relationship listed and no repeated relationships.

The neo4j_import file runs a script to import the data into Neo4j.  It creates a database named graph.db in Neo4j's data directory.  If there is already a database with this name, the import will fail.

phrase_label.csv and sub_to_obj.csv contain the headers labeling the nodes and relationships, respectively.

###Structure of the Database

Subjects and objects are nodes (vertices) with the label "PHRASE."  Nodes have three properties: phrase, type, and cui.  The phrase is the subject or object.  The type is a comma-separated array of the semantic type abbreviations that apply to the phrase.  The cui is the identification number from UMLS or EntrezGene for the subject or object.

Predicates are relationships (edges) that go from the subject to the object.  The type of the relationship is the predicate.  The relationships have two properties: predicate and pmid.  The predicate property contains the predicate; it is the same as the relationship type.  The pmid is a comma-separated array of PMIDs for articles in which the relationship was found.

###Quick Guide to Neo4j

Please also refer to the Neo4j Manual: neo4j.com/docs/stable/

Find what ngly1 causes:

    match (s {phrase:'ngly1'})-[r:causes]->(o) return o;

Find subjects and objects with types 'gngm' and 'imft' (limit to 25 results):

    match (s) where 'gngm' in s.type and 'imft' in s.type return s limit 25;

Multistep relationships (3-4 steps; skip the first 1000 paths returned):

    match (s)-[r*3..4]-(o) return s,r,o skip 1000 limit 5;

Multistep relationships (2 step relationships of type "inhibits"):

    match (s)-[r:inhibits*2]->(o) return s,r,o limit 3;

Fine relationship of type "location_of" or "neg_location_of":

    match p = (()-[r:neg_location_of|location_of]-())
    return p skip 10000 limit 5;

Find the shortest paths between ngly1 and nodes with the substring "cancer":

    match (s {phrase:'ngly1'}), (o) where o.phrase =~ '.*cancer.*'
    match p = shortestPath((s)-[*]-(o))
    return p limit 3;

Find subjects related to objects with the subtring "cancer," ordered by the number of objects:

    match (s)-->(o) where o.phrase =~ '.*cancer.*'
    return s.phrase as subject, collect(distinct o.phrase) as objects, count(distinct o) as num
    order by num DESC;

###Web Accessible Instance of Neo4j

To allow anyone to access the database in the Neo4j browser, uncomment

    org.neo4j.server.webserver.address=0.0.0.0

in conf/neo4j-server.properties.

For more detail, see the Neo4j Manual, section 24.2 (neo4j.com/docs/stable/server-configuration.html)

For security information, see section 27.1 (neo4j.com/docs/stable/security-server.html)
