from requests import get
import json
import sys


def compare_files(file_a, file_b):
    total_line_a = get_total_line(file_a)
    total_line_b = get_total_line(file_b)

    loop = total_line_a
    not_used_line = 0
    if (total_line_b != total_line_a):
        not_used_line = total_line_b - total_line_a
        if (total_line_b < total_line_a):
            loop = total_line_b

    for i in range(loop):
        el1 = (get_element_on_file(file_a,i)).rstrip("\n")
        el2 = (get_element_on_file(file_b,i)).rstrip("\n")

        compare_responses(el1, el2)

    if (not_used_line < 0):
        print(str(abs(not_used_line)) + " last line is not used on " + file_a)
    elif (not_used_line > 0):
        print(str(not_used_line) + " last line is not used on " + file_b)


def get_row(fileA, fileB):
    row_a = get_total_line(fileA)
    row_b = get_total_line(fileB)
    total_row = row_a
    if(row_b < row_a):
        total_row = row_b
    return total_row


def get_total_line(file):
    with open(file) as f:
        count = sum(1 for _ in f)
        return count


def get_element_on_file(file, line):
    with open(file) as f:
        lines = f.readlines()
        return lines[line]


def compare_responses(res_a, res_b):
    e1 = get_response(res_a)
    e2 = get_response(res_b)

    if (not e1):
        print(res_a + " is not valid Endpoint in First File")
    elif (not e2):
        print(res_b + " is not valid Endpoint in Second File")
    else:
        if (res_a==res_b):
            print(res_a + " equals " + res_b)
        else: print(res_a + " not equals " + res_b)


def get_response(endpoint):
    try:
        res = get(endpoint)
        js = res.json()
        return json.dumps(js, sort_keys=True)
    except Exception:
        return False


try:
    if(len(sys.argv) != 3):
        raise ValueError("Please only input 2 files")

    file_a = sys.argv[1]
    file_b = sys.argv[2]
    compare_files(file_a, file_b)
except Exception as e:
    print(e)
