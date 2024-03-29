#Adapted from the pseudocode at:
# https://en.wikipedia.org/wiki/Shunting-yard_algorithm


# Notes to self
#in the shunting yard algorithm you need a stack for operators
# We need to set up the presedance order (see below)

def shunt(infix):
    """Convert infix expressions to postfix. """

    #the eventual output
    postfix =""
    #the shunting yard operator stack
    stack =""
    #operator presedance
    presedance = {'*':100, '.':90, '|':80}
    #loop trough the input character at the time
    for c in infix:

        #debbuging
        #print(f"c: {c}\t postfix: {postfix} \t stack: {stack}")
      
        #it first check if c is an operator without checking if is a letter
        if c in {'*','.', '|'}:
            while len(stack) > 0 and stack[-1] != '(' and presedance[stack[-1]] >= presedance[c]:
                #move operator at the top of stack to output
                postfix = postfix + stack[-1]
                #removes operator, replaces stack with the last one removed
                stack = stack[:-1]
            #push c to the stack
            stack = stack + c
        elif c== '(':
            #push c to the stack
            stack = stack + c
        elif c == ')':
            while stack [-1] != '(':
                postfix = postfix + stack[-1]
                stack = stack[:-1]
            #remove open bracket from stack
            stack = stack[:-1]      
        else:
        #push it to the output
            postfix += c

    while len(stack) !=0:
        postfix = postfix + stack[-1]
        stack = stack[:-1]
    return postfix
