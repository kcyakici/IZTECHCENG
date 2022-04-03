#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define SIZE 5

int nums[SIZE] = {0, 1, 2, 3, 4};

void *increment_my_list(void *arg)
{
    for (int i = 0; i < SIZE; i++)
    {
        nums[i] *= -i;
        printf("CHILD: %d \n", nums[i]);
    }
}

int main(int argc, char const *argv[])
{
    int i;
    pthread_t thread1;

    pthread_create(&thread1, NULL, increment_my_list, (void *) 5);

    pthread_join(thread1, NULL);
        for (i = 0; i < SIZE; i++)
        {
            printf("PARENT: %d \n", nums[i]); // WHAT IS THE OUTPUT?
        }
    
    return 0;
}
