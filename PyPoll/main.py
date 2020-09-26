import os
import csv
pypoll = os.path.join("resources", "election_data.csv")

voters = []
candidates = []
unique_names = []

with open(pypoll, "r") as pypoll_file:
    pypoll_reader = csv.reader(pypoll_file, delimiter = ',')
    pypoll_header = next(pypoll_reader)
    for votes in pypoll_reader:
        voters.append(votes) #List out all votes
        candidates.append(votes[2])
        candidate = votes[2] #Declare which column our candidates are in
    for name in candidates:
        if name not in unique_names: 
            unique_names.append(name) #add name into this variable only if not already there

total_voters = len(voters) #Calculate # of total votes
winner = max(set(candidates), key = candidates.count) #Calculate the name w/ most occurrences

print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_voters}")
print(f"----------------------------")
for names in unique_names:
    print(f"{names}: {round((candidates.count(names)/(total_voters))*100): .3f}% ({candidates.count(names)})")
print(f"----------------------------")
print(f"Winner: {winner}")
print(f"----------------------------")

pypoll_analysis = os.path.join("analysis", "election_results.txt") #Export to .txt file
with open(pypoll_analysis, "w") as pypoll_final:
    pypoll_final.write(f"Election Results")
    pypoll_final.write("\n")
    pypoll_final.write(f"----------------------------")
    pypoll_final.write("\n")
    pypoll_final.write(f"Total Votes: {total_voters}")
    pypoll_final.write("\n")
    pypoll_final.write(f"----------------------------")
    pypoll_final.write("\n")
    pypoll_final.write(f"{unique_names[0]}: {round((candidates.count('Khan')/(total_voters))*100): .3f}% ({candidates.count('Khan')})")
    pypoll_final.write("\n")
    pypoll_final.write(f"{unique_names[1]}: {round((candidates.count('Correy')/(total_voters))*100): .3f}% ({candidates.count('Correy')})")
    pypoll_final.write("\n")
    pypoll_final.write(f"{unique_names[2]}: {round((candidates.count('Li')/(total_voters))*100): .3f}% ({candidates.count('Li')})")
    pypoll_final.write("\n")
    pypoll_final.write(f"""{unique_names[3]}: {round((candidates.count("O'Tooley")/(total_voters))*100): .3f}% ({candidates.count("O'Tooley")})""")
    pypoll_final.write("\n")
    pypoll_final.write(f"----------------------------")
    pypoll_final.write("\n")
    pypoll_final.write(f"Winner: {winner}")
    pypoll_final.write("\n")
    pypoll_final.write(f"----------------------------")