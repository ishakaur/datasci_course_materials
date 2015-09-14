1. select count(*) from frequency where docid = "10398_txt_earn";
2. select count(term) from frequency where docid = "10398_txt_earn" and count = 1;
3. select count(*) from (select term from frequency where docid = "10398_txt_earn" and count = 1 union select term from frequency where docid = "925_txt_trade" and count = 1) unionized;
4. select count (distinct docid) from frequency where term = 'parliament';
5. select count(*) from (select docid from frequency group by docid having sum(count) > 300);
6. select count(*) from frequency f1 join frequency f2 on f1.docid = f2.docid where f1.term = 'transactions' and f2.term = "world";