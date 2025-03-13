#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * reverse the specified sub string in a string, from `start` to `stop - 1`
 */
void reverse(char *s, int start, int stop) {
    for (int i = 0; i < (stop - start) / 2; i++) {
        char a = s[start + i], b = s[stop - 1 - i];
        s[start + i] = b;
        s[stop - 1 - i] = a;
    }
}

/**
 * remove any spaces at the beginning and end of the specified string,
 * and any duplicated spaces between words
 */
void trimWords(char *s) {
    int duplicatedSpaces = 1, i = 0, deletedCount = 0;
    while (s[i]) {
        printf("%d\n", i - deletedCount);
        s[i - deletedCount] = s[i];
        if (s[i] == ' ') {
            if (!duplicatedSpaces)
                duplicatedSpaces = 1;
            else
                deletedCount++;
        } else {
            duplicatedSpaces = 0;
        }
        i++;
    }
    if (i - deletedCount - 1 >= 0 && s[i - deletedCount - 1] == ' ')
        s[i - deletedCount - 1] = '\0';
    else
        s[i - deletedCount] = '\0';
}

char *reverseWords(char *s) {
    trimWords(s);
    int len = strlen(s);
    reverse(s, 0, len);
    int start = 0, stop = 0;
    while (start < len) {
        while (stop < len && s[stop] != ' ') stop++;
        reverse(s, start, stop);
        start = stop = stop + 1;
    }
    printf("|%s|\n", s);
    return s;
}