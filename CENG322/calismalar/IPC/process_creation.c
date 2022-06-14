#include <sys/types.h>
#include <sys/wait.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


/**
 * A parent may terminate the execution of one of its children for a variety of reasons, such as these:

 * The child has exceeded its usage of some of the resources that it has been allocated. 
 * (To determine whether this has occurred, the parent must have a mechanism to inspect the state of its children.)

 * The task assigned to the child is no longer required.

 * The parent is exiting, and the operating system does not allow a child to continue if its parent terminates.
 */

int main()
{
	/* a signed integer type which is capable of representing a process ID */
	pid_t pid;

	/* fork a child process */
	pid = fork();
	
	/* error occurred */
	if (pid < 0) 
	{ 
		fprintf(stderr, "Fork Failed");
		return 1;
	}
	
	 /* child process */
	else if (pid == 0) 
	{
		printf("Child process starts\n");
		printf("PID of child process is %d\n", getpid());
//		printf("PID of parent process is %d\n", getppid());

	/*  execl(const char *file, const char *arg, ...);  */
//	    execl("/bin/ls", "ls", "-l", "-R", NULL);

		/* ls will list files and folders */
//		char* arr[] = {"ls", "-l", "-R", "-a", NULL};
//		execv("/bin/ls", arr);
 
		/* file is the /bin/ps */
//		execl("/bin/ps", "ps", "-el", NULL);

/*
		char *cmd = "grep"; //"ls";
		char *argv[4];
		argv[0] = "grep";
		argv[1] = "-r"; // -la all
		argv[2] = "process";
		argv[3] = NULL;

		execvp(cmd, argv); // command should be defined in PATH variable. 
*/
		printf("Child process ends\n");
		exit(0);
		printf("We cannot see this\n");
	}

	/* parent process */
	/* parent will wait for the child to complete */	
	else 
	{
		printf("Parent process starts\n");
		int x = 0;
//		wait(&x);
		waitpid(-1, &x, 0);
		printf("Return status of child process = %d\n", x);
		printf("Parent process ends\n");
	}
	return 0;
}