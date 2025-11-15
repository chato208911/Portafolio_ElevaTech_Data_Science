/*
  Consultas SQL Fundamentales
  Demostrando SELECT, WHERE, JOIN y GROUP BY (Requisitos de ElevaTech)
*/

-- Supongamos que tenemos dos tablas:
-- 1. PROYECTOS (ProyectoID, Nombre, RegionID, Inversion)
-- 2. REGIONES (RegionID, NombreRegion, Responsable)

-- 1. Consulta SELECT simple con Clausula WHERE
-- Objetivo: Obtener la inversión de proyectos en la región Norte.
SELECT
    Nombre,
    Inversion
FROM
    PROYECTOS
WHERE
    RegionID = 1; -- Asumiendo que RegionID = 1 es 'Norte'

-- 2. Consulta con JOIN
-- Objetivo: Listar todos los proyectos junto con el nombre del responsable de su región.
SELECT
    p.Nombre AS Nombre_Proyecto,
    r.NombreRegion,
    r.Responsable
FROM
    PROYECTOS p
INNER JOIN
    REGIONES r ON p.RegionID = r.RegionID;

-- 3. Uso de Agregación y GROUP BY
-- Objetivo: Calcular la inversión total y el número de proyectos por cada región.
SELECT
    r.NombreRegion,
    SUM(p.Inversion) AS Inversion_Total,
    COUNT(p.ProyectoID) AS Cantidad_Proyectos
FROM
    PROYECTOS p
INNER JOIN
    REGIONES r ON p.RegionID = r.RegionID
GROUP BY
    r.NombreRegion
HAVING
    COUNT(p.ProyectoID) > 1; -- Ejemplo de filtro avanzado