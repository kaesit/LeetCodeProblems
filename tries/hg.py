class Solution:
     def removeDigit(self, number: str, digit: str) -> str:
          def drop_first_member(s, char_to_remove):
               index = s.find(char_to_remove)
               if index == -1 or index == 1:
                    return s
               else:
                    return s[:index] + s[index + 1:]
          #count = {}
          new_number = drop_first_member(number, digit)
          return new_number
   
   
print("Soluition: ", Solution().removeDigit("133235", "3"))


"""def printDups(Str):

    count = {}
    for i in range(len(Str)):
        if(Str[i] in count):
            count[Str[i]] += 1
        else:
            count[Str[i]] = 1
        #increase the count of characters by 1 
 
    for it,it2 in count.items():  #iterating through the unordered map 
        if (it2 > 1):   #if the count of characters is greater than 1 then duplicate found
            print(str(it) + ", count = "+str(it2))
    
# Driver code
Str = "test string"
printDups(Str)

string = "123"
a = string.index("3")
print(a)

"""

"""# Kullanım örneği
original_string = "Merhaba Dünya"
index_to_remove = 8
new_string = remove_char_at_index(original_string, index_to_remove)

print("Orijinal string:", original_string)
print("Yeni string:", new_string)
"""
"""def remove_first_occurrence(s, char_to_remove):
    index = s.find(char_to_remove)
    if index == -1:
        return s  # Karakter bulunamazsa, orijinal string döndürülür
    return s[:index] + s[index+1:]

# Kullanım örneği
original_string = "Merhaba Dünya, Dünya!"
char_to_remove = 'D'
new_string = remove_first_occurrence(original_string, char_to_remove)

print("Orijinal string:", original_string)
print("Yeni string:", new_string)

def remove_non_adjacent_char(s, char_to_remove):
    # Karakterin tüm konumlarını bul
    indices = [i for i, char in enumerate(s) if char == char_to_remove]
    
    if not indices:
        return s  # Karakter bulunamazsa, orijinal string döndürülür
    
    # Yan yana olmayan ilk örneği bul
    for i in range(len(indices) - 1):
        if indices[i + 1] != indices[i] + 1:
            first_non_adjacent_index = indices[i]
            break
    else:
        # Eğer yan yana olmayan karakter bulunamazsa
        return s

    # İlk yan yana olmayan karakteri sil
    return s[:first_non_adjacent_index] + s[first_non_adjacent_index + 1:]

# Kullanım örneği
original_string = "133235"
char_to_remove = '3'
new_string = remove_non_adjacent_char(original_string, char_to_remove)

print("Orijinal string:", original_string)
print("Yeni string:", new_string)"""