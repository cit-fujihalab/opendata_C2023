# find ./data/vitals -name "*.csv" | xargs -IFILENAME psql -h 192.168.10.101 -p 5432 -U postgres -d postgres -c "\copy temp_vitals from"FILENAME" with csv header encoding 'UTF8'"
# find ./data/events -name "*.csv" | xargs -IFILENAME psql -h 192.168.10.101 -p 5432 -U postgres -d postgres -c "\copy temp_events from"FILENAME" with csv header encoding 'UTF8'"
# find ./data/sensors_acc -name "*.csv" | xargs -t -P20 -n1 -IFILENAME psql -h 192.168.10.101 -p 5432 -U postgres -d postgres -c "\copy temp_sensors_acc from"FILENAME" with csv header encoding 'UTF8'"
find /var/mnt/sdf/sensors_map -name "*.csv" | xargs -t -IFILENAME psql -h localhost -p 5432 -U postgres -d postgres -c "copy temp_sensors_map from 'FILENAME' with csv header encoding 'UTF8'"
