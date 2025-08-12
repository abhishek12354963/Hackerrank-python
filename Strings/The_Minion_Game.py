'''Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string,S .
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string S.

For Example:
String S = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

For better understanding, see the image below:

banana.png

Your task is to determine the winner of the game and their score.

Function Description

Complete the minion_game in the editor below.

minion_game has the following parameters:

string string: the string to analyze
Prints

string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
Input Format

A single line of input containing the string S.
Note: The string S will contain only uppercase letters:[A-Z] .

Constraints



Sample Input

BANANA
Sample Output

Stuart 12
Note :
Vowels are only defined as AEIOU. In this problem, Y is not considered a vowel.'''

#code

def minion_game(string):
    # your code goes here
    vowels="AEIOU"
    kevin_scores = 0
    stuart_score = 0    
    length=len(string)
    for i in range(length):
        if string[i] in vowels:
            kevin_scores+=length-i
        else:   
            stuart_score += length-i
    if stuart_score > kevin_scores:
        print(f"Stuart {stuart_score}")
    elif kevin_scores > stuart_score:
        print(f"Kevin {kevin_scores}")
    else:
        print("Draw")

