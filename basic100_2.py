```
1014 : [기초-입출력] 문자 2개 입력받아 순서 바꿔 출력하기

2개의 문자(ASCII CODE)를 입력받아서 순서를 바꿔 출력해보자.

입력
2개의 문자가 공백으로 구분되어 입력된다.

출력
두 문자의 순서를 바꿔 출력한다.

입력 예시   
A b

출력 예시
b A
```

a,b = input().split(" ")
print(b, a)