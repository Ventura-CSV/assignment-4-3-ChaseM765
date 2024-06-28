def main():
    number = int(input('Enter your input: '))
    result = []
    while True:
        x = number // 2
        rem = number % 2
        result.append(rem)
        if x > 0:
            number = x
        else:
            break

    print(*result)
    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
