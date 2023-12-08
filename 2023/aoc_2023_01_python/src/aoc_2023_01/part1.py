def part1(text:str) -> int:

    total = 0
    for line in text.split('\n'):
        i = 0
        while not line[i].isdigit():
            i += 1
        j = -1
        while not line[j].isdigit():
            j -= 1

        num = int(line[i] + line[j])
        total += num

    return total

def main():
    import sys
    if len(sys.argv) != 2:
        print(f'usage: {sys.argv[0]} input-file')
        sys.exit(1)

    with open(sys.argv[1]) as f:
        text = f.read()

    result = part1(text.strip())

    print(result)



if __name__ == '__main__':
    main()
