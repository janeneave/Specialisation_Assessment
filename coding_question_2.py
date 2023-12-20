# Coding Question 2
def number_of_squares(n):
    if n == 1:
        return 1
    else:
        return number_of_squares(n - 1) + n * n


print(number_of_squares(2))  # 5
print(number_of_squares(3))  # 19
print(number_of_squares(4))  # 30

