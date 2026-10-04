'''
We keep 2 lists: A list of primes, and also a list of Squares of primes.
We start with a seed list of primes, and a matching seed list of sqaures of primes, and then we add (append) to each of them
as we discover more primes in the sequence.
To test for a prime number we divide our suspect by all prime numbers that are less than the square root of our suspect.
As long as the GCD outcome continues to be non zero then the suspect must be be prime.
This version of teh program will work from a low prime such as 11, and then UP TO the nearest square root prime
we can start from 11 because we pre-test all suspects for being divisible by 3,5 and 7 to eliminate trivial non-primes before we start.
As a bit of a sophistication to the division and no remainder test, we use GCD - Greatest Common Divisor -
of the suspect and the known primes just to confirm. The reason for this is so that we can use the GCD function for another
purpose in determining the "probability of prime", or in resolving (factoring or simplifying) fractions.
Except, that I previously had not written the GCD as a stand alone function - it is too tightly embedded into the prime number lists
method, so that change is needed.
2 changes to make:
1) Get the GCD untangled from the lists - DONE, a Def(inition) GcdIterationTest has been created and tested to work with Def ModularDivision.
2) Go up from 11 instead of down to 11. We'll break this down into 2 parts, finding the highest square prime and hence teh index into the list of primes, AND THEN
the GCD test of all the primes from nearest square down to 11. We don't need to do 7, 5 or 3 as we will do a simple division by the trivial primes beforehand. DONE
BUGS
1) now cleared, it was allowing squares of primes through as prime, because for 121 teh checker would only check for prime divisors up to 7, but not 11.
        Fixed this by, once finding the max-pointer, adding one to the max-pointer.
2) The for next loop will not run for low primes in the sequence. Say if you start checking from index 7,
but highest square of prime is 6, or 7, then the for-next loop will not even start, because it can't do "step +1"!
'''
Primes_So_Far = [1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]
Squares_of_Primes_So_Far = [1,4,9,25,49,121,169,289,361,529,841,961,1369,1681,1849,2209,2809]
def GCDTestForPrimes (IndexToHighestPrime,CopyOfPrimeList,SuspectPrime):
        for counter in range(IndexToHighestPrime,3,-1):
                NextDividend=CopyOfPrimeList[counter]
                ''' This is the actual Euclidean GCD test
'''
        return counter
def GcdIterationTest (Higher,Lower):
        Remains, Answer, NextDivisor = ModularDivision(Higher,Lower)
        while Remains!=1:
                if Remains == 0:
                        break
                else:
                        Remains, Answer, NextDivisor = ModularDivision(NextDivisor,Remains)
                continue
                if Remains ==0:
                        break
        return Remains
def ModularDivision (SuspectPrimeOrRemainder,NextMappedPrime):
	Divisor=NextMappedPrime
	Dividend=SuspectPrimeOrRemainder
	Quotient=Dividend
	Remainder=Dividend%Divisor
	return Remainder, Quotient, Divisor
for suspect_prime in range (59, 2001, 2):
        if suspect_prime%3 !=0 and suspect_prime%5 !=0 and suspect_prime%7 !=0:
                suspect_squared = suspect_prime * suspect_prime
                count_squared=1
                while Squares_of_Primes_So_Far[count_squared] < suspect_prime:
                        count_squared = count_squared + 1
                        continue
                ''' Now we have exited with our pointer stored in count_squared Here we go with the test
                '''
                for nextprime in range (4, count_squared+1,1):
                        GCDOutcome = GcdIterationTest (suspect_prime,Primes_So_Far[nextprime])
                        if GCDOutcome ==0:
                                print (suspect_prime, " is not prime, it was divisible by ", Primes_So_Far[nextprime])
                                break
                if GCDOutcome ==1:
                        print (suspect_prime, " is prime")
                        Primes_So_Far.append(suspect_prime)
                        Squares_of_Primes_So_Far.append(suspect_squared)
print (Primes_So_Far)
print (len(Primes_So_Far))
print (Squares_of_Primes_So_Far)