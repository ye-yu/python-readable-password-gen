import secrets
import string

vowels = 'euioa'
consonants = [i for i in string.ascii_lowercase if i not in vowels]
beginning_cluster = [
  "qw",
  "qr",
  "qh",
  "ql",
  "wr",
  "wh",
  "rh",
  "tw",
  "tr",
  "th",
  "pw",
  "pr",
  "ph",
  "pl",
  "sw",
  "sr",
  "sh",
  "sl",
  "fw",
  "fr",
  "fh",
  "fl",
  "gw",
  "gr",
  "gh",
  "gl",
  "cw",
  "cr",
  "ch",
  "cl",
  "vw",
  "vr",
  "vh",
  "vl",
  "bw",
  "br",
  "bh",
  "bl",
]
beginning_cluster.extend(consonants)

ending_cluster = [
  "ng",
  "lt",
  ""
]
ending_cluster.extend(consonants)

def secureBoolean():
  return secrets.randbits(1) == 1

def secureChoose(bits):
  return secrets.randbits(bits) % bits

def getBeginningConsonant():
  return beginning_cluster[secureChoose(len(beginning_cluster))]

def getEndingConsonant():
  return ending_cluster[secureChoose(len(ending_cluster))]

def getVowel():
  return vowels[secureChoose(len(vowels))]

def getSyllable():
  return f"{getBeginningConsonant()}{getVowel()}{getEndingConsonant()}"

print(f"!1O{getSyllable()}{getSyllable()}-2{getSyllable()}{getSyllable()}")