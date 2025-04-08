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
    "murky: ["blurring of consciousness", "deceit", "sterility", "stagnation"]
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

# list all rune names and ask user to select one; return all info on selected rune; enter 'back' to return to options
def list_runes():
  print("\n")
  for rune in runes:
    print(rune)
  list_sel = input("\nType name of rune to select: ").upper()
  if list_sel in runes:
    print(f"\nRune: {list_sel}")
    for key, value in runes[list_sel].items():
      print(f"{key.capitalize()}: {value}")
      # for each value, print with comma separation
    print("\n")
  else:
    print("\nThat's not a rune, silly.\n")
      # go back and let them try again

# randomly throw a single rune by name; ask user if they would like more info
  # if yes - return all info on rune
  # if no - return to options
def cast1():
  print("\nSingle cast randomizer coming soon!\n")

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
  choice = input("Type '1' to view the list of runes. \nType '2' to cast one rune. \nType '3' to cast three runes. \n\n--> ")
  if choice == "1":
    list_runes()
  elif choice == "2":
    cast1()
  elif choice == "3":
    cast3()
  else:
    # restart from 'choice = input' ask
    print("\nNo no no!\n")
