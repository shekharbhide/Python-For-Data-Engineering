# def remove_duplicate(str):
#     str = str.lower()

#     op = ''
#     for i in str:
#         if i not in op:
#             op += i

#     return op
    


# str = input()

# print(remove_duplicate(str))

def remove_duplicate(s):
    s = s.lower()  # Convert the string to lowercase
    seen = set()   # Create a set to keep track of seen characters
    op = []        # Use a list to store the result

    for char in s:
        if char not in seen:
            seen.add(char)  # Add the character to the set
            op.append(char) # Append the character to the result list

    return ''.join(op)  # Join the list into a string

s = input("Enter a string: ")
print(remove_duplicate(s))