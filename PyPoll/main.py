import csv

# Read election data from the CSV file
data = csv.reader(open('Resources/election_data.csv'))
    
next(data)  # aka skip the header row

total_votes = 0
candidates = {}

for row in data:
    candidate = row[2]
    total_votes += 1
    candidates[candidate] = candidates.get(candidate, 0) + 1

# Calculate the % of votes each candidate won
results = []
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results.append((candidate, percentage, votes))

# Winner based on popular vote
winner = max(results, key=lambda x: x[2])

# Print the output
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, percentage, votes in results:
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner[0]}")
print("-------------------------")