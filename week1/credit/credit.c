#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long number = get_long("Number: ");
    long output = 0;
    int i = 1;
    while (number != 0)
    {
        if ( i % 2 == 0)
        {
            output += (number % 10) * 2;
        }else
        {
            output += number % 10;
        }
        i ++;
        number /= 10;
    }

    if (i != 13 && i != 15 && i != 16)
    {
        printf("INVALID\n");
        return 0;
    }

    long start = i;
    do
    {
        start = start / 10;
    }
    while (start > 100);

    

    if (output % 10 == 0)
    {
        printf("VISA\n");
    }else
    {
        printf("INVALID\n");
    }
}