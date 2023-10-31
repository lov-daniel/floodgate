# Floodgate
What is Floodgate
-

Floodgate is a small project that I created in order to practice my understanding of how ciphers work. Cryptology entered my life as a small interest and I wanted to apply it to my skills as a computer programmer. The program works by first taking in a message, this message can be encrypted or decrypted, and the program runs the message through a series of functions and returns a string value of the encrypted/decrypted message.

How does it work?
-   
Currently, the program is utilizing three different forms of encryption: a Caeser cipher[^1], a Vigenère cipher[^2], and another cipher that I
developed involving the use of mathematical functions, more on this later. 
<br><br/>
The program itself runs through a specific encryption with the reverse order applying to the decryption sequence. The Caeser cipher is first applied which causes a shift by one letter to the right. This shift causes the following changes to letters within the given message:

* a -> b, 
* b -> c,
* etc.

The second form of encryption that is used in this sequence is the Vigenère cipher. The user is asked to give a key word to scramble their message
with. This is very dynamic as it is entirely depended on what the user inputs. For example: 
* Given the message "hello world"
* Given the keyword sophia
* Results in encrypted message zsasw wgfak

[^1]: Caeser ciphers, also known as Caeser shift ciphers, are very basic, involving the movement of letter positions.
  [^2]: Vigenère ciphers are very similar in nature to the Caeser cipher, however, the primary difference is that it is a shift by a specific keyword. [Learn more here.](https://www.geeksforgeeks.org/vigenere-cipher/#)

