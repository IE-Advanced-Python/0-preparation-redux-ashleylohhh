def stopword_removal(sentence):
  import nltk
  nltk.download('punkt')
  sentence = nltk.word_tokenize(sentence)
  stopwords = ["a", "the", "or", "and"]
  list1 = [x for x in sentence if x not in stopwords]
  return list1

def punctuation_removal(sentence):
  import nltk
  nltk.download('punkt')
  sentence = nltk.word_tokenize(sentence)
  punctuation = [".", ",", "!"]
  list2 = [x for x in sentence if x not in punctuation]
  return list2