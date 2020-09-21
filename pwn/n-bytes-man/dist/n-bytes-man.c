#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void setup() {
    alarm(60);
    setvbuf(stdout, 1, _IONBF, 0);
    setvbuf(stdin, 1, _IONBF, 0);
    puts("Hi!");
    puts("Welcome to TSG Live 5!");
    puts("This is Live CTF. Enjoy :)");
}

unsigned readn(char *buf, unsigned size) {
    char c;
    unsigned cnt = 0;
    for (unsigned i = 0; i < size; i++) {
        unsigned x = read(0, buf + i, 1);
        cnt += x;
        c = buf[cnt - 1];
        if (x != 1 || c == '\n') break;
    }
    if (c == '\n') buf[cnt-1] = '\x00';
    return cnt;
}


int main(void) {
    unsigned long long addr;
    unsigned long long size;
    char buf[0x20];
    setup();
    write(1, "address: ", 9);
    readn(buf, 0x1f);
    addr = strtoull(buf, NULL, 10);
    write(1, "size: ", 9);
    readn(buf, 0x1f);
    size = strtoull(buf, NULL, 10);
    write(1, (char*)addr, size);
    write(1, "data: ", 6);
    readn((char *)addr, size);
    exit(0);
}


void friend() {
    execl("/bin/sh", "sh", NULL);
}

