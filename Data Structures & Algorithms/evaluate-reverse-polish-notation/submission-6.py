class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        valid_operators = set(['+', '-', '*', '/'])
        int_stack = []
        next_idx = 1
        for token in tokens:
            if token in valid_operators:
                second = int_stack.pop(-1)
                first = int_stack.pop(-1)
                if token == '+':
                    int_stack.append(first + second)
                if token == '-':
                    int_stack.append(first - second)
                if token == '*':
                    int_stack.append(first * second)
                if token == '/':
                    towards_zero = first // second
                    if towards_zero < 0:
                        towards_zero = -1 * (abs(first) // abs(second))
                    int_stack.append(towards_zero)
            else:
                int_stack.append(int(token))
            print(int_stack)
        return int_stack[0]

        

