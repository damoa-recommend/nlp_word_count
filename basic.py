sentences = [
  "나는 오늘도 받을 먹습니다.",
  "나는 오늘도 출근을 합니다.",
  "오늘은 날씨가 좋네요"
]

word_map = {}
space = ' '

for sentence in sentences:
  print(sentence)
  words = sentence.split(space)

  for word in words:
    word_map.setdefault(word, 0)
    word_map[word] += 1

print('word map: ', word_map)