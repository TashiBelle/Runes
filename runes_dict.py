import random 

# add file paths to pngs later 
  # "sprite": "Macintosh HD/Users/dawson/Desktop/Custom Device Images/<name>.png"
runes = {
  "FEHU": {
    "phonetic": "F",
    "number": 1,
    "bright": ["social success", "wealth energy", "foresight", "new beginnings"],
    "murky": ["greed", "burnout", "atrophy", "poverty", "discord"]
  },
  "URUZ": {
    "phonetic": "U",
    "number": 2,
    "bright": ["strength", "defense", "tenacity", "freedom", "form", "health", "understanding"],
    "murky": ["weakness", "obsession", "misdirected force", "domination by others", "sickness", "inconsistency", "ignorance"]
  },
  "THURISAZ": {
    "phonetic": "TH",
    "number": 3,
    "bright": ["reactive force", "directed force", "vital eroticism", "regenerative catalyst"],
    "murky": ["danger", "defenselessness", "compulsion", "betrayal", "dullness"]
  },
  "ANSUZ": {
    "phonetic": "A",
    "number": 4,
    "bright": ["inspiration (enthusiasm)", "synthesis", "transformation", "words"],
    "murky": ["misunderstanding", "delusion", "manipulation by others", "boredom"]
  },
  "RAIDHO": {
    "phonetic": "R",
    "number": 5,
    "bright": ["rationality", "action", "justice", "ordered growth", "journey"],
    "murky": ["crisis", "rigidity", "stasis", "injustice", "irrationality"]
  },
  "KENAZ": {
    "phonetic": "K",
    "number": 6,
    "bright": ["technical ability", "inspiration", "creativity", "transformation", "offspring"],
    "murky": ["disease", "breakup", "inability", "lack of creativity"]
  },
  "GEBO": {
    "phonetic": "G",
    "number": 7,
    "bright": ["gift giving", "generosity", "magical exchange", "honor", "sacrifice"],
    "murky": ["influence-buying", "greed", "loneliness", "dependence", "over-sacrifice"]
  },
  "WUNJO": {
    "phonetic": "W",
    "number": 8,
    "bright": ["harmony", "joy", "fellowship", "prosperity"],
    "murky": ["stultification", "sorrow", "strife", "alienation"]
  },
  "HAGALAZ": {
    "phonetic": "H",
    "number": 9,
    "bright": ["change according to ideals", "controlled crisis", "completion", "inner harmony"],
    "murky": ["catastrophe", "crisis", "stagnation", "loss of power"]
  },
  "NAUTHIZ": {
    "phonetic": "N",
    "number": 10,
    "bright": ["resistance leading to strength", "recognition", "innovation", "need-fire", "self-reliance"],
    "murky": ["constraint of freedom", "distress", "toil", "drudgery", "laxity"]
  },
  "ISA": {
    "phonetic": "I",
    "number": 11,
    "bright": ["concentrated self", "ego", "consciousness", "self-control", "unity"],
    "murky": ["ego-mania", "dullness", "blindness", "dissipation"]
  },
  "JERA": {
    "phonetic": "J/Y",
    "number": 12,
    "bright": ["reward", "plenty", "peace", "proper timing"],
    "murky": ["repetition", "bad timing", "poverty", "conflict"]
  },
  "EIHWAZ": {
    "phonetic": "E/I",
    "number": 13,
    "bright": ["enlightenment", "endurance", "initiation", "protection"],
    "murky": ["confusion", "destruction", "dissatisfaction", "weakness"]
  },
  "PERTHRO": {
    "phonetic": "P",
    "number": 14,
    "bright": ["good lot", "knowledge", "fellowship", "joy", "evolutionary change"],
    "murky": ["addiction", "stagnation", "loneliness", "malaise"]
  },
  "ELHAZ": {
    "phonetic": "Z",
    "number": 15,
    "bright": ["connection with the gods", "awakening", "higher life", "protection"],
    "murky": ["hidden danger", "consumption by divine forces", "loss of divine link"]
  },
  "SOWILO": {
    "phonetic": "S",
    "number": 16,
    "bright": ["guidance", "hope", "success", "goals achieved", "honor"],
    "murky": ["false goals", "bad counsel", "false success", "gullibility", "loss of goals"]
  },
  "TIWAZ": {
    "phonetic": "T",
    "number": 17,
    "bright": ["justice", "rationality", "self-sacrifice", "analysis"],
    "murky": ["mental paralysis", "over-analysis", "over-sacrifice", "injustice", "imbalance"]
  },
  "BERKANO": {
    "phonetic": "B",
    "number": 18,
    "bright": ["birth", "becoming", "life changes", "shelter", "liberation"],
    "murky": ["blurring of consciousness", "deceit", "sterility", "stagnation"]
  },
  "EHWAZ": {
    "phonetic": "E",
    "number": 19,
    "bright": ["harmony", "teamwork", "trust", "loyalty"],
    "murky": ["duplication", "disharmony", "mistrust", "betrayal"]
  },
  "MANNAZ": {
    "phonetic": "M",
    "number": 20,
    "bright": ["divine structure", "intelligence", "awareness", "social order"],
    "murky": ["depression", "mortality", "blindness", "self-delusion"]
  },
  "LAGUZ": {
    "phonetic": "L",
    "number": 21,
    "bright": ["life", "'water' journey", "sea of vitality", "sea of unconscious", "growth"],
    "murky": ["fear", "circular motion", "avoidance", "withering"]
  },
  "INGWAZ": {
    "phonetic": "NG",
    "number": 22,
    "bright": ["rest stage", "internal growth", "gestation"],
    "murky": ["impotence", "scattering", "movement without change"]
  },
  "DAGAZ": {
    "phonetic": "D",
    "number": 23,
    "bright": ["awakening", "awareness", "hope", "happiness", "the ideal"],
    "murky": ["blindness", "hopelessness"]
  },
  "OTHALA": {
    "phonetic": "O",
    "number": 24,
    "bright": ["home", "group prosperity", "group order", "freedom", "productive interaction"],
    "murky": ["lack of customary order", "totalitarianism", "slavery", "poverty", "homelessness"]
  }
}

