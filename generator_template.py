import os
from glob import glob
from random import *

import numba

# Create input and output folders if they don't exist
if not os.path.exists("input"):
    os.makedirs("input")
if not os.path.exists("output"):
    os.makedirs("output")

# Clear input and output folders if they contain anything
files = glob("input/*")
for f in files:
    os.remove(f)
files = glob("output/*")
for f in files:
    os.remove(f)

# You may define upper bounds for different levels as follows
SMALL = 10
MED = 10**6
BIG = 10**12

"""
NO: Test set number.

SET_NAME:
How can you describe this test set?
If it contains small numbers, then call it "small".
If the answer is always -1, call it "answer is always -1".

N_TC: Number of test cases in this set (number of input/output pairs).
"""
NO = 1
SET_NAME = "put-your-set-name-here"
N_TC = 1

# numba.njit is for fast python. You may comment it out in case of errors, or
# you might try to get rid of errors.


@numba.njit
def generate_test_cases(t=1):
    """
    Implement it however you want. It generates t number of customly generated test cases.\n
    In this pseudo implementation, the problem has two parameters a and b and the corresponding
    answers are stored in ans_s.
    """
    a_s, b_s, ans_s = [], [], []

    for i in range(t):
        a = randint(1, SMALL)
        b = randint(5, SMALL)
        ans = 0
        # Solve the problem to obtain ans
        a_s.append(a)
        b_s.append(b)
        ans_s.append(ans)

    return a_s, b_s, ans_s


def write_test_cases_to_file(l, out):
    """Write multiple test cases to the file `out`.

    Args:
        `l` (`List[List]`): Contains the test cases.
        `out`: File to write. Should pass `open("path-to-file", "w")`.
    """

    write_single_test_case_to_file(l[0], out)
    for i, x in enumerate(l[1:]):
        write_single_test_case_to_file(x, out, sep=" ", last=i+1 == len(l[1:]))


def write_single_test_case_to_file(l, out, sep=" ", last=False):
    """Write single test case to the file `out`.

    Args:
        `l` (`List`): Test case to write.
        `out`: File to write.
        `sep` (str, optional): Separator between the numbers in the test case. Defaults to " ".
        `last` (bool, optional): Whether this test case is the last. Defaults to False.
    """

    out.write(f"{l[0]}")
    for x in l[1:]:
        out.write(sep + f"{x}")
    if not last:
        out.write("\n")


for tc in range(N_TC):
    input = open(f"input/input{tc}.txt", "w")
    output = open(f"output/output{tc}.txt", "w")

    t = 10

    a_s, b_s, ans_s = generate_test_cases(t)

    write_single_test_case_to_file([t], input)
    write_test_cases_to_file(list(zip(a_s, b_s)), input)

    write_single_test_case_to_file(ans_s, output, "\n", last=True)

    input.close()
    output.close()

os.system(f"zip -r \"{NO}. {SET_NAME} {N_TC}.zip\" input output")
os.system(f"copy gen.py {NO}.py")
