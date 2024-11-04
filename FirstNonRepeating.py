# Function to count the character in the string
def charCount(string, char):
    count = 0
    for val in string:
        if (val == char):
            count += 1
    return count

string = str(input()).lower() # Getting the input string from the user and i consiter all the character as lowercase
ind = 0 # intializing the index to access the character
flag = 0
while (ind < len(string)):
    count = charCount(string, string[ind])
    if (count == 1): # This block will works when the count of the particular character is one and it will print that character and break the loop
        print(string[ind])
        flag = 1
        break
    ind += 1
    
# This block will work only if the string doesn't contain the non-repeating character
if (flag==0):
    print("There is no Non-Repeating character in the given string")
    
'''    
Sample Input -> 1
    input - "swiss"
    output - w
    
Sample Input -> 2
    input - "palinrome"
    ouput - p
    
Sample Input -> 3
    input - "aabbbccc"
    ouput - There is no Non-Repeating character in the given string
'''