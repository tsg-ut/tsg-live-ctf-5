#!/bin/sh

BIN=one-byte-man
SRC=$BIN.c
OUTDIR="./"


gcc -no-pie -o $OUTDIR/$BIN $SRC

