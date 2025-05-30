#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <string.h>

int main()
{
    DIR *dir;
    struct dirent *entry;

    dir = opendir(".");
    if (dir == NULL)
    {
        perror("ls");
        return EXIT_FAILURE;
    }
    while ((entry = readdir(dir)) != NULL)
    {
        printf("%s\n",entry->d_name);
    }

    closedir(dir);
    return EXIT_SUCCESS;
}