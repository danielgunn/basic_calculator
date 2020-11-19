import PySimpleGUI as sg

# global variable: set of operators and their precedence score
operators_precedence = {"+": 1, "-": 1, "*": 2, "/": 2, ")": 0, "(": 0}

def make_buttons_from_line(text_line):
    r = []
    for c in text_line:
        r.append(sg.Button(c))
    return r

def main():
    layout = [
        [sg.Text("0 " + " " * 30, key="-ANS-")],
        make_buttons_from_line("789()"),
        make_buttons_from_line("456/*"),
        make_buttons_from_line("123+-"),
        make_buttons_from_line("0=")
    ]

    # Create the window
    window = sg.Window("Gunn Calculator", layout)

    # Create an event loop
    ans = ""
    while True:
        event, values = window.read()
        # End program if user closes window
        if event == sg.WIN_CLOSED:
            break
        elif event in "0123456789":
            ans += event
            window["-ANS-"].update(ans)
        elif event in "+/-*()":
            ans += " " + event + " "
            window["-ANS-"].update(ans)
        elif event == "=":
            ans = str(evaluate_expression(ans))
            window["-ANS-"].update(ans)

    window.close()

# Stack Data Structure - A Last in first out collection (LIFO)
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        #print("push called:", data)
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

# Shunting Yard Algorithm
# Returns a postfix set of tokens given an infix set
def shunting_yard_algorithm(infix_tokens):
    operator_stack = Stack()
    postfix_tokens = []
    depth = 0  # how many layers deep of brackets are we?
    for x in infix_tokens:
        # print("Token:",x)
        if x in operators_precedence.keys():
            if x == "(":
                depth += 1
                operator_stack.push(x)
            elif x == ")":
                while (not operator_stack.is_empty()):
                    op = operator_stack.pop()
                    if op == "(":
                        depth -= 1
                        break
                    else:
                        postfix_tokens.append(op)
            else:
                while ((not operator_stack.is_empty()) and (
                        operators_precedence[operator_stack.peek()] > operators_precedence[x])):
                    op = operator_stack.pop()
                    if op not in ("(", ")"):
                        postfix_tokens.append(op)
                operator_stack.push(x)
        else:
            postfix_tokens.append(x)
    while (not operator_stack.is_empty()):
        op = operator_stack.pop()
        if op not in ("(", ")"):
            postfix_tokens.append(op)
    return postfix_tokens


def evaluate_expression(line_in):
    infix_tokens = line_in.split()
    postfix_tokens = shunting_yard_algorithm(infix_tokens)
    print("POSTFIX",postfix_tokens)

    # Evaluate the RPN
    operator_stack=[]
    for x in postfix_tokens:
        if x in operators_precedence.keys():
            a = float(operator_stack.pop())
            b = float(operator_stack.pop())
            c = 0
            if x == "+":
                c = a + b
            elif x == "-":
                c = b - a
            elif x == "*":
                c = a * b
            else:
                c = b / a
            operator_stack.append(c)
        else:
            operator_stack.append(x)
    answer = operator_stack.pop()
    return answer

if __name__ == "__main__":
    main()
