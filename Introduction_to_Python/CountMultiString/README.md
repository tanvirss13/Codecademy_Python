# Count Multi String
Count the appearance of a string of letters in a word

Define a function to compare against an entire string instead of a single character. This function should accept a string and a substring to compare against. The number of occurrences of the second parameter within the first parameter string are returned. What this means is that we are checking the number of occurrences of the shorter string (second parameter) within the longer string (first parameter). One way to accomplish this is using the split function. Here is how to do that:

Define the function to accept two parameters. word for the input string and x for the second string we are searching for
Split the string into substrings based on the second input parameter
Count the number of instances the substring appeared in the first input string based on the split string
Return the result

Write a function named count_multi_char_x that takes a string named word and a string named x. This function should do the same thing as the count_char_x
function you just wrote - it should return the number of times x appears in word. However, this time, make sure your function works when x is multiple
characters long.

