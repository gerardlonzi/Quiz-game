import requests

params = {
    'amount':'10',
    'difficulty':'hard',
    'type':'boolean'
}
requet =requests.get(url='https://opentdb.com/api.php',params=params)
requet.raise_for_status()
data = requet.json()['results']

question_response = [(i['question'],i['correct_answer']) for i in data]
 
p = q =0
score = 0
win_question =0
while True:
  print(f"score :{score}")
  question = question_response[p][0]
  reponse = (question_response[p][1]).lower()
  
  print(f"questons : {p+1}/{len(question_response)}")
  print(f"vous avex trouve :{q}/{win_question}")
  
  user_reponse =  input(f"Q.{p+1}: {question} (true/false) ?")
  
  if user_reponse.lower() == (reponse).lower():
      print('vous avez reussir')
      score+=1
      q+=1
      
  else:
      print('vous avez rater')    
  win_question+=1
  p+=1
