#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int n;
    do
    {
        n = get_int("Start size: ");
    }
    while (n < 9);
    // TODO: Prompt for end size
    int s;
    do
    {
        s = get_int("End size: ");
    }
    while (s < n);
    // TODO: Calculate number of years until we reach threshold
    int y = 0;
    do
    {
        n = n + (n/3) - (n/4);
        y ++;
    }
    while (s > n);
    // TODO: Print number of years
    printf("Years: %i\n", y);
}
