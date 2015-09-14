1.
General: select f1.docid, f2.docid, sum(f1.count * f2.count) as value from frequency f1, frequency f2 where f1.docid < f2.docid and f1.term = f2.term group by f1.docid, f2.docid order by value;
Specific: select f1.docid, f2.docid, sum(f1.count * f2.count) as value from frequency f1, frequency f2 where f1.docid = '10080_txt_crude' and f2.docid = '17035_txt_earn' and f1.term = f2.term group by f1.docid, f2.docid;
2.
select f2.docid, sum(f1.count * f2.count) as value
from (SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION
SELECT 'q' as docid, 'treasury' as term, 1 as count) f1,
(SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION
SELECT 'q' as docid, 'treasury' as term, 1 as count) f2
where f1.docid = 'q' and f1.term = f2.term group by f1.docid, f2.docid order by value;