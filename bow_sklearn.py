from sklearn.feature_extraction.text import CountVectorizer
corpus = ['''가장 대표적인 것이 ‘빨리 감기’다. 1시간짜리 수업을 1분여만에 다 들을 수 있도록 해주는 것이다. 인터넷 커뮤니티 등에서는 "EBS 온라인 클래스 100배속 하는 법"하는 것과 같은 글이 공유되고 있다. 이 글에는 "수업 듣기 싫은데 일수는 채워야 하는 친구들 이 코드로 째버리자" "학교 공부대신 자바스크립트(프로그래밍 언어) 공부하러 가야지" 등의 댓글이 달렸다.''']
corpus = ['''정부가 발표하는 물가상승률과 소비자가 느끼는 물가상승률은 다르다.''']

vector = CountVectorizer()
print(vector.fit_transform(corpus).toarray()) # 코퍼스로부터 각 단어의 빈도 수를 기록한다.
print(vector.vocabulary_)