import json

class Highscore:
    def __init__(self):
        self.score = json.loads(open("assets/highscore.json").read()) #for string
      self.score = {'score':'user_time'}
      with open('highscore.txt', 'w') as HS_FILE:
        json.dump(self.score, HS_FILE)
      with open("highscore.txt") as HS_FILE:
        data = json.load(HS_FILE)
      
      