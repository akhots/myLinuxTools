#!/bin/bash
echo 'processing...'
sudo tree / -ifDsa | grep -v -E " ./dev| ./run| ./sys| ./snap| -> | /proc" > \
disk-tree-$(date '+%Y-%m-%d-%H-%M').txt
echo 'done'
