Simple python script to remove already merged branches in your local and origin.

usage, run in your git repo directory:

`python3 clear_branches.py master ls`
`python3 clear_branches.py master rm`

or more customizable:

`python3 clear_branches.py --filter feature master ls` will only consider branches starting with feature
`python3 clear_branches.py --filter --remote origin2 ls` will remove branches from this origin
