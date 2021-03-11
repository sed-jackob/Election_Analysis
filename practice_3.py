voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

'''   
for i in range(len(voting_data)):
    print(f'{voting_data[i]["county"]} county has {voting_data[i]["registered_voters"]} registered voters')
'''
for eachVotingData in voting_data:
    text1 = eachVotingData["county"]
    text2 = eachVotingData["registered_voters"]
    print(f"{text1} county has {text2} registered voters.")