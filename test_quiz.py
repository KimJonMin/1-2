from quiz import Quiz

q = Quiz('파이썬을 만든 사람은?', ['고슬링', '귀도', '림누스', '빌게이츠'], 2)
q.display()
print('정답(2):', q.check_answer(2))
print('오답(1):', q.check_answer(1))
