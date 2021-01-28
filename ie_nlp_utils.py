def tokenize(sentence, lower=False):
  if lower:
    return sentence.lower().split()
  return sentence.split()