import sys
sys.path.append('src')
#sys.path.insert(0, '../src/')
from ie_nlp_utils import stopword_removal, punctuation_removal

def test_removal_returns_expected_output():
  sentence = "Once upon a time, Eleonora and Ashley were best friends!"

  expected_output1 = ['Once', 'upon', 'time', ',', 'Eleonora', 'Ashley', 'were', 'best', 'friends', '!']
  output1 = stopword_removal(sentence)
  assert output1 == expected_output1

  expected_output2 = ['Once', 'upon', 'a', 'time', 'Eleonora', 'and', 'Ashley', 'were', 'best', 'friends']
  output2 = punctuation_removal(sentence)
  assert output2 == expected_output2