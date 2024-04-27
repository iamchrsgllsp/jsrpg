import json


def get_inv(char):
  with open("/home/runner/jsrpg/static/assets/inventory.json") as file:
    inv = json.load(file)
    inv = inv[char]
    return inv


def get_char():
  character = {
      "name":
      "Jack",
      "inventory":
      get_inv("testuser"),
      "lvl":3,
      "hp":
      100,
      "atk":
      14,
      "mag":
      16,
      "def":
      4,
      "ultimate":
      "Shadowshot",
      "abilities": [{
          "name": "Heal",
          "cost": 10,
          "heal": 10
      }, {
          "name": "Fireball",
          "cost": 20,
          "dmg": 20
      }]
  }
  return character
