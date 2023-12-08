digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        }

def part2(text:str) -> int:
    total = 0
    for line in text.split('\n'):
        i = 0
        while not is_number(line,i):
            i += 1
        j = -1
        while not is_number(line,j):
            j -= 1

        num = int( digit_for(line,i) + digit_for(line,j))
        total += num

    return total

def is_number(line:str, i:int) -> bool:
    return line[i].isdigit() or is_digit_string(line, i)

def is_digit_string(line:str, i:int) -> bool:
    for digit_str in digits.keys():
        if line[i:].startswith(digit_str):
            return True
    return False

def digit_for(line: str, i:int) -> str:
    if line[i].isdigit():
        return line[i]
    for digit_str, val in digits.items():
        if line[i:].startswith(digit_str):
            return val
    return ""


def main():
    import sys
    if len(sys.argv) != 2:
        print(f'usage: {sys.argv[0]} input-file')
        sys.exit(1)

    with open(sys.argv[1]) as f:
        text = f.read()

    result = part2(text.strip())

    print(result)



if __name__ == '__main__':
    main()
