#!/bin/sh

rm -rf dist
mkdir -p dist
cp -r build/env dist/
cp Dockerfile dist/Dockerfile
cd dist
tar czvf env.tar.gz env

