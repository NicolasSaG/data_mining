/****** Script for SelectTopNRows command from SSMS  ******/
SELECT COUNT(*) as registros_totales
  FROM [testdb].[dbo].[bitacora];

SELECT [año], COUNT(*) as registros
  FROM [testdb].[dbo].[bitacora]
  GROUP BY [año];