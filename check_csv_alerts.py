import pandas as pd

# Check the analyzed CSV
df = pd.read_csv('uploads/analyzed_student_feedback.csv')

print(f"Total rows: {len(df)}")
print(f"\nAlert column values:")
print(df['Alert'].value_counts())

print(f"\nRows with Alert=Yes:")
alert_rows = df[df['Alert'] == 'Yes']
if len(alert_rows) > 0:
    for idx, row in alert_rows.iterrows():
        print(f"  Student: {row['Student_ID']}")
        print(f"  Feedback: {row['Feedback'][:100]}...")
        print()
else:
    print("  No alerts found!")

print(f"\nSample feedback (first 5 rows):")
for i, row in df.head(5).iterrows():
    feedback = str(row['Feedback'])
    print(f"\n{i+1}. Student: {row['Student_ID']}")
    print(f"   Feedback: {feedback[:150]}...")
    print(f"   Alert: {row['Alert']}")
    
    # Check if keywords are present
    keywords = ["harassment", "discrimination", "unsafe", "abuse", "bullying", "threat", "violence"]
    found_keywords = [kw for kw in keywords if kw in feedback.lower()]
    if found_keywords:
        print(f"   ⚠️ Keywords found but not flagged: {found_keywords}")
