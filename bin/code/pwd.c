#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <limits.h>

int main()
{
    char path[PATH_MAX];

    if (getcwd(path,PATH_MAX) != NULL)
    {
        printf("%s\n",path);
    }else{
        perror("pwd");
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}