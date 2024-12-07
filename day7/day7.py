from itertools import product


def evaluate_expression(test_value, numbers, operators):
    n = len(numbers)

    for ops in product(operators, repeat=n-1):
        expression = str(numbers[0])
        for i in range(n-1):
            expression += f" {ops[i]} {numbers[i+1]}"

        result = numbers[0]
        for i in range(n-1):
            if ops[i] == '+':
                result += numbers[i+1]
            elif ops[i] == '*':
                result *= numbers[i+1]
            elif ops[i] == '||':
                result = int(str(result)+str(numbers[i+1]))

        if result == test_value:
            return True

    return False


with open("input.txt", 'r') as f:
    equations = f.read().splitlines()
s1, s2 = 0, 0
for eq in equations:
    test_value, numbers = eq.split(": ")
    test_value = int(test_value)
    numbers = list(map(int, numbers.split()))

    if evaluate_expression(test_value, numbers, ['+', '*']):  ## Part I
        s1 += test_value
    if evaluate_expression(test_value, numbers, ['+', '*', '||']):  ## Part II
        s2 += test_value
        
print(s1, s2)
