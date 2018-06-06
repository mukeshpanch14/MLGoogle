import time
from pycricbuzz import Cricbuzz
c=Cricbuzz()
#for match in c.matches():
 # print(match)
  

while True:
  m=dict(c.livescore(1))
  print('{} Runs {}, Overs {}, Wickets {}'.format(m['batting']['team'],m['batting']['score'][0]['runs'],m['batting']['score'][0]['overs'],m['batting']['score'][0]['wickets']))
  time.sleep(30)