#Lets check anagrams.

"""
Anagram is a word, phrase or name formed by rearranging the 
letters of another word. Like spar from rasp

"""
def anagram(st1:str, st2:str) ->bool:
    st_len = len(st1)
    tru = []
    for f in st1:
        if f in st2:
            tru.append(True)
        else:
            tru.append(False)

    if all(tru):
        return True
    else:
        return False

while True:
    st1 = input("Enter the first string: ")
    st2 = input("Enter the second string: ")

    if len(st1) != len(st2): 
        print("Please enter words of same length")

    else:
        break

if anagram(st1, st2):
    print(f"{st1} and {st2} are Anagrams")
else:
    print(f"{st1} and {st2} are not Anagrams")