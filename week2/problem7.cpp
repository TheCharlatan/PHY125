/*By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?*/

#include <iostream>
#include <math.h>
using namespace std;

bool isprime(long tester)
{
	if (tester % 2 == 0)
		return false;
	else if (tester % 3 == 0)
		return false;
	else if (tester % 5 == 0)
		return false;
	else
	{
		long parser (3);
		while (parser != tester/2)
		{
			parser++;
			if (tester % parser == 0)
				return false;
		}
		return true;
	}
}

int main ()
{
	int position = 7;
	long number = 17;
	while (position < 10001)
	{
		number++;
		if (isprime(number))
		{
			position++;
			number++;
		}
	}
	cout << "Just say something: " << number;
}
