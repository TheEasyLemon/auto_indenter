# auto_indenter
By Dawson Ren

## Inspiration
I want to get a better idea of the JS behind many websites. However, these websites have code that are not very readable.

This is a python script that can convert not very readable website code into more readable code through the addition in newlines and indents.

## Considerations
### Javascript
* After every semicolon, there should be a newline ("\n")
* After every left bracket ("{"), there should be a newline ("\n") and every following line should be indented by a level ("\t" or two spaces " ")
* Before every right bracket ("}"), there should be a new line ("\n") and every following line should be dedented by a level
* After every right bracket ("}"), there should be a newline ("\n")

After some more consideration, there are some more rules that need to be followed.
* If there is a semicolon within a for loop, we should not add a newline ("\n")
* If a right bracket is followed by a semicolon, right parenthesis, comma, or another right bracket, we should not add newline ("\n") in between them
* There should be a space before every left bracket.
* We also need to be able to tell if we're in a case block, and properly indent/dedent


I think that's it!