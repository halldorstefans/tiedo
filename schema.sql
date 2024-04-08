-- Create a table to store GPS data
CREATE TABLE IF NOT EXISTS gps_data (
    id INTEGER PRIMARY KEY,
    vehicle_id TEXT NOT NULL,
    timestamp DATETIME NOT NULL,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL
);

-- Optional: Create an index on vehicle_id for faster retrieval
CREATE INDEX IF NOT EXISTS idx_vehicle_id ON gps_data (vehicle_id);

-- Optional: Create an index on timestamp for time-based queries
CREATE INDEX IF NOT EXISTS idx_timestamp ON gps_data (timestamp);

-- Create a table to store tokens
CREATE TABLE IF NOT EXISTS token (
    id INTEGER PRIMARY KEY,
    vehicle_id TEXT NOT NULL UNIQUE,
    token_hash TEXT NOT NULL UNIQUE    
);

-- Optional: Create an index on token_hash for faster retrieval
CREATE INDEX IF NOT EXISTS idx_token_hash ON token (token_hash);
