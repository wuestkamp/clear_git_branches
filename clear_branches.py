import sys
import subprocess
import argparse

parser = argparse.ArgumentParser(description='Clear already merged branches')
parser.add_argument('base_branch', help='select master for example')
parser.add_argument('operation', help='ls or rm', choices=['ls', 'rm'])
parser.add_argument('--filter', help='Filter for branches that start with')
args = parser.parse_args()


def main():
    if args.operation == 'ls':
        ls()
    elif args.operation == 'rm':
        rm()


def run_command(cmd):
    # print(cmd)
    try:
        output = subprocess.check_output(cmd, shell=True).decode(sys.stdout.encoding)
    except subprocess.CalledProcessError as e:
        output = "ERROR: " + e.output
    return output


def get_branch_list():
    output = run_command("git branch --merged " + args.base_branch)
    output_list = output.split("\n")
    branch_list = []
    for line in output_list:
        line = line.strip()
        if (args.filter is None or line.startswith(args.filter)) and args.base_branch not in line and line:
            branch_list.append(line)

    if len(branch_list) == 0:
        print("No branches found.")
    else:
        print("The following branches will be removed!")

    return branch_list


def ls():
    branch_list = get_branch_list()
    for branch in branch_list:
        print(branch)


def rm():
    branch_list = get_branch_list()
    for branch in branch_list:
        output = run_command("git push origin " + branch + " --delete")
        print(output)

        output = run_command("git branch -D " + branch)
        print(output)


main()
