# [].sorted -> it's built in!!! and it's a function!! é uma função

linguagens = ["Python", "VB", "PHP"]
print(sorted(linguagens, key=lambda x: len(x)))
print(sorted(linguagens, key=lambda x: len(x), reverse=True))
