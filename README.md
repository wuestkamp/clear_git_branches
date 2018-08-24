Clear Git Branches
=================

Simple python script to remove already merged branches in your local and remote (origin by default).

usage
------------
run in your git repo directory

`python3 clear_branches.py master ls` shows all branches already merged in master

`python3 clear_branches.py master rm` removes all branches already merged in master (local and remote!)

options
------------

`python3 clear_branches.py --filter feature master ls` will only consider branches starting with "feature"

`python3 clear_branches.py --filter --remote origin2 ls` will remove branches from remote "origin2" (and local!)
