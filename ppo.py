candidates = ["paul", "eve", "solomon", "peter"]
paul = []
eve = []
solomon = []
peter = []

def find_leader(paul_votes, eve_votes, solomon_votes, peter_votes):

    winner = []  
    Top = max(paul_votes, eve_votes, solomon_votes, peter_votes)
    
    if paul_votes == Top:
        winner.append("paul")  
    if eve_votes == Top:
        winner.append("eve")   
    if solomon_votes == Top:
        winner.append("solomon")  
    if peter_votes == Top:
        winner.append("peter")    
    
    return winner, Top  

while True:
    
    print("Voting system")
    
    
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    
    if age < 18:
        print("Not allowed to vote")
        continue

    print("\nCandidates:")
    for a_num in range(0, 4):
        print(f'Choose {a_num+1} to vote for {candidates[a_num]}')
    print("Choose 5 to see the leading candidate")
    print("Press 0 to Exit")
    
    choice = int(input("Your choice: "))
    
    if choice == 0:
        print("FINAL RESULTS:")
        print(f"paul: {len(paul)} votes")
        print(f"eve: {len(eve)} votes")
        print(f"solomon: {len(solomon)} votes")
        print(f"peter: {len(peter)} votes")
        
        
        winner, Top = find_leader(len(paul), len(eve), len(solomon), len(peter))
        
        if len(winner) == 1:
            print(f"\nWINNER: {winner[0]} with {Top} votes!")
        else:
            print(f"\nTIE! Winners: {', '.join(winner)} with {Top} votes each")
        
        print("Thank you for voting!")
        break
    
    elif choice == 1:
        paul.append(f"{name} {age}")
        print(f'\n{name} voted for {candidates[0]}')
        print(f"paul: {len(paul)} votes")
        print(f"eve: {len(eve)} votes")
        print(f"solomon: {len(solomon)} votes")
        print(f"peter: {len(peter)} votes")
    
    elif choice == 2:
        eve.append(f"{name} {age}")
        print(f'\n{name} voted for {candidates[1]}')
        print(f"paul: {len(paul)} votes")
        print(f"eve: {len(eve)} votes")
        print(f"solomon: {len(solomon)} votes")
        print(f"peter: {len(peter)} votes")
    
    elif choice == 3:
        solomon.append(f"{name} {age}")
        print(f'\n{name} voted for {candidates[2]}')
        print(f"paul: {len(paul)} votes")
        print(f"eve: {len(eve)} votes")
        print(f"solomon: {len(solomon)} votes")
        print(f"peter: {len(peter)} votes")
    
    elif choice == 4:
        peter.append(f"{name} {age}")
        print(f'\n{name} voted for {candidates[3]}')
        print(f"paul: {len(paul)} votes")
        print(f"eve: {len(eve)} votes")
        print(f"solomon: {len(solomon)} votes")
        print(f"peter: {len(peter)} votes")
    
    elif choice == 5:
        
        winner, Top = find_leader(len(paul), len(eve), len(solomon), len(peter))
        
        print("\n" + "="*50)
        print("CURRENT VOTE COUNT:")
        print("="*50)
        print(f"paul: {len(paul)} votes")
        print(f"eve: {len(eve)} votes")
        print(f"solomon: {len(solomon)} votes")
        print(f"peter: {len(peter)} votes")
        print("="*50)
        
        if len(winner) == 1:
            print(f"The leading candidate is: {winner[0]} with {Top} votes")
        else:
            print(f"There's a tie! Leading candidates are: {', '.join(winner)} with {Top} votes each")
    
    else:
        print("Invalid choice! Please enter 0-5.")