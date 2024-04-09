import sqlite3
import hashlib
import secrets


class DB:
    def init(db_path, db_schema):
        DB.DATABASE = db_path

        conn = sqlite3.connect(DB.DATABASE)
        cursor = conn.cursor()

        with open(db_schema, 'r') as sql_file:
            cursor.executescript(sql_file.read())

        conn.commit()
        conn.close()

    def verify_schema():
        conn = sqlite3.connect(DB.DATABASE)
        cursor = conn.cursor()
        cursor.execute("""SELECT count(*) FROM sqlite_master WHERE type='table'
        AND name='gps_data'; """)
        data = cursor.fetchone()
        conn.close()

        return data[0]

    def get_gps_data(vehicle_id):
        conn = sqlite3.connect(DB.DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM gps_data WHERE vehicle_id=?
        ''', (vehicle_id,))
        data = cursor.fetchall()
        conn.close()

        return data

    def receive_gps_data(content):
        vehicle_id = content['vehicle_id']
        timestamp = content['timestamp']
        latitude = content['latitude']
        longitude = content['longitude']

        # Save data to SQLite database
        conn = sqlite3.connect(DB.DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO gps_data (vehicle_id, timestamp, latitude, longitude)
            VALUES (?, ?, ?, ?)
        ''', (vehicle_id, timestamp, latitude, longitude))
        conn.commit()
        conn.close()

        return vehicle_id

    def create_token(vehicle_id):
        token = hashlib.sha256(secrets.token_bytes(32)).hexdigest()

        # Save data to SQLite database
        conn = sqlite3.connect(DB.DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO token (vehicle_id, token_hash)
            VALUES (?, ?)
            ON CONFLICT(vehicle_id)
            DO UPDATE SET token_hash=excluded.token_hash;
        ''', (vehicle_id, token))
        conn.commit()
        conn.close()

        return token

    def get_token(token):
        conn = sqlite3.connect(DB.DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM token WHERE token_hash=?
        ''', (token,))
        data = cursor.fetchall()
        conn.close()

        return data
