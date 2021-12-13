
--Numero de registros en tabla
select count(*) as numero_registros from dbo.llamadas_911;

select count(manzana) as num_manzanas_iguales, len(manzana) as long_manzana from dbo.llamadas_911 group by len(manzana);
select manzana from  dbo.llamadas_911 where len(manzana) = 2;-- todos estos son NA 3k aprox
select manzana from  dbo.llamadas_911 where len(manzana) = 15;-- todos estos son numericos 200k aprox
select manzana from  dbo.llamadas_911 where len(manzana) = 16; --todos estos son alfanumericos 20k aprox

SELECT count(manzana) FROM dbo.llamadas_911  where manzana like '%[A-Z]%';

select count(*) as numero_registros from dbo.llamadas_911 where manzana not like 'NA';

select count(delegacion_cierre), delegacion_cierre from dbo.llamadas_911 group by delegacion_cierre;

