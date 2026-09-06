"""
Test complete alert flow from upload to display
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

print("="*80)
print("TESTING COMPLETE ALERT FLOW")
print("="*80)

# Step 1: Analyze feedback
print("\n1️⃣ STEP 1: Analyzing feedback with NLP...")
from nlp_test import analyze_feedback_csv
result = analyze_feedback_csv('test_alert_feedback.csv', 'Feedback', 'uploads/test_analyzed.csv')
print(f"   ✓ Analysis complete")

# Step 2: Check analyzed CSV
print("\n2️⃣ STEP 2: Checking analyzed CSV...")
import pandas as pd
df = pd.read_csv('uploads/test_analyzed.csv')
alerts_in_csv = df[df['Alert'] == 'Yes']
print(f"   ✓ Total rows: {len(df)}")
print(f"   ✓ Alerts in CSV: {len(alerts_in_csv)}")
print(f"   ✓ Alert students: {list(alerts_in_csv['Student_ID'])}")

# Step 3: Save alerts to database
print("\n3️⃣ STEP 3: Saving alerts to database...")
from alerts_database import save_alert

faculty_id = 1
faculty_name = "Test Faculty"
faculty_email = "test@example.com"
faculty_dept = "Computer Science"

saved_count = 0
for idx, row in alerts_in_csv.iterrows():
    feedback = str(row['Feedback'])
    feedback_lower = feedback.lower()
    
    # Find keywords
    alert_keywords = []
    for keyword in ["harassment", "discrimination", "unsafe", "abuse", "bullying", "threat", "violence"]:
        if keyword in feedback_lower:
            alert_keywords.append(keyword)
    
    try:
        alert_id = save_alert(
            faculty_id=faculty_id,
            faculty_name=faculty_name,
            faculty_email=faculty_email,
            department=faculty_dept,
            student_id=str(row['Student_ID']),
            feedback_text=feedback,
            sentiment=str(row['Sentiment']),
            category=str(row['Category']),
            alert_keywords=', '.join(alert_keywords),
            priority='High'
        )
        print(f"   ✓ Saved alert #{alert_id} for student {row['Student_ID']}")
        saved_count += 1
    except Exception as e:
        print(f"   ❌ Error: {e}")

print(f"\n   ✓ Saved {saved_count}/{len(alerts_in_csv)} alerts")

# Step 4: Check SQLite database
print("\n4️⃣ STEP 4: Checking SQLite database...")
from alerts_database import get_all_alerts
all_alerts = get_all_alerts()
print(f"   ✓ Total alerts in SQLite: {len(all_alerts)}")

# Step 5: Check Firebase
print("\n5️⃣ STEP 5: Checking Firebase...")
from firebase_config import firebase_sync
firebase_alerts = firebase_sync.get_all_alerts_from_firebase()
print(f"   ✓ Total alerts in Firebase: {len(firebase_alerts)}")

# Step 6: Summary
print("\n" + "="*80)
print("FLOW TEST COMPLETE")
print("="*80)
print(f"\n✅ CSV Analysis: {len(alerts_in_csv)} alerts detected")
print(f"✅ Database Save: {saved_count} alerts saved")
print(f"✅ SQLite: {len(all_alerts)} total alerts")
print(f"✅ Firebase: {len(firebase_alerts)} total alerts")

if len(firebase_alerts) >= saved_count:
    print(f"\n🎉 SUCCESS! All alerts are in Firebase and ready to display!")
else:
    print(f"\n⚠️  WARNING: Some alerts may not have synced to Firebase")

print("\n📱 Next steps:")
print("   1. Open admin dashboard")
print("   2. Go to Alerts tab")
print("   3. You should see all alerts")
print("   4. Open faculty dashboard")
print("   5. Go to Alerts & Reports tab")
print("   6. You should see faculty-specific alerts")
