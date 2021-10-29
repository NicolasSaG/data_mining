--Punto 2: Identifique valores nulos y errores en los formatos de tipo de datos

--Fecha_creacion
select count(*) nulos_fecha_creacion from dbo.incidentes where dbo.incidentes.fecha_creacion is NULL;

--todos los relacionados al cierre
--	codigo_cierre	
select count(*) nulos_codigo_cierre from dbo.incidentes where dbo.incidentes.codigo_cierre is NULL;

--	fecha_cierre	
select count(*) nulos_fecha_cierre from dbo.incidentes where dbo.incidentes.fecha_cierre is NULL;

--	año_cierre
select count(*) nulos_año_cierre from dbo.incidentes where dbo.incidentes.año_cierre is NULL;

--	mes_cierre	
select count(*) nulos_mes_cierre from dbo.incidentes where dbo.incidentes.mes_cierre is NULL;

--	hora_cierre	
select count(*) nulos_hora_cierre from dbo.incidentes where dbo.incidentes.hora_cierre is NULL;

--	delegacion_cierre
select count(*) nulos_delegacion_cierre from dbo.incidentes where dbo.incidentes.delegacion_cierre is NULL;


select * from dbo.incidentes where dbo.incidentes.delegacion_cierre is NULL;

--se encontro un valor nulo en delegacion se procede a eliminar
delete from dbo.incidentes where dbo.incidentes.delegacion_cierre is NULL;

--Incidente_c4
select count(*) nulos_incidente_c4 from dbo.incidentes where dbo.incidentes.incidente_c4 is NULL;


--otras columnas 
select count(*) nulos_folio from dbo.incidentes where dbo.incidentes.folio is NULL;
select count(*) nulos_hora_creacion from dbo.incidentes where dbo.incidentes.hora_creacion is NULL;
select count(*) nulos_dia_semana from dbo.incidentes where dbo.incidentes.dia_semana is NULL;
select count(*) nulos_delegacion_inicio from dbo.incidentes where dbo.incidentes.delegacion_inicio is NULL;
select count(*) nulos_latitud from dbo.incidentes where dbo.incidentes.latitud is NULL;

select count(*) nulos_longitud from dbo.incidentes where dbo.incidentes.longitud is NULL;
select count(*) nulos_clas_con_f_alarma from dbo.incidentes where dbo.incidentes.clas_con_f_alarma is NULL;
select count(*) nulos_tipo_entrada from dbo.incidentes where dbo.incidentes.tipo_entrada is NULL;
select count(*) nulos_geopoint from dbo.incidentes where dbo.incidentes.geopoint is NULL;
select count(*) nulos_mes from dbo.incidentes where dbo.incidentes.mes is NULL;


--no se encontro nada mas




--numero de registros despues de limpieza
select count(*) as numero_registros from dbo.incidentes;


--verificar duplicados
select dbo.incidentes.delegacion_inicio, count(*) ocurrencias from dbo.incidentes group by delegacion_inicio having count(*) > 0;

select dbo.incidentes.delegacion_cierre, count(*) ocurrencias from dbo.incidentes group by delegacion_cierre having count(*) > 0;

--palabra NULL
select * from dbo.incidentes where dbo.incidentes.delegacion_inicio = 'NULL';

--se eliminan los que tienen NULL como string
delete from dbo.incidentes where dbo.incidentes.delegacion_inicio = 'NULL';

--verificar campos con strings
select dbo.incidentes.codigo_cierre, count(*) ocurrencias from dbo.incidentes group by codigo_cierre having count(*) > 0;
select dbo.incidentes.dia_semana, count(*) ocurrencias from dbo.incidentes group by dia_semana having count(*) > 0;
select dbo.incidentes.año_cierre, count(*) ocurrencias from dbo.incidentes group by año_cierre having count(*) > 0;
select dbo.incidentes.incidente_c4, count(*) ocurrencias from dbo.incidentes group by incidente_c4 having count(*) > 0;
select dbo.incidentes.clas_con_f_alarma, count(*) ocurrencias from dbo.incidentes group by clas_con_f_alarma having count(*) > 0;
select dbo.incidentes.tipo_entrada, count(*) ocurrencias from dbo.incidentes group by tipo_entrada having count(*) > 0;
select dbo.incidentes.mes, count(*) ocurrencias from dbo.incidentes group by mes having count(*) > 0;

select dbo.incidentes.hora_cierre , count(*) ocurrencias from dbo.incidentes group by hora_cierre having count(*) > 0;

--verificar folios duplicados
select dbo.incidentes.folio, count(*) ocurrencias from dbo.incidentes group by folio having count(*) > 1;
