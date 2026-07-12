proc sql;
create table sales_summary as
select
    region,
    sum(amount) as total_sales,
    avg(amount) as avg_sale,
    count(*) as transactions
from sales
group by region;
quit;