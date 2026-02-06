SELECT
  z."Zone" AS pickup_zone,
  SUM(t.total_amount) AS total_amount_sum
FROM green_trips t
JOIN zones z
  ON t."PULocationID" = z."LocationID"
WHERE t.lpep_pickup_datetime >= '2025-11-18'
  AND t.lpep_pickup_datetime <  '2025-11-19'
GROUP BY z."Zone"
ORDER BY total_amount_sum DESC
LIMIT 1;