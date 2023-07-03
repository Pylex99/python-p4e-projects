# The purpose of this program is to read an email file, extract the domain from each "From:" line, and store the counts of each domain in a SQLite database. The program creates a database table called "Counts" with columns "org" (representing the domain) and "count" (representing the number of occurrences). It then reads through the file, updates the counts in the database, and finally retrieves and prints the top 10 domains with the highest counts.

import sqlite3

# Establish a connection to the SQLite database
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Drop the "Counts" table if it already exists
cur.execute('DROP TABLE IF EXISTS Counts')

# Create the "Counts" table with columns "org" (text) and "count" (integer)
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

# Prompt the user for the file name and open the file
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox.txt'
fh = open(fname)

# Read through the file line by line
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    domain = email.split("@")[1]

    # Check if the domain already exists in the database
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain,))
    row = cur.fetchone()

    if row is None:
        # If the domain doesn't exist, insert a new row with count=1
        cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (domain,))
    else:
        # If the domain already exists, update the count by incrementing it by 1
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain,))

# Commit the changes to the database
conn.commit()

# Retrieve the top 10 rows from the "Counts" table based on count, in descending order
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

# Execute the SQL query and print the results
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

# Close the cursor and the database connection
cur.close()
