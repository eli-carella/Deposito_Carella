SELECT rental_id, amount FROM payment
where amount = 0.99;

SELECT rental_id, amount FROM payment
where amount > 4;

select * from film
order by length desc;

select * from film
order by length desc
limit 10;

select * from film
where title like "%aby%";

select * from film
where length > 120 and rental_rate < 10;

select * from film
where length > 180 or rental_rate < 60;

select *from film
where length between 60 and 60;

select * from film
where rating in ("G", "R");

select distinct rental_rate from film;

select count(*) from film;

select rating, count(*) as totale_film
from film
group by rating;

select * from payment;

select customer_id, SUM(amount) as totale_speso
from payment
group by customer_id;

