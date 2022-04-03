#include <sys/types.h>
#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>

#define SIZE 5

int nums[SIZE] = {0, 1, 2, 3, 4};

int main(int argc, char const *argv[])
{
    int i;
    pid_t pid;

    pid = fork();

    if (pid == 0)
    {
        for (i = 0; i < SIZE; i++)
        {
            int *ptr = &nums[0];
            *(ptr+i) = nums[i] * nums[i];
            printf("CHILD: %d \n", *(ptr+i)); // WHAT IS THE OUTPUT?
        }
    }
    else if (pid > 0)
    {
        wait(NULL);
        for (i = 0; i < SIZE; i++)
        {
            printf("PARENT: %d \n", nums[i]); // WHAT IS THE OUTPUT?
        }
    }
    return 0;
}
