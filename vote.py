candidate1=input("Enter The Nominee 1 name: ")
candidate2=input("Enter The Nominee 2 name: ")

can1votes=0
can2votes=0
votes_id=[1,2,3,4,5,6,7,8,9,10]
num_of_votes=len(votes_id)
while True:
  if votes_id==[]:
    print("Your voting session is completed")
    if can1votes>can2votes:
      percentage=(can1votes/can2votes)*100
      print("CANDIDATE 1 HAS WON","with",percentage,"% votes")
      break

    elif can2votes>can1votes:
      percentage=(can2votes/can1votes)*100
      print("CANDIDATE 2 HAS WON","with",percentage,"% votes")
      break

  else:
    voter=int(input("Enter Your voter id no: "))
    if voter in votes_id:
      print("YOU ARE A VOTER!")
      votes_id.remove(voter)
      vote=int(input("Enter Your Vote for Candidate1 or Candidate2: "))
      if vote==1:
        can1votes+=1
        print("THANKYOU FOR CASTING YOUR VOTE")
      
      elif vote==2:
        can2votes+=1
        print("THANKYOU FOR CASTING YOUR VOTE")

    else:
      print("YOU HAVE ALREADY VOTED OR YOU ARE NOT A VOTER")
