find ./data/vitals -name "*.csv" | xargs -IFILENAME psql -h 192.168.10.101 -p 5432 -U postgres -d postgres -c "\copy temp2 from"FILENAME" with csv header encoding 'UTF8'"