# makes it so the menu is called at the beginning of each loop in the main branch
def runes_menu():
  choice = input("\nType 'L' to view the list of runes. \nType 'S' to cast a single rune. \nType 'T' to cast three runes. \nType 'Q' to quit.\n--> ").upper()
  return choice 

# lists all rune names and asks user to select one; returns all info on selected rune
def list_runes():
  for rune in runes:
    print(rune)
  while True:
    list_choice = input("\nWould you like more info on a specific rune? (y/n) -->").lower()
    if list_choice == "y":
      list_sel = input("\nType name of rune to select: ").upper()
      if list_sel in runes:
        print(f"\nRune: {list_sel}")
        for key, value in runes[list_sel].items():
          print(f"{key.capitalize()}: {value}")
            # for each value, print with comma separation
      else:
        print("\nThat's not a rune, silly.")
    elif list_choice == "n":
      print("\nCool cool.\n")
      break
    else:
      print("\nTry again!")

# randomly throw a single rune by name; ask user if they would like more info, cast again, return to menu, or quit
def cast1():
  rune_names = list(runes.keys())
  cast1_rune = random.choice(rune_names)
  cast1_info = runes[cast1_rune]

  while True:
    print(f"\n{cast1_rune}\n")
    while True:
      cast1_choice = input("Type 'I' for more info on this rune. \nType 'C' to cast again. \nType 'M' to return to the menu. \nType 'Q' to quit. \n--> ").upper()
      if cast1_choice == 'I':
        print(f"\n{cast1_rune}")
        for key, value in cast1_info.items():
          if isinstance(value, list):
            clean_list = ", ".join(value)
            print(f"{key.capitalize()}: {clean_list}")
          else:
            print(f"{key.capitalize()}: {value}")
                # fixing so that each key is on a new line & capitalized all nice
        print("\n")
      elif cast1_choice == 'C':
        break
      elif cast1_choice == 'M':
        return
      elif cast1_choice == 'Q':
        quit()
      else:
        print("\nUm...what?\n")

#randomly throw 3 runes by name; ask user if they would like more info on any
  # if yes - prompt user to input rune name they would like more info about
    # return with info on selection
    # ask if user would like to go back for more info
      # if yes (would like to return), return list of previously thrown runes; ask user which one; repeat
      # if no - return to options
  # if no - return to options
def cast3():
  print("\nTriple cast randomizer coming soon!\n")

# prompt user to input if they would like to pick from the list, throw 1, or throw 3; continue to correct line
while True: 
  choice = runes_menu()
  if choice == "L":
    list_runes()
  elif choice == "S":
    cast1()
  elif choice == "T":
    cast3()
  elif choice == "Q":
    quit()
  else:
    print("\nNo no no!\n")
