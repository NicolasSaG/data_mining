USE [pph]


select elemento as Elemento, localizacion as Delegación, semana as NoSemana, año as Año, mes as Mes, medicion as Medición from dbo.bitacora;

--Creacion de Cubos solicitados
--a) delegacion, noSemana, anio
select localizacion as Delegación, semana as NoSemana, año as Año, medicion as Medición into dbo.cubo_a_dsa from dbo.bitacora;

--b) delegacion, noSemana, mes
select localizacion as Delegación, semana as NoSemana, mes as Mes, medicion as Medición into dbo.cubo_b_dsm from dbo.bitacora;

--c) delegcion, noSemana
select localizacion as Delegación, semana as NoSemana, medicion as Medición into dbo.cubo_c_ds from dbo.bitacora;

--d) Delegacion, mes
select localizacion as Delegación, mes as Mes, medicion as Medición into dbo.cubo_d_dm from dbo.bitacora;

--e) delegacion anio
select localizacion as Delegación, año as Año, medicion as Medición into dbo.cubo_e_da from dbo.bitacora;

--f) delegacion
select localizacion as Delegación, medicion as Medición into dbo.cubo_f_d from dbo.bitacora;

--g) anio
select año as Año, medicion as Medición into dbo.cubo_g_a from dbo.bitacora;

--h) mes
select mes as Mes, medicion as Medición into dbo.cubo_h_m from dbo.bitacora;

--i) noSemana
select semana as NoSemana, medicion as Medición into dbo.cubo_i_s from dbo.bitacora;

