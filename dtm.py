from bow import Bow
import pandas as pd
import numpy as np
from operator import itemgetter

if __name__ == "__main__":

  sentences = [
    '''가장 대표적인 것이 ‘빨리 감기’다. 1시간짜리 수업을 1분여만에 다 들을 수 있도록 해주는 것이다. 인터넷 커뮤니티 등에서는 "EBS 온라인 클래스 100배속 하는 법"하는 것과 같은 글이 공유되고 있다. 이 글에는 "수업 듣기 싫은데 일수는 채워야 하는 친구들 이 코드로 째버리자" "학교 공부대신 자바스크립트(프로그래밍 언어) 공부하러 가야지" 등의 댓글이 달렸다.''',
    '''1시간짜리 수업을 1분여만에 다 들을 수 있도록 해주는 것이다.''',
    '''인터넷 커뮤니티 등에서는 "EBS 온라인 클래스 100배속 하는 법"하는 것과 같은 글이 공유되고 있다.''',
  ]

  w2i = {}
  bows = []

  for sentence in sentences:
    w2i, bow = Bow(sentence, w2i, split_type=1)
    bows.append(bow)

  np_bows = np.array(bows)
  df = pd.DataFrame(np_bows, columns=[word[0] for word in sorted(w2i.items(),  key=lambda item: item[1])])
  print(df)
  df.to_csv('dtm.csv')

