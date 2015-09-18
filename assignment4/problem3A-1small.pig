register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' USING TextLoader AS (line:chararray);

ntriples = FOREACH raw GENERATE FLATTEN(myudfs.RDFSplit3(line)) AS (subject:chararray,predicate:chararray,object:chararray);

filtered_triples = FILTER ntriples BY subject MATCHES '.*business.*' PARALLEL 50;

filtered_triples2 = FOREACH filtered_triples GENERATE $0 AS subject2, $1 AS predicate2, $2 AS object2 PARALLEL 50;

joined_triples = JOIN filtered_triples BY subject, filtered_triples2 BY subject2 PARALLEL 50;

unique_joined_triples = DISTINCT joined_triples PARALLEL 50;

grouped_by_all = GROUP unique_joined_triples ALL PARALLEL 50;

count_of_all = FOREACH grouped_by_all GENERATE COUNT(unique_joined_triples) PARALLEL 50;

STORE count_of_all INTO '/user/hadoop/problem3A' USING PigStorage();
