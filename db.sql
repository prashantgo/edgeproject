CREATE TABLE IF NOT EXISTS sourcestest (
  source_id SERIAL PRIMARY KEY,
  source varchar(200) NOT NULL,
  source_type varchar(10) NOT NULL,
  source_tag varchar(10) NOT NULL,
  frequency varchar(5) NOT NULL,
  last_update_date TIMESTAMP,
  from_date TIMESTAMP,
  to_date TIMESTAMP
);