# Encryption-from-scratch
Out of personal interest. Absolutely no security guarantees. I did not know how encryption algorithms worked and decided to have a crack at it. I would call this a fairly succesful attempt at hashing and symmetric encryption, though it still has some room for optimizing which I may get around to at some point.


The main property I was trying to achieve was that if you have E(text, key) and you change even one bit of the key, the new output would not have any clear realtionship to the original one.


Hashing here is implemented as H(text) = E('AAAAAAAAA', text)
Basically, we use the encryption algorithm, but put in the string we want to hash as the key instead of the input. Thus, since we use a constant as the string we are "encrypting", we get an output of constant size, which also changes completely when the input string is changed even slightly.
