def solution(s):
    answer = False
    if(s.isdigit() and (len(s)==4 or len(s)==6)):
        answer=True
    '''
    isalpha > 문자인지  isdigit()숫자인지
    return s.isdigit() and len(s) in (4, 6)> len(s) 가(in) (4,6)에 있으면 True
    
        try:
            int(s)    int(s)해서 에러일시 return false
        except:       
            return False
    return len(s) == 4 or len(s) == 6 
    '''
    return answer

s="11234"
print(solution(s))

'''
정확도100%

문제 설명
문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 예를 들어 s가 a234이면 False를 리턴하고 1234라면 True를 리턴하면 됩니다.

제한 사항
s는 길이 1 이상, 길이 8 이하인 문자열입니다.
입출력 예
s   	return
a234	false
1234	true
'''