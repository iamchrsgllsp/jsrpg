from flask import Flask, render_template, request
import json
from random import randint
from enemies import enemylist
from mobs import mobslist
from character import get_char
import os
import stats

app = Flask(__name__, static_folder="static")
userxp = 100
prog = 0


@app.route("/sessionprogress", methods=["GET", "POST"])
def sessionprogress():
  global prog
  global userxp
  if request.method == "POST":
    if request.json is None:
      return "Invalid JSON"
    else:
      data = request.json
      loot = data['loot']
      xp = data['xp']
      print(loot)
      print(xp)
      userxp = userxp + xp
      prog += 1
      print(prog)
      print(userxp)
      return request.data
  else:
    return "Invalid Method"


@app.route("/orbit")
def orbit():
  with open("/home/runner/jsrpg/static/assets/planets.json") as file:
    planets = json.load(file)
    planets = planets["planets"]
  return render_template("orbit.html", planets=planets, prog=prog)


@app.route("/planet/<planet>")
def dest(planet):
  activities = []
  with open("/home/runner/jsrpg/static/assets/planets.json") as file:
    planets = json.load(file)
    planets = planets["planets"]
    destination = None  # Initialize destination variable outside the loop
    for area in planets:
      if area["id"] == planet:
        destination = area
        break  # Add break once the planet is found to exit the loop
    if destination:
      with open("/home/runner/jsrpg/static/assets/activities.json") as file:
        act = json.load(file)
        for a in destination.get("activities", []):
          activities.append(act[str(a)])
      return render_template("activities.html",
                             activities=activities,
                             planet=planet)
    else:
      return "Planet not found"  # Handle the case when the planet is not found


@app.route('/game/<planet>/<activity>')
def index(planet, activity):
  global prog
  print(planet)
  character = stats.find_lvl("warlock", userxp)
  print(character)
  if prog < 10:
    selenemy = mobslist[randint(0, len(enemylist) - 1)]
  elif activity == "patrol":
    print("patrol")
    selenemy = mobslist[randint(0, len(enemylist) - 1)]
  else:
    selenemy = enemylist[randint(0, len(enemylist) - 1)]
  return render_template("home.html",
                         char=character,
                         enemy=selenemy,
                         planet=planet,
                         activity=activity)


#app.run(host='0.0.0.0', port=80)
