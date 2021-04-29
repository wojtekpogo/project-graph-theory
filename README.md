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


#### How to use

Navigate to the directory with the project and execute following command

```python3 reg.py --h``` 

It will then show you help menu in the console

![1](https://user-images.githubusercontent.com/55446533/116600433-36014580-a921-11eb-863b-4b3753d1e95a.PNG)


#### Example

```python3 reg.py --regex "a.b|b*" --file "/home/wojtekpogo/repo/project-graph-theory/myfile.txt"```

![2](https://user-images.githubusercontent.com/55446533/116600691-7bbe0e00-a921-11eb-96ed-a805c14b1180.PNG)

*--regex* specifies the regex you wish to use

*--file* specify the path to the text file

**Disclaimer**

Depending on your Python version you may use ```python reg.py ``` instead of ```python3 reg.py```

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

### Conversion

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

Most important thing to understand about this algorithm is the set of 5 rules.[<sup>6</sup>]

#### Rule 1 An Empty Expression
An empty expression, for example ‘ ’ or ε, will be converted to:

![rule1](https://user-images.githubusercontent.com/55446533/116317191-ebf65380-a7aa-11eb-8d15-0915fc1e79b5.png)

#### Rule 2: A symbol
A symbol is converted to:

![rule2](https://user-images.githubusercontent.com/55446533/116317471-47284600-a7ab-11eb-972b-b14a79629558.png)

#### Rule 3: Union expression
A union expression a+b is converted to:

![rule3](https://user-images.githubusercontent.com/55446533/116317605-78a11180-a7ab-11eb-80e8-d141453fc34d.png)

#### Rule 4: Concatenation expression
A concatenation expression ab or a?b is converted to:

![rule4](https://user-images.githubusercontent.com/55446533/116317763-af772780-a7ab-11eb-852b-05e9dead9e06.png)

![rule4a](https://user-images.githubusercontent.com/55446533/116317769-b1d98180-a7ab-11eb-8224-572cd20ca2b1.png)

#### Rule 5: Kleene star expression
The [Kleene star](https://en.wikipedia.org/wiki/Kleene_star) expression is converted to:

![rule5](https://user-images.githubusercontent.com/55446533/116318039-1268be80-a7ac-11eb-9aa5-f78dd69269a8.png)

---

# What is a Regular Expression?

A regular expression also known as '**regex**' is a search pattern used for matching one or more characters within a string. It can match specific characters, [wildcards](https://en.wikipedia.org/wiki/Wildcard_character#:~:text=In%20regular%20expressions%2C%20the%20period,which%20matches%20any%20single%20character.&text=*%20it%20will%20match%20any%20number,known%20as%20the%20Kleene%20star.), and ranges of characters. 
> “A regular expression is a pattern which specifies a set of strings of characters; it is said to match certain strings.” —**Ken Thompson** [<sup>1</sup>] [<sup>2</sup>]

They can be used to search, edit, or manipulate text and data.[<sup>7</sup>]

Some of the uses of Regular Expressions:
* Find a list of phone numbers in a large text file
* Check that a user-provided email address is valid
* Verify that a password meets custom strength requirements
* Locate all outgoing links in an HTML document

Basic expression ```abcde```  will only match ```abcde```, but if we'll add the [quantifier](https://en.wikipedia.org/wiki/Generalized_quantifier) to it, then our expression will look like: ```a+bcde```, now it can match ```abcde```,```aabcde``` or ```aaaaaaabcde```. In other words, it will match any number of character ```a``` at the beggining of the expression (but at least one) and then the rest of the expression which is ```bcde```.

#### Quantification



| Quantifier       | Meaning        | Example | What it will match |
| ------------- |:-------------:| :-----:|:------:|
| [Kleene Star](https://en.wikipedia.org/wiki/Kleene_star#:~:text=In%20mathematical%20logic%20and%20computer,as%20the%20free%20monoid%20construction.) (✱) | 0 or more occurrences | a✱b  | ab, b, aab, aaaaaab, aaab...and more |
| +      |  1 or more occurrences     |   a+b | ab, aab, aaaaaaab, aab..and more |
| ? | 0 or 1 occurrences   |  a?b |  ab, b  |  
| {n,m} | at least *n* and maximum *m* occurrences | a{1,4}b | ab, aab, aaab, aaaab |
| {n,} | at least *n* occurrences |  a{3,}b | aaab, aaaab aaaaab..and more |
| {,n} | maximum *n* occurrences |  a{,3}b |  b, ab, aab, aaab |
| {n} | *n* occurrences specificly | a{3}b |  aaab |




# How do regular expressions differ across implementations?

answer here

# Can all formal languages be encoded as regular expressions?

According to [Wikipedia](https://en.wikipedia.org/wiki/Formal_language), formal language consists of words whose letters are taken from an alphabet and are well-formed according to a specific set of rules. Regular expressions and nondeterministic finite automata are two representations of formal languages.

Formal Languages can be also:

*

# Refereneces

<sup>1</sup>[What is Regular expression](https://bit.ly/3v3RTp2)

<sup>2</sup>[Ken's Thompson quote](https://www.oreilly.com/library/view/introducing-regular-expressions/9781449338879/ch01.html)

[formal languages](https://dzone.com/articles/back-basics-regular)

<sup>3</sup>[Infix and Postfix Definition](https://studyalgorithms.com/theory/what-are-infix-postfix-and-prefix-expressions/#:~:text=An%20infix%20expression%20is%20a,)

<sup>4</sup>[Shutning Yard Algorithm](https://www.javatpoint.com/shunting-yard-algorithm-in-java)

<sup>5</sup>[Thompson's Construction definition](https://en.wikipedia.org/wiki/Thompson%27s_construction)

<sup>6</sup> [Thompson's construction rules](https://medium.com/swlh/visualizing-thompsons-construction-algorithm-for-nfas-step-by-step-f92ef378581b)

<sup>7</sup>[Regex definition](https://docs.oracle.com/javase/tutorial/essential/regex/)

  



