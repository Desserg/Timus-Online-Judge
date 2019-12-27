string = input()
#string = string.lower()

def longest_palindrome(text):
    longest = ""
    for i in range(len(text)):
        for j in range(0, i):
            chunk = text[j:i + 1]
            if chunk == chunk[::-1]:
                if len(chunk) > len(longest):
                    longest = chunk
    return longest

string2 = longest_palindrome(string)

if string2 == '':
    print(string[0])
#elif string == string2:
#    print(string[1:-1])    
else:    
    print(string2)
