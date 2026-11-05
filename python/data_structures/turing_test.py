# Finding the First Non-Repeating Character
#Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1
def non_repeating_character(test_str: str) -> int:

    freq_dict = {}

    for char in test_str:
        freq_dict[char] = freq_dict.get(char, 0) + 1

    for i , char in enumerate(test_str):
        if freq_dict[test_str[i]] == 1:
            return i

    return -1    


# Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

def valid_anagram(str_1: str, str_2: str) -> bool:
    
    dict_a = {}
    

    if len(str_1) != len(str_2):
        return False

    for char in str_1:
        dict_a[char] = dict_a.get(char, 0) + 1

    
    for zz in  str_2:
        if dict_a.get(zz, 0) > 0:
            dict_a[zz] -= 1
        else:
            return False
        
    return True             
    


if __name__ == "__main__":

    print("\n Non Repeating Character Index")
    print(non_repeating_character("leetcode"))
    print(non_repeating_character("loveleetcode"))
    print(non_repeating_character("aabbcc"))
    print(non_repeating_character("z"))
    print(non_repeating_character("aabbc"))


    print("\n Valid Anagram Test")
    print(valid_anagram("anagram", "nagaram"))
    print(valid_anagram("rat", "car"))
    print(valid_anagram("a", "ab"))
    print(valid_anagram("aacc", "ccac"))
    print(valid_anagram("a", "a"))