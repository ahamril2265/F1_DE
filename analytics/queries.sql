-- Fastest lap
SELECT driver, MIN(lap_time_sec) FROM lap_times GROUP BY driver;

-- Driver consistency
SELECT driver, STDDEV(lap_time_sec) FROM lap_times GROUP BY driver;