import ephem
from datetime import datetime 

user_planet = ['sapd', 'Moon']
    
u = getattr(ephem, user_planet[1])
tm = datetime.now()
star_in = u(tm)
result = ephem.constellation(star_in)
print(result)

