#!/usr/bin/env bash

echo "file1.txt" > /home/dario/file1.txt
echo "file2.txt" > /home/dario/file2.txt
 

cat /home/dario/file1.txt | bash -ci 'ohoh'

cat /home/dario/file2.txt | cat  
