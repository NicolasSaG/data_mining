select delegacion_cierre, month(llamadas_911.fecha_creacion) as mes, day(llamadas_911.fecha_creacion) as dia, count(*) as average 
from dbo.llamadas_911 
group by delegacion_cierre, month(llamadas_911.fecha_creacion), day(llamadas_911.fecha_creacion);

--catalogo de delegaciones
select distinct(llamadas_911.delegacion_cierre), row_number() OVER (ORDER BY llamadas_911.delegacion_cierre DESC) AS id from dbo.llamadas_911 order by llamadas_911.delegacion_cierre;

select distinct(llamadas_911.delegacion_cierre) from dbo.llamadas_911 order by llamadas_911.delegacion_cierre as catalogo_delegaciones;


--catalogo de delegaciones
select catalogo_delegaciones.delegacion,  row_number() OVER (ORDER BY catalogo_delegaciones.delegacion asc) AS id into dbo.catalogo_delegaciones from 
(select distinct(llamadas_911.delegacion_cierre) as delegacion from dbo.llamadas_911) as catalogo_delegaciones order by catalogo_delegaciones.delegacion;

select * from dbo.catalogo_delegaciones order by id;

--cambiar nombre delegacion por id
select delegacion_cierre, id, month(llamadas_911.fecha_creacion) as mes, day(llamadas_911.fecha_creacion) as dia, count(*) as average 
from dbo.llamadas_911, dbo.catalogo_delegaciones where llamadas_911.delegacion_cierre = catalogo_delegaciones.delegacion
group by delegacion_cierre,id, month(llamadas_911.fecha_creacion), day(llamadas_911.fecha_creacion);

--cambiar id con join
select delegacion_cierre, id, month(llamadas_911.fecha_creacion) as mes, day(llamadas_911.fecha_creacion) as dia, count(*) as average 
from dbo.llamadas_911, dbo.catalogo_delegaciones where llamadas_911.delegacion_cierre = catalogo_delegaciones.delegacion
group by delegacion_cierre,id, month(llamadas_911.fecha_creacion), day(llamadas_911.fecha_creacion);

--crear tabla hechos
select id, month(llamadas_911.fecha_creacion) as mes, day(llamadas_911.fecha_creacion) as dia, count(*) as average into dbo.tabla_hechos 
from dbo.llamadas_911, dbo.catalogo_delegaciones where llamadas_911.delegacion_cierre = catalogo_delegaciones.delegacion
group by id, month(llamadas_911.fecha_creacion), day(llamadas_911.fecha_creacion);


--




--select count(*) from dbo.llamadas_911;
--select sum(asd.average) from (select delegacion_cierre, month(llamadas_911.fecha_creacion) as mes, day(llamadas_911.fecha_creacion) as dia, count(*) as average 
--from dbo.llamadas_911 
--group by delegacion_cierre, month(llamadas_911.fecha_creacion), day(llamadas_911.fecha_creacion)) as asd;