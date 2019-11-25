We've all seen Fibonacci sequences. But they are all played out. Let's look at a different sequence. They are called Hamming Numbers  after Richard Hamming, who proposed the problem of finding computer algorithms for generating these numbers in ascending order.

For number H is equal to 2**i * 3**j * 2**k where i,k,k are all non negative. 

For example 
2**0 * 3**0 * 5**0 = 1 
2**1 * 3**0 * 5**0 = 2
2**0 * 3**1 * 5**0 = 3
2**2 * 3**0 * 5**0 = 4
2**0 * 3**0 * 5**1 = 5
2**2 * 3**1 * 5**0 = 6
2**3 * 3**0 * 5**0 = 8

So hopefully that explains what the sequence looks like. Your challenge, if you choose to accept it is to generate the first 25 of them. An arbitrary nth one such as 1700th. And given a number X determine if it is or is not a valid hamming number. 

Here is the wiki article on them:

https://en.wikipedia.org/wiki/Regular_number


