# Thompson's construction
# G00375250
# 20/04/21 (a bit late, but beter late than never)
# Updated on 27/04/21
# Added match and follow E Arrows function

# Every state is a single symbol arrow or 1 or 2 empty arrows
"""A state and its arrows in Thompson's construction."""
class State():

    # Constructor
    def __init__(self,label,arrows,accept):
        self.label = label
        self.arrows = arrows
        self.accept = accept #true or false if its accept state


    # Whenever we're in the state, this function gives us the set containing this state and  also all of the states we can get to upon following the 'e' arrows
    def followEarrows(self):
        """The set of states that are gotten from following state"""

        # Include this state in the returned set
        states = {self}

        # If the state has 'e' arrows or let's say the label is None
        if self.label is None:
            # Loop through this state's arrows
            for state in self.arrows:
                # Incorporate that state's 'e' arrows occurs in states
                states=(states | state.followEarrows())

        # Return the set of states
        return states


# Class represents whole NFA
class NFA:
    """A non-deterministic finite automation."""

    def __init__(self,start,end):
        self.start = start
        self.end = end

    #match function
    def match(self, s):
        """Return True if and only if 's' is accepted by this NFA"""

        

        return True

# Method that runs throuh postfix notation and turns it to NFA
def re_to_nfa(postfix):

    stack = [] #list of nfas
    #loop through postfix re left to right
    for c in postfix: #loop through each character at the time
        # concatenation
        if c == '.':
            # pop nfa2 off the stack
            nfa2 = stack[-1]
            stack = stack[:-1]
            # pop the next nfa1 off the stack
            nfa1 = stack[-1]
            stack = stack[:-1]
            # make accept state of nfa1 non-accept
            nfa1.end.accept = False
            # make it point at start state of nfa2
            nfa1.end.arrows.append(nfa2.start)
            # make a new nfa with nfa1's start state and nfa2's end state
            nfa = NFA(start=nfa1.start,end=nfa2.end)
            # push to the stack
            stack.append(nfa)

        elif c == '|':
        
            # pop nfa2 off the stack first 
            nfa2 = stack[-1]
            stack = stack[:-1]
            # pop the next nfa1 off the stack
            nfa1 = stack[-1]
            stack = stack[:-1]

            # create new start and end state
            start = State(None, [], False) #constructor without naming the parameters
            end = State(None, [],  True)

            #make a new start state point at old start states
            start.arrows.append(nfa1.start)
            start.arrows.append(nfa2.start)
            # make old accept states tonon-accept
            nfa1.end.accept = False
            nfa2.end.accept = False

            #point old end states to new ones
            nfa1.end.arrows.append(end)
            nfa2.end.arrows.append(end)
           
            # make a new nfa with nfa1's start state and nfa2's end state
            nfa = NFA(start,end)
            # push to the stack
            stack.append(nfa)

        # Kleene's star
        elif c == '*':

            # pop nfa2 off the stack first 
            nfa1 = stack[-1]
            stack = stack[:-1]
           
            # create new start and end state
            start = State(None, [], False) #constructor without naming the parameters
            end = State(None, [],  True)

            #make a new start state point at old start state
            start.arrows.append(nfa1.start)
            # and at the new end state
            start.arrows.append(end)
            # make old accept state of  non-accept
            nfa1.end.accept = False
            #make old accept state point to new accept state
            nfa1.end.arrows.append(end)
            #make old accept state point to old accept state
            nfa1.end.arrows.append(nfa1.start)

            # make a new nfa
            nfa = NFA(start,end)
            # push to the stack
            stack.append(nfa)

        else:
            #create an nfa for the non-special character c
            #create the end state
            end = State(None,[],True)
            #create the start state
            start = State(c, [],False)
            # point new start state at new end state
            start.arrows.append(end)

            #create the nfa with start and end state
            nfa = NFA(start, end)
            #append the nfa to the nfa stack
            stack.append(nfa)

    #error checking
    if len(stack) != 1:
        return None
    else:
        return stack[0] #there should be just 1 nfa on the stack at the end


#unit tests
if __name__ == "__main__":
    for postfix in ["abb.*.a.","100.*.1.", "ab|"]:
        print(f"postfix:    {postfix}")
        print(f"nfa:      {re_to_nfa(postfix)}")
        print()