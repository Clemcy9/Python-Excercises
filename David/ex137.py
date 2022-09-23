"""
In the game of Scrabble™, each letter has points associated with it. The total score
of a word is the sum of the scores of its letters. More common letters are worth fewer
points while less common letters are worth more points. The points associated with
each letter are shown below:
One point A, E, I, L, N, O, R, S, T and U
Two points D and G
Three points B, C, M and P
Four points F, H, V, W and Y
Five points K
Eight points J and X
Ten points Q and Z
Write a program that computes and displays the Scrabble™ score for a word.
Create a dictionary that maps from letters to point values. Then use the dictionary to
compute the score.
"""


Pa={1:["A","E","I","L","N","O","R","S","T","U"], 2:["D","G"], 3:["B","C","M","P"],4:["F","H","V","W","Y"],5:["K"],8:["J","X"],10:["Q","Z"]}
def scrabble_Calculator(user_input):
	sumnum=0
	for x in user_input.upper():
		if x in Pa[1]:
			sumnum+=1
		elif x in Pa[2]:
			sumnum+=2
		elif x in Pa[3]:
			sumnum+=3
		elif x in Pa[4]:
			sumnum+=4
		elif x in Pa[5]:
			sumnum+=5
		elif x in Pa[8]:
			sumnum+=8
		elif x in Pa[10]:
			sumnum+=10
	print("Your score is ",sumnum)
while True:
	scrabble_Calculator(input("Input word: "))