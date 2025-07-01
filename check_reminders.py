import sqlite3
from datetime import datetime
from send_sms import send_sms

def check_and_send():
    conn = sqlite3.connect("database/clients.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients")
    clients = cursor.fetchall()
    conn.close()

    print(f"[✓] Found {len(clients)} clients in DB")

    today = datetime.now().date()
    print(f"[INFO] Today is {today}")

    for client in clients:
        id, license_plate, phone, brand, model, expiry = client

        try:
            expiry_date = datetime.strptime(expiry, "%Y-%m-%d").date()
        except ValueError as ve:
            print(f"[X] Invalid date format for client ID {id}: {expiry}")
            continue

        days_left = (expiry_date - today).days
        print(f"[DEBUG] {license_plate} expires in {days_left} days")

        if 0 < days_left <= 7:
            print(f"[✓] Sending SMS to {phone} ({license_plate})")
            send_sms(phone, license_plate, brand, model, expiry)

if __name__ == "__main__":
    check_and_send()