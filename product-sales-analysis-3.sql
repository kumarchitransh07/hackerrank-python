with ct as (
    select
    product_id,
MIN(year) as first_year 
from 
sales
group by product_id
)
select
sales.product_id,
ct.first_year,
sales.quantity,
sales.price
from sales
inner join ct on
sales.product_id = ct.product_id
and ct.first_year = sales.year




# Write your MySQL query statement below
select product_id,year as first_year, quantity, price
from Sales
where(product_id, year) in (select  product_id, min(year) from Sales group by product_id)
