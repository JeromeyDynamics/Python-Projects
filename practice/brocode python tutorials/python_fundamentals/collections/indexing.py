# indexing = accessing elements of a sequence using [] (indexing operator)
#                     [start : end : step]

# EXERCISE 0
credit_number = "1234-5678-9012-3456"

print(credit_number[0])
print(credit_number[0:4])
print(credit_number[:4])
print(credit_number[4:8])
print(credit_number[4:])
print(credit_number[-1])
print(credit_number[-4:])
print(credit_number[::2])
print(credit_number[::3])

print("--------------------------------------")

# EXERCISE 1
credit_number = "1234-5678-9012-3456"
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

print("--------------------------------------")

# EXERCISE 2
credit_number = "1234-5678-9012-3456"
credit_number = credit_number[::-1]
print(credit_number)