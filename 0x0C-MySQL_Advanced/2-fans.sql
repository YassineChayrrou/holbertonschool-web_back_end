-- SQL script
-- Description: Ranks country origins of bands, ordered by number of fans.
-- fans are not unique
SELECT
origin,
SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC
