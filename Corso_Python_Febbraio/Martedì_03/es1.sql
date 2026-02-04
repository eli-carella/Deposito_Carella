-- Estrai i nomi (first_name) e i cognomi (last_name) di tutti gli attori presenti nella tabella actor. Rinomina le colonne come "Nome" e "Cognome" per rendere il report più leggibile.
select first_name as nome, last_name as cognome from actor;

-- Trova tutti i titoli dei film che hanno un rating uguale a 'G' (General Audiences).
select title from film
where rating = "G";

-- Trova tutti i clienti nella tabella customer il cui nome inizia con la lettera "A" e il cognome finisce con la lettera "S".
SELECT * FROM customer
WHERE first_name LIKE 'A%'AND last_name LIKE '%S';

-- Seleziona i film che hanno una durata (length) superiore a 150 minuti E un costo di noleggio (rental_rate) inferiore a 1.00$.
SELECT * FROM film
WHERE length > 150 AND rental_rate < 1.00;

