find /var/mnt/sdf/driving_vitals -name "*.csv" | xargs -t -P60 -IFILENAME psql -U postgres -d postgres -c "copy temp_driving_vitals from 'FILENAME' with csv header encoding 'UTF8'"
find /var/mnt/sdf/events -name "*.csv" | xargs -t -P60 -IFILENAME psql -U postgres -d postgres -c "copy temp_events from 'FILENAME' with csv header encoding 'UTF8'"
find /var/mnt/sdf/vitals -name "*.csv" | xargs -t -P60 -IFILENAME psql -U postgres -d postgres -c "copy temp_vitals from 'FILENAME' with csv header encoding 'UTF8'"


find /var/mnt/sdf/sensors_map -name "*202201*.csv" | xargs -t -P35 -IFILENAME psql -U postgres -d postgres -c "copy temp_sensors_map from 'FILENAME' with csv header encoding 'UTF8'"
psql -U postgres -d postgres -c "CALL move_positions();"
