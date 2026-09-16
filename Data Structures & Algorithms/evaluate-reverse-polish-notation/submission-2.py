class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        captured = []
        for i in range(len(tokens)):
            if tokens[i] not in ['+','-','*',"/"]:
                captured.append(int(tokens[i]))
            else:
                operand2 = captured.pop()
                operand1 = captured.pop()

                match tokens[i]:
                    case '+':
                        self.operate(captured, '+', operand1=operand1, operand2=operand2)
                    case '*':
                        self.operate(captured, '*', operand1=operand1, operand2=operand2)
                    case '-':
                        self.operate(captured, '-', operand1=operand1, operand2=operand2)
                    case '/':
                        self.operate(captured, '/', operand1=operand1, operand2=operand2)
                        
        return int(captured[0])

    
    def operate(self, captured, operator, **kwargs):
        operand1 = kwargs.get('operand1', None)
        operand2 = kwargs.get('operand2', None)

        if operator == '+':
            captured.append(operand1 + operand2)
        elif operator == '*':
            captured.append(operand1 * operand2)
        elif operator == '-':
            captured.append(operand1 - operand2)
        elif operator == '/':
            captured.append(int(operand1 / operand2))
            



