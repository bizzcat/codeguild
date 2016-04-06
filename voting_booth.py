election = {}

vote = True
while vote:
    print ('Would you like to vote?')
    choice = input()

    if choice != 'no':
        print ('Who would you like to vote for?')
        answer = input()
        if answer in election:
            election[answer] += 1
        else:
            election[answer] = 1

    else:
        vote = False #this closes out the loop, because the loop is
                        #only active when vote = True

print ('Okay, now lets see the results!')
print (election)

highest_vote = max(election.values())

#when the value of the key is == to the max value

winner = (max(election, key=election.get))
sorter = (sorted(election, key=election.get, reverse=True))

print winner
