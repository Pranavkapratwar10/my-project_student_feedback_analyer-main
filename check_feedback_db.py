import sqlite3

conn = sqlite3.connect('feedback_analysis.db')
cursor = conn.cursor()

# Check total entries
cursor.execute('SELECT COUNT(*) FROM feedback_analysis')
total = cursor.fetchone()[0]
print(f'Total feedback entries: {total}')

if total > 0:
    # Get recent entries
    cursor.execute('''
        SELECT id, student_id, faculty_id, sentiment, category, created_at 
        FROM feedback_analysis 
        ORDER BY created_at DESC 
        LIMIT 10
    ''')
    
    print('\nRecent entries:')
    print('-' * 80)
    for row in cursor.fetchall():
        print(f'ID: {row[0]}, Student: {row[1]}, Faculty ID: {row[2]}, Sentiment: {row[3]}, Category: {row[4]}, Date: {row[5]}')
else:
    print('\n⚠️ No feedback entries found in database!')

conn.close()
