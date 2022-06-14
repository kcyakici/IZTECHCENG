#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

/*        
        NOTES: 
        
        - Pipe is a one-way communication only.
          (If you need two-way communication, you can have 2 pipes.)
        
        **- Pipes are treated as a special type of file ("virtual file"):
        - Thus; use write(), read() system calls.

        Limitations:

        - There are two processes. One is reader, one is writer.
        - These processes should be related (e.g. a parent and a child).

        (Note: If you want to communicate two unrelated processes using pipes, use "named pipes". mkpipe())

*/

#define BUFFER_SIZE 40
#define READ_END 0
#define WRITE_END 1

int main() 
{

    int fd[2];
    
    // create pipe with fd array.
    // if it does not return with 0;

    /**
     * fd[0] will be the fd(file descriptor) for the read end of pipe.
     * fd[1] will be the fd for the write end of pipe.
     * Returns : 0 on Success and -1 on Error */

    if (pipe(fd) < 0)
    {
        printf("There is a problem in pipe creation.");
    }

    pid_t process_id = fork();   

    if (process_id > 0)     // this is the parent process 
    {
        printf("Parent process -- Start\n");
        char sent_message1[BUFFER_SIZE] = "Operating Systems";
        char sent_message2[BUFFER_SIZE] = "CENG 313";

        //close and write are the system calls (system functions)
        //first close read side.

        //sent_message1 to the child process
        write(fd[WRITE_END], sent_message1, BUFFER_SIZE);        // two write functions are called sequentially
                                                                 // messages will be concatenated.
        //sent_message2 to the child process
        write(fd[WRITE_END], sent_message2, BUFFER_SIZE);        // third message will also be concatenated. 

        //sent_message1 to the child process
        write(fd[WRITE_END], sent_message1, BUFFER_SIZE);
        printf("Parent process -- End\n");
    } 

    else // this is the child process since pid = 0; 
    {
        int counter = 1;

        printf("Child process -- Start\n");

        char received_message[BUFFER_SIZE];
    
        while (read(fd[READ_END], received_message, BUFFER_SIZE) > 0) 
        {
            printf("Message %d: %s\n", counter++, received_message);
        }
        printf("Child process -- End\n");
        printf("XXX");
    }  
    
    return 0;
}

