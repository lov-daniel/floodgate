# Floodgate
What is Floodgate
-

Floodgate is a small project that I created in order to practice my understanding of how ciphers work. Cryptology entered my life as a small interest and I wanted to apply it to my skills as a computer programmer. The program works by first taking in a message, this message can be encrypted or decrypted, and the program runs the message through a series of functions and returns a string value of the encrypted/decrypted message.

How does it work?
-   
Currently, the program is utilizing three different forms of encryption: a Caeser cipher[^1], a Vigenère cipher[^2], and another cipher that I
developed involving the use of mathematical functions, more on this later. The program itself runs through a specific encryption with the reverse order applying to the decryption sequence.
### Caeser Cipher 
 The first form of encryption that is being used is the Caeser cipher is first applied which causes a shift by one letter to the right. This shift causes the following changes to letters within the given message:

* Given the message "hello world"
* Results in encrypted message "ifmmp xpsme"

This is pretty cool, however, it's quite easy to crack usually by recognizing patterns such as the double m, as not many letters are used in doubles and once the two letters have been solved for, the entire thing is cracked.

### Vigenère Cipher
The second form of encryption that is used in this sequence is the Vigenère cipher. The user is asked to give a key word to scramble their message
with. This is very dynamic and much more difficult to simply 'guess' as it is entirely depended on what the user inputs as their key word. For example:

* Given the message "hello world"
* Given the keyword "sophia"
* Results in encrypted message "zsasw wgfak"

### Tsunami Cipher

The third form of encryption is what I named the Tsunami cipher. I felt it was very fitting considering the world started from water. It involves converting the letter into an ASCII code and dividing by the meaning of life: fourty-two[^3]. The result is then returned to the user as an array of 'obscure numbers.' For example:

* Given the message "hello world"
* 
* 



When we combine these three encryption methods sequentially, the following result will occur.

* First, the Caeser cipher will encode the message by shifting the phrase "hello world" into "ifmmp xpsme."
* Second, we will use the keyword we are given "sophia" and run the Vigenère cipher, resulting in the phrase, "atbtx xhgbl."
* Third, we will utilize the mathematical transformation of the letters by converting each letter into an ASCII code and 

### Foot Notes
[^1]: Caeser ciphers, also known as Caeser shift ciphers, are very basic, involving the movement of letter positions.
  [^2]: Vigenère ciphers are very similar in nature to the Caeser cipher, however, the primary difference is that it is a shift by a specific keyword. [Learn more here.](https://www.geeksforgeeks.org/vigenere-cipher/#)
[^3]: The meaning of life being fourty-two was coined by Douglas Adams in his book, "Hitchhiker's Guide to the Galaxy." In programming, typically fourty-two in ASCII refers to the asterisk, which is used to represent everything. Neat huh!
