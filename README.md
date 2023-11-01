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
* Results in the encrypted message: "ifmmp xpsme"

This is pretty cool, however, it's quite easy to crack usually by recognizing patterns such as the double m, as not many letters are used in doubles and once the two letters have been solved for, the entire thing is cracked.

### Vigenère Cipher
The second form of encryption that is used in this sequence is the Vigenère cipher. The user is asked to give a key word to scramble their message
with. This is very dynamic and much more difficult to simply 'guess' as it is entirely depended on what the user inputs as their key word. For example:

* Given the message "hello world"
* Given the keyword "sophia"
* Results in the encrypted message: "zsasw wgfak"

### Tsunami Cipher

The third form of encryption is what I named the Tsunami cipher. I felt it was very fitting considering the world started from water. It involves converting the letter into an ASCII code and dividing by the meaning of life: fourty-two[^3]. The result is then returned to the user as an array of 'obscure numbers.' For example:

* Given the message "hello world"
* Results in the encrypted messsage: "2.48, 2.40, 2.57, 2.57, 2.64, 2.83, 2.64, 2.71, 2.57, 2.83"

Now, this is really started to look like an encrypted message, but it only gets better because by layering these mentioned forms of encryption, we are able to get a fascinating result. Each form of encryption, on its own, has its own level of security, however, by essentially 'stacking' them together, we can get something that is incomprehensible to the normal person.

When we combine these three encryption methods sequentially, the following result will occur.

* First, the Caeser cipher will encode the message by shifting the phrase "hello world" into "ifmmp*xpsme."
* Second, we will use the keyword we are given "sophia" and run the Vigenère cipher, resulting in the phrase, "atbtx*xhgbl."
* Third, we will utilize the mathematical transformation of the letters using the **famous** Tsunami cipher that I developed.
* The final message looks as following: 2.31 2.76 2.33 2.76 2.86 1.0 2.86 2.48 2.45 2.33 2.57

Here are a few example encoded texts that you can try using this [online ide](https://www.online-python.com/yPdrGgU12k).

* 2.81 2.381 2.405 2.762 2.714 2.667 1.0 2.571 2.476 1.0 2.476 2.31 1.0 2.571 2.381 2.714 2.31 (keyword : coolio)
* 2.786 1.0 2.595 2.571 2.405 2.762 1.0 2.857 2.571 2.738 2.762 (keyword : lactose)
* 2.571 2.667 2.881 1.0 2.619 2.738 2.5 1.0 2.905 2.905 1.0 2.524 2.619 2.833 2.738 2.405 2.524 2.857 2.714 1.0 2.69 2.5 2.405 2.762 2.738 2.31 (keyword : mad)
### Foot Notes
[^1]: Caeser ciphers, also known as Caeser shift ciphers, are very basic, involving the movement of letter positions.
  [^2]: Vigenère ciphers are very similar in nature to the Caeser cipher, however, the primary difference is that it is a shift by a specific keyword. [Learn more here.](https://www.geeksforgeeks.org/vigenere-cipher/#)
[^3]: The meaning of life being fourty-two was coined by Douglas Adams in his book, "Hitchhiker's Guide to the Galaxy." In programming, typically fourty-two in ASCII refers to the asterisk, which is used to represent everything. Neat huh!
