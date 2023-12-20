# 1 A)
def number_of_unique_consonants(string):
    consonants = "bcdfghjklmnpqrstvwxyz"
    occurred_once = []
    occurred_more_than_once = []

    for char in string.lower():
        if char in consonants:
            if char in occurred_once:
                occurred_once.remove(char)
                occurred_more_than_once.append(char)
            elif char not in occurred_more_than_once:
                occurred_once.append(char)

    return len(occurred_once)


print(number_of_unique_consonants('cat'))
print(number_of_unique_consonants('cataract'))
print(number_of_unique_consonants('hello'))

# B)
# Time Complexity:
# My function above iterates through each character in the input string, then checks and updates the
# for each character depending on whether or not it is already in the occurs once or occurs more than once lists.
# Both of these are O(n) worst case, where n is the number of characters in the string and n is the size
# of the lists being searched.
# Removing and appending to another list also has O(n) of time complexity for the worst case whereby you might
# have to shift n characters.
# Altogether, because of the repeating search and also modifications to the lists
# i think this means that the time complexity of this function in the worst case is O(n^2).

# Space Complexity:# The space complexity of my function in the worst case is O(n) where n is the length of the input string.
# This is becuase the 2 lists could hold n number of consonants in the string. And becuase the
# string of consonant which are used to compared against is not modifed/does not change in size or get larger,
# I'd assume it is unlikely to impact the space complexity.