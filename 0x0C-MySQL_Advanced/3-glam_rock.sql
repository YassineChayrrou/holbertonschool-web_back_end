-- sql script that lists all bands with Glam rock as their main style
-- listing is ranked by longevity
SELECT
band_name,
IFNULL(split, CURRENT_DATE()) - formed AS lifespan
FROM metal_bands
WHERE style REGEXP '.*Glam rock.*'
ORDER BY lifespan DESC;

