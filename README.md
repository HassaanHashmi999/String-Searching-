# String-Searching


## Brute Force (Naive Method)
Slide the pattern over text one by one and check for a match. If a match is found, then slide by 1
again to check for subsequent matches.
The Time Complexity: O(N 2 )
The number of comparisons in the worst case is O(M * (N – M + 1)). Although strings which
have repeated characters are not likely to appear in English text, they may well occur in other
applications (for example, in binary texts). The KMP matching algorithm improves the worst
case to O(N).


## KMP
Unlike Brute Force Algorithm, where we slide the pattern by one and compare all characters at
each shift, we use a value from lps[] to decide the next characters to be matched. The idea is to
not match a character that we know will anyway match.
How to use lps[] to decide next positions (or to know a number of characters to be skipped)?

We start comparison of pat[j] with j = 0 with characters of current window of text.
We keep matching characters txt[i] and pat[j] and keep incrementing i and j while pat[j]
and txt[i] keep matching.
When we see a mismatch
○ We know that characters pat[0..j-1] match with txt[i-j...i-1] j starts with 0 and
increment it only when there is a match.
○ We also know (from above definition) that lps[j-1] is count of characters of
pat[0...j-1] that are both proper prefix and suffix.


## RABIN KARP:
Like the Brute Force Algorithm, the Rabin-Karp algorithm also slides the pattern one by
one. But unlike the Brute Force, the Rabin Karp algorithm matches the hash value of the
pattern with the hash value of the current substring of text, and if the hash values match
then only it starts matching individual characters. So Rabin Karp algorithm needs to
calculate hash values for the following strings.
Pattern itself
All the substrings of the text of length n
Since we need to efficiently calculate hash values for all the substrings of
size m of text, we must have a hash function that has the following
property:
Hash at the next shift must be efficiently computable from the current hash
value and next character in text or we can say hash(txt[s+1 .. s+m]) must be●
efficiently computable from hash(txt[s .. s+m-1]) and txt[s+m] i.e.,
hash(txt[s+1 .. s+m]) = rehash(txt[s+m], hash(txt[s .. s+m-1])) and
Rehash must be O(1) operation.
The hash function suggested by Rabin and Karp calculates an integer value. The integer value
for a string is the numeric value of a string.


## I have used a library known as tkinter which helped us to build the GUI for the Algorithms
