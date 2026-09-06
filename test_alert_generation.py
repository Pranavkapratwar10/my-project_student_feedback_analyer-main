"""
Test script to verify alert generation and Firebase sync
"""
import sys
import os

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from alerts_database import save_alert, get_all_alerts
from firebase_config import firebase_sync

print("="*80)
print("Testing Alert Generation and Firebase Sync")
print("="*80)

# Test data
test_alert = {
    'faculty_id': 1,
    'faculty_name': 'Test Faculty',
    'faculty_email': 'test.faculty@example.com',
    'department': 'Computer Science',
    'student_id': 'S001',
    'feedback_text': 'I experienced harassment from a classmate during the lab session',
    'sentiment': 'NEGATIVE',
    'category': 'Behavior',
    'alert_keywords': 'harassment',
    'priority': 'High'
}

print("\n1. Saving test alert to database...")
try:
    alert_id = save_alert(**test_alert)
    print(f"   ✓ Alert saved with ID: {alert_id}")
except Exception as e:
    print(f"   ❌ Error saving alert: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n2. Checking SQLite database...")
try:
    alerts = get_all_alerts()
    print(f"   ✓ Total alerts in SQLite: {len(alerts)}")
    if alerts:
        print(f"   ✓ Latest alert: ID={alerts[0]['id']}, Keywords={alerts[0]['alert_keywords']}")
except Exception as e:
    print(f"   ❌ Error reading from SQLite: {e}")

print("\n3. Checking Firebase...")
try:
    firebase_alerts = firebase_sync.get_all_alerts_from_firebase()
    print(f"   ✓ Total alerts in Firebase: {len(firebase_alerts)}")
    if firebase_alerts:
        latest = firebase_alerts[0]
        print(f"   ✓ Latest Firebase alert:")
        print(f"      Faculty: {latest.get('faculty_name')}")
        print(f"      Student: {latest.get('student_id')}")
        print(f"      Keywords: {latest.get('alert_keywords')}")
        print(f"      Firebase Key: {latest.get('firebase_key')}")
except Exception as e:
    print(f"   ❌ Error reading from Firebase: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "="*80)
print("Test Complete!")
print("="*80)
print("\nIf you see alerts in both SQLite and Firebase, the system is working!")
print("If Firebase shows 0 alerts, check:")
print("  1. Firebase Realtime Database is created")
print("  2. Database rules allow write access")
print("  3. Database URL is correct")
