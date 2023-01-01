# Final-Project-Github
 CSC 2280 Final Project Riley Sweeting

My Final Project is a Cryptography Program with 5 Main Functions/Options

1) Encrypt A Message: 
The User will input a message to be encrypted, followed by the desired key when prompted to do so.
This also has 2 submenus, Ceasar and Vigenere Cipher, depending on which method you want to use.
At the end of both of these functions, you will be asked whether you want to copy the encoded to a clipboard,
and whether you want to select another task.

2) Decrypt A Message:
The User will input a message to be decrypted, followed by the key used to encrypt it when prompted to do so.
This also has 2 submenus, Ceasar and Vigenere Cipher, depending on which method you used to encrypt the message.
At the end of both of these functions, you will be asked whether you want to copy the decoded to a clipboard,
and whether you want to select another task.

3) Bruteforce a Ciphertext: DISCLAIMER!! This option ONLY works for a Caesar Cipher. This part of the program will
prompt you to enter a CAESAR encoded message, to which it will attempt to decode for you, without a key. This works
with reasonable accuracy. Whenever I test it on my own, it nearly always gives the correct message to me first try,
but when I show it to others, it does not for some unlucky reason. Regardless, it should take the program no more than
3 tries to get it correct. The program will ask you if the possible message looks to be the correct decrypted one,
to which you will respond "yes" or "no". 

4) Cryptography History: This option simply gives a short explanation of how the ciphers work, and a brief history of them.
You will also be prompted to select whether you want a wikipedia article to be copied to your clipboard.

5) Exit: This option, Exits the program. If you choose to not select another task earlier in the program, it will
also exit the program. 