import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

df = pd.read_csv('./the-movies-dataset/movies_metadata.csv', low_memory=False)

# fillna는 Null값을 처리하는 메서드
# 아래 코드는 Null값을 빈 스트링으로 치환
def null_to_zero_padding(df, column):
  return df[column].fillna('')

def get_recommendations(title, cosine_sim, recommend_size=10):
    '''
    [
      [영화0 - 영화0 유사도, 영화0 - 영화1 유사도, 영화0 - 영화2 유사도, ... 영화0 - 영화n 유사도],
      [영화1 - 영화0 유사도, 영화1 - 영화1 유사도, 영화1 - 영화2 유사도, ... 영화1 - 영화n 유사도],
      [영화2 - 영화0 유사도, 영화2 - 영화1 유사도, 영화2 - 영화2 유사도, ... 영화2 - 영화n 유사도],
      [영화3 - 영화0 유사도, 영화3 - 영화1 유사도, 영화3 - 영화2 유사도, ... 영화3 - 영화n 유사도],
      [영화4 - 영화0 유사도, 영화4 - 영화1 유사도, 영화4 - 영화2 유사도, ... 영화4 - 영화n 유사도],
    ]

    cosine_sim => row는 특정 영화가 다른영화들과 어떤 유사도를 가지고 있는지 저장한다
    '''
    idx = indices[title] #  제목을 통해 몇번째 영화인지 가져온다.

    sim_scores = list(enumerate(cosine_sim[idx])) # 

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:recommend_size + 1]

    movie_indices = [i[0] for i in sim_scores]

    return data['title'].iloc[movie_indices]

data = df # .head(20000)

print('[전처리] NULL값 제거 ===========================')
print('null 처리 전: ', data['overview'].isnull().sum())
data['overview'] = null_to_zero_padding(data, 'overview')
print('null 처리 후: ', data['overview'].isnull().sum())
print('[전처리] NULL값 완료 ===========================\n')

print('[토큰 백터화] IF-IDF 시작 ===========================')
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(data['overview'])
print(tfidf_matrix)
print('shape: ',tfidf_matrix.shape) # shape: (20000, 47487) => (영화 갯수, 모든 영화에서 사용된 총 단어)
print('[토큰 백터화] IF-IDF 완료 ===========================\n')

print('[유사도 측정] 코사인 유사도 시작 ===========================')
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix) # shpae: (20000, 20000) => (영화, 영화) 각 영화와 간의 유사율, n 번째 영화는 (n,n)는 1이 나온다. 
print('shape: ', cosine_sim.shape)
print('[유사도 측정] 코사인 유사도 완료 ===========================\n')

print('[인덱싱] index => 영화이름, value => index(number)')
indices = pd.Series(data.index, index=data['title']).drop_duplicates()
print()

recommends = get_recommendations('The Dark Knight Rises', cosine_sim, 10)
print(recommends)