import sqlite3
from datetime import datetime

# Check alerts.db
conn = sqlite3.connect('alerts.db')
cursor = conn.cursor()

# Count total alerts
cursor.execute('SELECT COUNT(*) FROM alerts')
total = cursor.fetchone()[0]
print(f"Total alerts in database: {total}")

if total > 0:
    # Get recent alerts
    cursor.execute('''
        SELECT id, faculty_name, student_id, alert_keywords, status, created_at 
        FROM alerts 
        ORDER BY created_at DESC 
        LIMIT 10
    ''')
    
    print("\nRecent alerts:")
    print("-" * 80)
    for row in cursor.fetchall():
        print(f"ID: {row[0]}")
        print(f"  Faculty: {row[1]}")
        print(f"  Student: {row[2]}")
        print(f"  Keywords: {row[3]}")
        print(f"  Status: {row[4]}")
        print(f"  Created: {row[5]}")
        print("-" * 80)
else:
    print("\n⚠️ No alerts found in database!")
    print("This means alerts are not being saved during analysis.")

conn.close()

# Check if Firebase sync is working
print("\n" + "="*80)
print("Checking Firebase sync...")
print("="*80)

try:
    from backend.firebase_config import firebase_sync
    
    alerts = firebase_sync.get_all_alerts_from_firebase()
    print(f"Total alerts in Firebase: {len(alerts)}")
    
    if len(alerts) > 0:
        print("\nRecent Firebase alerts:")
        print("-" * 80)
        for alert in alerts[:5]:
            print(f"Firebase Key: {alert.get('firebase_key')}")
            print(f"  Faculty: {alert.get('faculty_name')}")
            print(f"  Student: {alert.get('student_id')}")
            print(f"  Keywords: {alert.get('alert_keywords')}")
            print(f"  Status: {alert.get('status')}")
            print("-" * 80)
    else:
        print("\n⚠️ No alerts found in Firebase!")
        print("Alerts may not be syncing to Firebase.")
        
except Exception as e:
    print(f"❌ Error checking Firebase: {e}")
