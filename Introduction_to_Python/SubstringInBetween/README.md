# Substrings in Between
Return the string of letters between the two characters passed in to the attributes of the function.

Define a function that is able to extract a portion of a string between two characters. The function will take three parameters where the first parameter is the string we are going to extract the substring from, the second input is the starting character of our substring and the third character is the ending character of our substring. Here are the steps we can use:

Define the function to accept three parameters, one string and two characters
find the starting index of our substring using the second input parameter
find the ending index of our substring using the third input parameter
If neither of the indices are -1, return the portion of the first input parameter string between the starting and ending indices (not including the starting and ending index)
If either of the indices are -1, that means the start or end of the substring didn’t exist in our string. Return the original string in this case.

Function should be named substring_between_letters that takes a string named word, a single character named start, and another character named end. This function should return the substring between the first occurrence of start and end in word. If start or end are not in word, the function should return word.

For example, substring_between_letters("apple", "p", "e") should return "pl".
