# handling files


def main():
    result = []

    with open('input.txt') as reader:
        for line in reader:
            result.append([int(x) for x in line.strip().split(";")])

    with open("output.txt", "x") as writer:
        for line_i in result:
            sum = 0
            line_o = ''
            for n in line_i:
                if line_o == '':
                    line_o = str(n)
                else:
                    line_o += ';' + str(n)
                sum += n
            line_o += '=' + str(sum)
            writer.write(line_o + '\n')


if __name__ == '__main__':
    main()
