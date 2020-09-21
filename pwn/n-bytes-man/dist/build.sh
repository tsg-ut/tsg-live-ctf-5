#!/bin/sh

BIN=n-bytes-man
SRC=$BIN.c
OUTDIR="./"


gcc -no-pie -o $OUTDIR/$BIN $SRC

