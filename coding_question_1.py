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


def number_of_unique_consonants(string):
    consonants = "bcdfghjklmnpqrstvwxyz"
    consonant_counts = {}
    for char in string.lower():
        if char in consonants:
            consonant_counts[char] = consonant_counts.get(char, 0) + 1
    return sum(1 for count in consonant_counts.values() if count == 1)

print(number_of_unique_consonants('cat'))
print(number_of_unique_consonants('cataract'))
print(number_of_unique_consonants('hello'))

