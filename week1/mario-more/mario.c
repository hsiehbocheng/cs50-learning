#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;
    do
    {
        height = get_int("Hight: ");
    }
    while (1>height | height>8);

    int i;
    int j;
    for (i = 1; i <= height; i++)
    {
        for (j = 1; j <= height-i; j++)
        {
            printf(" ");
        }
        for (j = 1; j <= i; j++)
        {
            printf("#");
        }
        printf(" ");
        for (j = 1; j <= i; j++)
        {
            printf("#");
        }
        for (j = 1; j <= height-i; j++)
        {
            printf(" ");
        }
        printf("\n");

    }
}