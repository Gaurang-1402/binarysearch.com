# approach

# inorder()
# we will split the numbers into operands and operators, doing this by checking if it is not in '+-*/' it is a digit else it can be a '-' of the number's value

# postorder()
# we will simply take the infix and return a postfix

# for each token
# -> if it is a operand i insert it in int() to the result
# ->else if it is a greater precedence operator ( here '*/' > '+-' or empty ) then add it to the stack
# -> else just keep popping from the stack and adding to the result for the greater/equal precedence operators since they MUST take place before you! ;)

# finally the last part of the operators is left in the stack, just pop and add to the result ( while len(ops) )

# postorder_eval()
# this may be the easiest function

# for each token
# -> if it is a operand push it to the stack
# -> if it is a operator, pop the previous two operands from the stack ( a, b ) , evaluate them and push them back inside (c);)

# analysis

# Time Complexity
# T = O(n) since each function works in a single pass! so total time = 3 * n

# Space Complexity
# S = O(n) the size of s, infix, postfix is n but 3 * n is still O(n) so this is also only O(n) which is acceptable :D


# convert the input from string to operands and operators
# in a list operand = numbers having multiple digits and neg!
def inorder(s):
    infix = []
    operand = ""
    prev_operator = "+"
    for c in s:
        if c not in "+-*/":
            operand += c
        elif prev_operator in "+-*/" and c == "-":
            # negative number found!
            operand += c
        else:
            infix.append(operand)
            infix.append(c)
            operand = ""
        prev_operator = c
    infix.append(operand)
    return infix


# convert infix to postfix expression using a stack
def postorder(s):
    # ops stack is storing the operators
    ops = []
    res = []

    for c in s:
        if c not in "+-/*":
            res.append(int(c))
        elif c in "/*" and len(ops) and ops[-1] in "+-" or len(ops) == 0:
            ops.append(c)
        else:
            # while precedence of operator is greater than or equal
            while len(ops) and (ops[-1] in "*/" or c in "+-"):
                res.append(ops.pop())
            ops.append(c)

    while len(ops):
        res.append(ops.pop())

    return res


# postfix is easy to evaluate for CPU and easy to code for us!
def postorder_eval(postfix):
    res = []

    for c in postfix:
        if isinstance(c, str):
            b = int(res.pop())
            a = int(res.pop())
            if c == "+":
                c = a + b
            elif c == "-":
                c = a - b
            elif c == "*":
                c = a * b
            elif c == "/":
                c = a // b
            res.append(c)
        else:
            res.append(c)

    return res[-1]


class Solution:
    def solve(self, s):

        infix = inorder(s)
        print(infix)

        postfix = postorder(infix)
        print(postfix)

        return postorder_eval(postfix)



        
