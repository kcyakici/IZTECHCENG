#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define SHMSZ 50

void main()
{
    int shmid;
    key_t key = 1234;
    char *shm, *s;

    /* We need to get the segment named "1234", created by the server.*/
    /* Locate the segment.*/
    key = 1234;
    if ((shmid = shmget(key, SHMSZ, 0666)) < 0) 
    {
        perror("shmget");
        exit(1);
    }

    /* Now we attach the segment to our data space. */
    if ((shm = shmat(shmid, NULL, 0)) == NULL) 
    {
        perror("shmat");
        exit(1);
    }

    /* Now read what the server put in the memory. */
    s = shm;

    int i = 0; int k = 0;
    char program[2][10];

    while(*(s++) != NULL)
    {
        if (*(s-1) == ' ')
        {
            program[i][k] = NULL;
            k = 0;
            i++;
        }
        else
        {
            program[i][k] = *(s-1);
            k++;
        }
    }
    program[i][k] = NULL;

    printf("%s\n", program[0]);
    printf("%s\n", program[1]);

    *shm = '*';
    execl("/bin/ls", program[0], program[1], NULL);

    /* Finally, change the first character of the segment to '*', indicating we have read 
     * the segment. */

    exit(0);
}