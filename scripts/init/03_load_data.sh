find /var/mnt/sdf/driving_vitals -name "*.csv" | xargs -t -P40 -IFILENAME psql -U postgres -d postgres -c "copy temp_driving_vitals from 'FILENAME' with csv header encoding 'UTF8'"
find /var/mnt/sdf/events -name "*.csv" | xargs -t -P40 -IFILENAME psql -U postgres -d postgres -c "copy temp_events from 'FILENAME' with csv header encoding 'UTF8'"
find /var/mnt/sdf/vitals -name "*.csv" | xargs -t -P40 -IFILENAME psql -U postgres -d postgres -c "copy temp_vitals from 'FILENAME' with csv header encoding 'UTF8'"


psql -U postgres -d postgres -c "ANALYZE;" &
find /var/mnt/sdf/sensors_map -name "*2022010*.csv" | xargs -t -P10 -IFILENAME psql -U postgres -d postgres -c "CALL postgres.insert_file('FILENAME')"
# psql -U postgres -d postgres -c "ANALYZE;" &

# find /var/mnt/sdf/sensors_map -name "*202202*.csv" | xargs -t -P1 -IFILENAME psql -U postgres -d postgres -c "CALL postgres.insert_file('FILENAME')"
# psql -U postgres -d postgres -c "ANALYZE;" &

# find /var/mnt/sdf/sensors_map -name "*202203*.csv" | xargs -t -P1 -IFILENAME psql -U postgres -d postgres -c "CALL postgres.insert_file('FILENAME')"
# psql -U postgres -d postgres -c "ANALYZE;" &

# find /var/mnt/sdf/sensors_map -name "*202204*.csv" | xargs -t -P1 -IFILENAME psql -U postgres -d postgres -c "CALL postgres.insert_file('FILENAME')"
# psql -U postgres -d postgres -c "ANALYZE;" &

# find /var/mnt/sdf/sensors_map -name "*202205*.csv" | xargs -t -P1 -IFILENAME psql -U postgres -d postgres -c "CALL postgres.insert_file('FILENAME')"
# psql -U postgres -d postgres -c "ANALYZE;" &

# find /var/mnt/sdf/sensors_map -name "*202206*.csv" | xargs -t -P1 -IFILENAME psql -U postgres -d postgres -c "CALL postgres.insert_file('FILENAME')"
# psql -U postgres -d postgres -c "ANALYZE;" &

# find /var/mnt/sdf/sensors_map -name "*202207*.csv" | xargs -t -P1 -IFILENAME psql -U postgres -d postgres -c "CALL postgres.insert_file('FILENAME')"
# psql -U postgres -d postgres -c "ANALYZE;" &

# find /var/mnt/sdf/sensors_map -name "*202208*.csv" | xargs -t -P1 -IFILENAME psql -U postgres -d postgres -c "CALL postgres.insert_file('FILENAME')"
# psql -U postgres -d postgres -c "ANALYZE;" &

# find /var/mnt/sdf/sensors_map -name "*202209*.csv" | xargs -t -P1 -IFILENAME psql -U postgres -d postgres -c "CALL postgres.insert_file('FILENAME')"
# psql -U postgres -d postgres -c "ANALYZE;" &

# find /var/mnt/sdf/sensors_map -name "*202210*.csv" | xargs -t -P1 -IFILENAME psql -U postgres -d postgres -c "CALL postgres.insert_file('FILENAME')"
# psql -U postgres -d postgres -c "ANALYZE;" &

# find /var/mnt/sdf/sensors_map -name "*202211*.csv" | xargs -t -P1 -IFILENAME psql -U postgres -d postgres -c "CALL postgres.insert_file('FILENAME')"
# psql -U postgres -d postgres -c "ANALYZE;" &

# find /var/mnt/sdf/sensors_map -name "*202212*.csv" | xargs -t -P2 -IFILENAME psql -U postgres -d postgres -c "CALL postgres.insert_file('FILENAME')"
# psql -U postgres -d postgres -c "ANALYZE VERBOSE;" &
