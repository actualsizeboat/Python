

def solution(problem):
    atbash_func = ord('z') + ord('a')
    if (problem[0] == problem[-1]) and problem.startswith(("'", '"')):
        return problem[1:-1]
    tochange = 'abcdefghijklmnopqrstuvwxyz'
    deciphered = ''
    for i in problem:
        if i in tochange:
            deciphered += chr(atbash_func - ord(i))
        if i not in tochange:
            deciphered += i
    print(deciphered)

solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")