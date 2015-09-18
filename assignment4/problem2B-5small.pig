REGISTER s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader AS (line:chararray);

ntriples = FOREACH raw GENERATE FLATTEN(myudfs.RDFSplit3(line)) AS (subject:chararray,predicate:chararray,object:chararray);

subjects = GROUP ntriples BY (subject) PARALLEL 50;

count_by_subject = FOREACH subjects GENERATE FLATTEN($0), COUNT($1) AS count PARALLEL 50;

counts = GROUP count_by_subject BY (count) PARALLEL 50;

count_by_counts = FOREACH counts GENERATE FLATTEN($0), COUNT($1) AS count_of_counts PARALLEL 50;

count_by_counts_ordered =  ORDER count_by_counts BY (count_of_counts) PARALLEL 50;

STORE count_by_counts_ordered INTO '/user/hadoop/problem2B' USING PigStorage();
