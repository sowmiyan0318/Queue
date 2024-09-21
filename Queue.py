from collections import deque

class BankLine:
    def __init__(self):
        self.line = deque()

    def join_line(self, name):
        self.line.append(name)
        print(f"{name} joins the line")
        self.print_line()

    def serve_customer(self):
        if self.line:
            name = self.line.popleft()
            print(f"{name} is served")
            self.print_line()
        else:
            print("No customers in line")

    def leave_line(self, name):
        if name in self.line:
            self.line.remove(name)
            print(f"{name} leaves the line")
            self.print_line()
        else:
            print(f"{name} is not in the line")

    def print_line(self):
        print(f"Current line: {list(self.line)}")


# Example usage:
bank_line = BankLine()

bank_line.join_line("John")
bank_line.join_line("Mary")
bank_line.join_line("David")

bank_line.serve_customer()

bank_line.leave_line("Mary")

bank_line.serve_customer()

bank_line.serve_customer()
