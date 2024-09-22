# Write a Python program that repeatedly reads lines from standard input
# until an EOFError is raised, and then outputs those lines in reverse order
# (a user can indicate end of input by typing ctrl-D)

def read_lines():
    lines = []
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        print("error")
    return lines

def main():
    lines = read_lines()
    for line in reversed(lines):
        print(line)

if __name__ == "__main__":
    main()
