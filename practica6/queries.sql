select
'0' + manzana
From dbo.ubicacion 
where len(dbo.ubicacion.manzana) = 15

update dbo.ubicacion
set [manzana] = '0' + [manzana]
From dbo.ubicacion 
where len(dbo.ubicacion.manzana) = 15
