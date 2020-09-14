def isVowel(c): 
    if (c == 'a' or c == 'A' or c == 'e' or 
        c == 'E' or c == 'i' or c == 'I' or 
        c == 'o' or c == 'O' or c == 'u' or c == 'U'): 
        return True
    return False

def reverserVowel(string): 
    j = 0
    vowel = [0] * len(string) 
    string = list(string) 
  
    # Storing the vowels separately 
    for i in range(len(string)): 
        if isVowel(string[i]): 
            vowel[j] = string[i] 
            j += 1
  
    # Placing the vowels in the reverse 
    # order in the string 
    for i in range(len(string)): 
        if isVowel(string[i]): 
            j -= 1
            string[i] = vowel[j] 
  
    return ''.join(string) 
  
if __name__ == "__main__": 
    string = input()
    print(reverserVowel(string)) 
