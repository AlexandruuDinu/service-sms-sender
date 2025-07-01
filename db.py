import sqlite3
import os

# Calea absolută, garantat să meargă pe orice sistem
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database", "clients.db")

def init_db():
    os.makedirs(os.path.join(BASE_DIR, "database"), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            license_plate TEXT NOT NULL,
            phone TEXT NOT NULL,
            brand TEXT NOT NULL,
            model TEXT NOT NULL,
            expiry_date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def update_client(client_id, license_plate, phone, brand, model, expiry_date):
    conn = sqlite3.connect("database/clients.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE clients
        SET license_plate = ?, phone = ?, brand = ?, model = ?, expiry_date = ?
        WHERE id = ?
    """, (license_plate, phone, brand, model, expiry_date, client_id))
    conn.commit()
    conn.close()

def get_client_by_id(client_id):
    conn = sqlite3.connect("database/clients.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients WHERE id = ?", (client_id,))
    client = cursor.fetchone()
    conn.close()
    return client

def get_all_clients():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients")
    clients = cursor.fetchall()
    conn.close()
    return clients

def add_client(license_plate, phone, brand, model, expiry_date):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clients (license_plate, phone, brand, model, expiry_date) VALUES (?, ?, ?, ?, ?)",
                   (license_plate, phone, brand, model, expiry_date))
    conn.commit()
    conn.close()

def delete_client(client_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clients WHERE id=?", (client_id,))
    conn.commit()
    conn.close()
