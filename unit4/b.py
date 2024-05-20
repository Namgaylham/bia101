#problem
#given an input string with just open and close brackets
#calculate the final floor that the alien will reach at

input_str = "((())())()(((((()()(()())())(()((((((((()))()(())(()())((()))())(((()())))()))(((()))()())()((()(())))((())())())()))))(((())()))()(()((()))(())()())))()()())(()(())))()))((())())()(((()()()()(()(()(((())((((()))))))(())((()(()())())()(())))()()(((((()))))(()))()))(())())))((()))((())))()))()))()(()(()))(()()())(()((((()())((()((()(()))))(()))())((())(((()()()))((((((()()()(()(())(()()()))()()()((((((())()))())()())()))()(())()())(()())()((()))()))))((((())))))())(())((((())))())((())()))(()))())))((())))()))))))((())(())))((())))(())))(())()(()()))(((())()((()()(((()))((()(()))()))))))()))))(()()(((()()((((((())()))()(((((((())())))()()((()))())())(((()(())()((((((())))))))()))))(())((((()((()()(()(())))()((((((())(()))(()))))((()(((()))()))))))(((((())()))(((((((()(()()((()))(())((()())((((()(((()))((()(()))))())())))())())(()))))(())(((())))())))((()(()(((((())))()())()()(((()()))()(()(((((())(())(())))(()())()(()))()((()())))()))())())(()(())()))())(())))(((((()())))()(()))(()()(()(()"

floor_index = 0 #? variable to keep track of the ans
for i in input_str: #! go through each character 
    if i == "(": #? if ( add one to the answer
        floor_index = floor_index + 1
    if i == ")": #? if ) sub one to the answer
        floor_index = floor_index - 1
# print the final answer
print('the final floor is', floor_index)

#problem 2
# scenario the alien only understand you
#if the input is valid
#given a set of open and close bracket
#check to see if the input is valid
#example 1
#((()))
#output: True
#(()
# output: False




input_str ==- ")))"
stack = []
for char in input_str:
    if char == "(":
        stack.append(char)
    if char == ")":
        stack.pop()
length = len(stack)
if length == 0:
    print('True')
else:
    print("False")