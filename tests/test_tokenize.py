import sys
sys.path.append('src')
#sys.path.insert(0, '../src/')
from ie_nlp_utils import tokenize

def test_tokenize_returns_expected_output():
  sentence1 = "This is a sentence"
  expected_output1 = ["This", "is", "a", "sentence"]

  output1 = tokenize(sentence1)

  assert output1 == expected_output1

  sentence2 = "Another short sentence"
  expected_output2 = ["Another", "short", "sentence"]

  output2 = tokenize(sentence2)

  assert output2 == expected_output2

def test_tokenize_lower_returns_expected_output():
  sentence1= "This is a sentence"
  expected_output1 = ["this", "is", "a", "sentence"]

  output1 = tokenize(sentence1, lower=True)

  assert output1 == expected_output1

  sentence2 = "Another short sentence"
  expected_output2 = ["another", "short", "sentence"]

  output2 = tokenize(sentence2, lower=True)

  assert output2 == expected_output2