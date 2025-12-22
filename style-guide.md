Computer Programming for Lawyers – Style Guide
==============================================

*Last updated 1/09/18*

The following guide contains general rules for good coding style in Python.
This guide serves as the manual of style for Computer Programming for Lawyers.
These rules are not comprehensive, nor are they perfect. There are many situations
where you will need to use your best judgment. Above all else, always code with a
reader in mind and always aim to be consistent. A good rule of thumb is to
emulate the style of the textbook.

As incentive to maintain good style, note that style
will count for part of your grade on each problem set.

Headers
-------

Every program should begin with a comment providing the following information:
* Your name.
* The filename of the program.
* A brief description of what the program does and how it is used.
  If the program needs command-line arguments or accepts input
  in a specific format, clarify that information here.
* A list of dependencies – other programs or libraries this program
  needs to run properly. Dependencies will become important later in the semester.
  * You do not need to list standard Python functions and libraries that are
    built-in (the print function or the sys library).
  * You need to list any libraries that require pip installation (beautifulsoup or pypdf2).
  * You need to list any Python libraries that you create. In
    other words, you should list any external Python files that
	are necessary for this Python file to run.
  * In general, list any file or library that a user
    of your code would need to obtain or install above
	and beyond a basic Python installation.
* A list of any help you received or other sources you consulted
  in the process of composing this program. This is your opportunity
  to acknowledge any collaboration/assistance and cite your sources as necessary.
  
To distinguish the header from the rest of your code, each line of
the header should be preceded with three # characters followed by a
single space. An example header is below:

```
### Name: Larry Lawyer
### Filename: hello_stock_quote.py
### Description: Receives a person’s name and a stock ticker as
###     command-line arguments (in that order). Prints a greeting to the name
###     and the current value of the user-specified stock.
### Dependencies:
###     * beautifulsoup (for scraping the stock quote)
### Help:
###     * Discussed high-level approaches to the problem with John Doe.
###     * Talked to Prof. Ohm at office hours about how print() works.
###     * Consulted stackoverflow for web-scraping examples.
```

General Rules
-------------

* No line of code should be longer than 100 characters.
  If a line is longer than 100 characters, break it up into 
  shorter lines by saving subexpressions to variables.
* Whenever you find yourself repeating identical code or
  needing to copy and paste code, you should instead capture
  that behavior in a single function that you can call from multiple places.
* Each program you write should be structured in the order below:
  * Header
  * Any imports your program needs
  * Any constants your program needs
  * The main body of the program
  
Comments
--------

* Comment code thoroughly. Each comment marker (#)
  should be followed by a single space. Each comment should begin with
  a capital letter and end with a period.
* Include plenty of whitespace. Remember that, although Atom
  colors your code to make it easy to read, your graders will see
  your code printed on paper in black and white.
* Break your code into “paragraphs” of two to five lines of
  related statements. Each paragraph should begin with a short
  comment summarizing the paragraph’s behavior. Each paragraph
  should be followed with a single blank line.
  
Variables
---------

* Give variables descriptive names.
* The first letter of a variable should always be lowercase.
* If a variable name comprises multiple words
  ("time of day" or "number of hours"), the first letter of subsequent words should
  be lowercase and each word should be separated with an underscore
  (`time_of_day`, `number_of_hours`).
* If a variable is a constant (if the variable's value should
  always be the same for all time – pi, feet per mile, number of US senators),
  it should be named in all caps with underscores in between each word
  (`PI`, `FEET_PER_MILE`, `NUMBER_OF_SENATORS`).
* If you ever find yourself needing to use a specific number (a *magic number*) in your code
  (60 for the number of minutes in an hour or 3.14 for pi), you should
  save the value to a constant variable (`MINUTES_PER_HOUR`, `PI`) at the
  top of your program and use the variable elsewhere. Make sure to provide
  a comment explaining what the constant represents. We will deduct points if you
  use magic numbers without first saving them to constants.
  
Operators
---------

* Each mathematical or Boolean operator (+, -, *, /, ==, etc.) should be
  surrounded by one blank space on either side.
* When calling a function, should be no space between the name of the
  function and the opening parenthesis containing its arguments. The
  commas between arguments should be followed by a single space.
* When indexing a list or dictionary, there should be no space between
  the list or dictionary and the opening square bracket containing the index.
  
Functions
---------

* Before each function, write a comment that briefly describes what
  it expects for each argument (i.e., type and purpose), what it returns, and its behavior.
* Remember that functions hide away code so a user doesn't need
  to know how it works, so avoid including extraneous information about a function's inner workings.
* Only write the minimum information that a user needs to properly use the function.


