#!/bin/bash
TIMESTAMP=$(date "+%Y-%m-%d_%H-%M-%S")
fswebcam -r 640x480 --no-banner intruder.jpg
echo "[$TIMESTAMP] Wrong attempt" >> logs/attempts.txt
system("echo Wrong password attempt >> logs.txt");
