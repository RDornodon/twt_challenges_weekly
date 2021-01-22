_={};T=[_.update({65+c:90-c,97+c:122-c})for c in range(0,26)];solution=lambda s:s.translate(_)

print(solution("Hello World"))
print(solution('Zyxw'))
