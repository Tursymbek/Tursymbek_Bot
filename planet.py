import ephem
from datetime import datetime 

user_planet = "Jupiter"

planet = getattr(ephem, user_planet)()
planet.compute(ephem.Date(datetime.now()))
result = ephem.constellation(planet)
print(result)

if  update.message.text.split() == "Mars":
        u = ephem.Mars()
        dt_now = datetime.now()
        u.compute(dt_now)
        rpl = ephem.constellation(u)
        rpl1 = str(rpl)
        update.message.reply_text(rpl1)
    elif  update.message.text.split() == "Mercury":
        u = ephem.Mercury()
        dt_now = datetime.now()
        u.compute(dt_now)
        rpl = ephem.constellation(u)
        rpl1 = str(rpl)
        update.message.reply_text(rpl1)
    elif  update.message.text.split() == "Venus":
        u = ephem.Venus()
        dt_now = datetime.now()
        u.compute(dt_now)
        rpl = ephem.constellation(u)
        rpl1 = str(rpl)
        update.message.reply_text(rpl1)
    elif  update.message.text.split() == "Jupiter":
        u = ephem.Jupiter()
        dt_now = datetime.now()
        u.compute(dt_now)
        rpl = ephem.constellation(u)
        rpl1 = str(rpl)
        update.message.reply_text(rpl1)
    elif  update.message.text.split() == "Saturn":
        u = ephem.Saturn()
        dt_now = datetime.now()
        u.compute(dt_now)
        rpl = ephem.constellation(u)
        rpl1 = str(rpl)
        update.message.reply_text(rpl1)
    elif  update.message.text.split() == "Uranus":
        u = ephem.Uranus()
        dt_now = datetime.now()
        u.compute(dt_now)
        rpl = ephem.constellation(u)
        rpl1 = str(rpl)
        update.message.reply_text(rpl1)
    elif  update.message.text.split() == "Neptune":
        u = ephem.Neptune()
        dt_now = datetime.now()
        u.compute(dt_now)
        rpl = ephem.constellation(u)
        rpl1 = str(rpl)
        update.message.reply_text(rpl1)
    elif  update.message.text.split() == "Pluto":
        u = ephem.Pluro()
        dt_now = datetime.now()
        u.compute(dt_now)
        rpl = ephem.constellation(u)
        rpl1 = str(rpl)
        update.message.reply_text(rpl1)
    elif  update.message.text.split() == "Sun":
        u = ephem.Sun()
        dt_now = datetime.now()
        u.compute(dt_now)
        rpl = ephem.constellation(u)
        rpl1 = str(rpl)
        update.message.reply_text(rpl1)
    elif  update.message.text.split() == "Moon":
        u = ephem.Moon()
        dt_now = datetime.now()
        u.compute(dt_now)
        rpl = ephem.constellation(u)
        rpl1 = str(rpl)
        update.message.reply_text(rpl1)