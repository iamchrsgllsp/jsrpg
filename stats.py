import json


def load_level_data(filename):
  with open(filename, "r") as file:
    return json.load(file)


def find_lvl(chr, xp, filename="/home/runner/jsrpg/static/assets/levels.json"):
  mx = []
  levels = load_level_data(filename)
  data = levels.get(chr)
  for it, i in enumerate(data):
    if xp > data[i]['xp']:
      mx.append(it + 1)
    else:
      continue

  return data[str(max(mx))]


# Example usage
