--Numero de registros en tabla
select count(*) as numero_registros from dbo.incidentes_mod;

--mins y maxs
--fecha creacion
SELECT MIN(dbo.incidentes_mod.fecha_creacion) AS min_fechaCreacion, 
MAX(dbo.incidentes_mod.fecha_creacion) as max_fechaCreacion 
FROM dbo.incidentes_mod;

--fecha cierre
SELECT MIN(dbo.incidentes_mod.fecha_cierre) AS min_fecha_cierre, 
MAX(dbo.incidentes_mod.fecha_cierre) as max_fecha_cierre
FROM dbo.incidentes_mod;

--mes
SELECT MIN(dbo.incidentes_mod.mes) AS min_mes, 
MAX(dbo.incidentes_mod.mes) as max_mes 
FROM dbo.incidentes_mod;

--latitud
SELECT MIN(dbo.incidentes_mod.latitud) AS min_latitud, 
MAX(dbo.incidentes_mod.latitud) as max_latitud 
FROM dbo.incidentes_mod;

--longitud
SELECT MIN(dbo.incidentes_mod.longitud) AS min_longitud, 
MAX(dbo.incidentes_mod.longitud) as max_longitud 
FROM dbo.incidentes_mod;

--año cierre
SELECT MIN(dbo.incidentes_mod.año_cierre) AS min_año_cierre, 
MAX(dbo.incidentes_mod.año_cierre) as max_año_cierre 
FROM dbo.incidentes_mod;

--hora cierre
SELECT MIN(dbo.incidentes_mod.hora_cierre) AS min_hora_cierre,
MAX(dbo.incidentes_mod.hora_cierre) as max_hora_cierre
FROM dbo.incidentes_mod;

--valorse no repetidos
--incidente_c4
select distinct dbo.incidentes_mod.incidente_c4 from dbo.incidentes_mod;

--tipo_entrada
select distinct dbo.incidentes_mod.tipo_entrada from dbo.incidentes_mod;

--clas_con_f_alarma
select distinct dbo.incidentes_mod.clas_con_f_alarma from dbo.incidentes_mod;

--delegacion_inicio
select distinct dbo.incidentes_mod.delegacion_inicio from dbo.incidentes_mod;
select * from dbo.incidentes_mod where dbo.incidentes_mod.delegacion_inicio is NULL;

--delegacion_cierre
select distinct dbo.incidentes_mod.delegacion_cierre from dbo.incidentes_mod;

--contar nulos
--incidente_c4
select count(*) nulos_incidente_c4 from dbo.incidentes_mod where dbo.incidentes_mod.incidente_c4 is NULL;

--tipo_entrada
select count(*) nulos_tipo_entrada from dbo.incidentes_mod where dbo.incidentes_mod.tipo_entrada is NULL;

--delegacion_inicio
select count(*) nulos_delegacion_inicio from dbo.incidentes_mod where dbo.incidentes_mod.delegacion_inicio is NULL;

--delegacion_cierre
select count(*) nulos_delegacion_cierre from dbo.incidentes_mod where dbo.incidentes_mod.delegacion_cierre is NULL;
