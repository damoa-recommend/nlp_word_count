from konlpy.tag import Okt
import re

okt = Okt()

sentence = '''가장 대표적인 것이 ‘빨리 감기’다. 1시간짜리 수업을 1분여만에 다 들을 수 있도록 해주는 것이다. 인터넷 커뮤니티 등에서는 "EBS 온라인 클래스 100배속 하는 법"하는 것과 같은 글이 공유되고 있다. 이 글에는 "수업 듣기 싫은데 일수는 채워야 하는 친구들 이 코드로 째버리자" "학교 공부대신 자바스크립트(프로그래밍 언어) 공부하러 가야지" 등의 댓글이 달렸다.'''
sentence = '''정부가 발표하는 물가상승률과 소비자가 느끼는 물가상승률은 다르다.'''

def Bow(sentence, word_2_idx={}, **kargs) :
  sentence = sentence.replace("\‘", '')
  sentence = sentence.replace("’", '')
  sentence = sentence.replace("‘", '')
  sentence = sentence.replace('"', '')
  sentence = sentence.replace('"', '')
  sentence = sentence.replace("(", '')
  sentence = sentence.replace(")", '')
  sentence = sentence.replace(".", '')
  
  split_type = kargs.get('split_type', 0)
  if not split_type:
    token=okt.morphs(sentence)  
  else :
    token=okt.nouns(sentence)  

  # print(token)

  word_2_idx = word_2_idx
  bow = [0 for word in word_2_idx.keys()]

  for voca in token:
    if not word_2_idx.get(voca, None):
      word_2_idx[voca] = len(bow)
      bow.append(1)
    else:
      bow[word_2_idx[voca]] += 1
  return word_2_idx, bow

if __name__ == "__main__":

  w2i, bow = Bow(sentence, {}, split_type=1) # split_type: 0이면 형태로, 1이면 명사사용

  print(w2i)
  print(bow)
  print()

  w2i, bow = Bow('1시간짜리 수업을 1분여만에 다 들을 수 있도록 해주는 것이다.', w2i, split_type=1) # split_type: 0이면 형태로, 1이면 명사사용

  print(w2i)
  print(bow)
  print()

  w2i, bow = Bow('인터넷 커뮤니티 등에서는 "EBS 온라인 클래스 100배속 하는 법"하는 것과 같은 글이 공유되고 있다.', w2i, split_type=1) # split_type: 0이면 형태로, 1이면 명사사용

  print(w2i)
  print(bow)
  print()


  w2i, bow = Bow('정부가 발표하는 물가상승률과 소비자가 느끼는 물가상승률은 다르다.', {}, split_type=1) # split_type: 0이면 형태로, 1이면 명사사용

  print(w2i)
  print(bow)