#!/usr/bin/env python3
import os
import shutil
import sqlite3

# Chrome history file
home=os.environ.get('HOME')

history_file = home + '/Library/Application Support/Google/Chrome/Default/History'  # macOS'
print("History file: " + history_file)

# copy the file because its locked if chrome is currently open
copied_file = home + '/data/copied_history'

shutil.copy2(history_file, copied_file)

# Connect to the database
conn = sqlite3.connect(copied_file)
cursor = conn.cursor()

# Query the history
cursor.execute("""
    SELECT url, title, visit_count, last_visit_time
    FROM urls
    ORDER BY last_visit_time DESC
""")

results = cursor.fetchall()
for row in results:
	print(row)

conn.close()
os.remove(copied_file)
