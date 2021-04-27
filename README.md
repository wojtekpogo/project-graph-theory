# Graph Theory Project 2021
**Name:** Wojciech Pogorzelski 

**Student ID:** G00375250

**Module:** Graph Theory
___

# Project Description
description here


---

# Instructions
**Requirements:**
* Python 3
* Git

### How to get repository
Once you have created a directory, simply copy the link from the github repo, then opend command line inside selected directory and enter

```git clone https://github.com/wojtekpogo/project-graph-theory.git```

---
# Algorithms Description

### Shunting Yard Algorithm
Invented by [Edsger Dijkstra](https://en.wikipedia.org/wiki/Edsger_W._Dijkstra) and named the **'shunting yard'** algorithm because its operation resembles that of a railroad shunting yard. There purpose of this algorithm is to convert **infix expression** into **postfix expressions**. It is a [stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))-based algorithm. This algorithm was later generalized to operator-precedence parsing. The input of this algorithm is divided into two parts: the output queue and the operator stack. [<sup>4</sup>]

**Infix Expression** is a single letter, or an operator, proceeded by one infix string and followed by another infix string.

**Postfix Expression** also known as Reverse Polish Notation ([RPN](https://en.wikipedia.org/wiki/Reverse_Polish_notation)) is a single letter or an operator, preceded by two postfix strings. Every postfix string longer than a single variable contains first and second operands followed by an operator.[<sup>3</sup>]

To create Shuting Yard Algorithm we will need:
* Stack for operators
* Queue for output
* Array or List of tokens

Let's consider an input: **4 + 2 / (9 - 8) ^ 4 ^ 2** 

| Symbols       | Action        | Stack | Output |
| ------------- |:-------------:| :-----:|:------:|
| 4             | '4' is added to output |  | 4 |
| +      | pushed to the operator stack     |   + | 4 |
| 2 | '2' is added to output      |    + | 4 2  |  
| / | pushed to the operator stack | +/ | 4 2 |
| ( | pushed to the operator stack | +/( | 4 2 |
| 9 | '9' is added to output | +/( | 4 2 9 |
| - | pushed to the operator stack | +/(- | 4 2 9 |
| 8 | '8' is added to output | +/(- | 4 2 9 8 |
| ) | Pop stack to output | +/ | 4 2 9 8 - |
| ^ | pushed to the operator stack | +/^ | 4 2 9 8 -|
| 4 | '4' is added to output | +/^ | 4 2 9 8 - 4 |
| ^ | pushed to the operator stack | +/^^ | 4 2 9 8 - 4 |
| 2 | '2' is added to output | +/^^| 4 2 9 8 - 4 2 |
|   | Pop the whole stack |  | 4 2 9 8 - 4 2 ^ ^ / + |

**Output:** 4 2 9 8 - 4 2 ^ ^ / +

---

### Thompson's Constructions

Invented by [Ken Thompson](https://en.wikipedia.org/wiki/Ken_Thompson). To put this in simple terms, this algorithm transforms regular expression into nondeterministic finite automaton ([NFA](https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton)) [<sup>5</sup>]

Most important thing to understand about this algorithm is the set of 5 rules.

#### Rule #1 An Empty Expression
An empty expression, for example ‘ ’ or ε, will be converted to:

!(https://miro.medium.com/max/688/0*rRnvHFHEl6Z57Q6x)





---

# What is a Regular Expression?

A regular expression also known as '**regex**' is a search pattern used for matching one or more characters within a string. It can match specific characters, [wildcards](https://en.wikipedia.org/wiki/Wildcard_character#:~:text=In%20regular%20expressions%2C%20the%20period,which%20matches%20any%20single%20character.&text=*%20it%20will%20match%20any%20number,known%20as%20the%20Kleene%20star.), and ranges of characters. 
> “A regular expression is a pattern which specifies a set of strings of characters; it is said to match certain strings.” —**Ken Thompson** [<sup>1</sup>] [<sup>2</sup>]

# How do regular expressions differ across implementations?

answer here

# Can all formal languages be encoded as regular expressions?

According to [Wikipedia](https://en.wikipedia.org/wiki/Formal_language), formal language consists of words whose letters are taken from an alphabet and are well-formed according to a specific set of rules. Regular expressions and nondeterministic finite automata are two representations of formal languages.

# Refereneces

<sup>1</sup>[What is Regular expression](https://bit.ly/3v3RTp2)

<sup>2</sup>[Ken's Thompson quote](https://www.oreilly.com/library/view/introducing-regular-expressions/9781449338879/ch01.html)

[formal languages](https://dzone.com/articles/back-basics-regular)

<sup>3</sup>[Infix and Postfix Definition](https://studyalgorithms.com/theory/what-are-infix-postfix-and-prefix-expressions/#:~:text=An%20infix%20expression%20is%20a,)

<sup>4</sup>[Shutning Yard Algorithm](https://www.javatpoint.com/shunting-yard-algorithm-in-java)

<sup>5</sup>[Thompson's Construction definition](https://en.wikipedia.org/wiki/Thompson%27s_construction)

  



