#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long number = get_long("Number: ");
    long output = 0;
    int start;
    int dig;
    int i = 1;
    while (number != 0)
    {
        if ( i % 2 == 0)
        {
            dig = (number % 10) * 2;
            if (dig > 9)
            {
                output += dig % 10;
                output += dig / 10;
            }
            else
            {
                output += dig;
            }
        }else
        {
            output += number % 10;
        }
        i ++;
        number /= 10;
        if (number > 10)
        {
            start = number;
        }
    }
    i -= 1;

    if (i != 13 && i != 15 && i != 16)
    {
        printf("dINVALID\n");
    }else if (output % 10 != 0)
    {
        printf("oINVALID\n");
    }else if (i == 15 && (start == 34 || start == 37))
    {
        printf("AMEX\n");
    }else if (i == 16 && (start >= 51 && start <= 55))
    {
        printf("MASTERCARD\n");
    }else if (start / 10 == 4)
    {
        printf("VISA\n");
    }else
    {
        printf("fINVALID\n");
    }

}