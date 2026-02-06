SELECT
  z_drop."Zone" AS dropoff_zone,
  t.tip_amount
FROM green_trips t
JOIN zones z_pick
  ON t."PULocationID" = z_pick."LocationID"
JOIN zones z_drop
  ON t."DOLocationID" = z_drop."LocationID"
WHERE z_pick."Zone" = 'East Harlem North'
  AND t.lpep_pickup_datetime >= '2025-11-01'
  AND t.lpep_pickup_datetime <  '2025-12-01'
ORDER BY t.tip_amount DESC
LIMIT 1;