class Account:
    def __init__(self, acc_no, acc_name, acc_value):
        self.acc_no = acc_no
        self.acc_name = acc_name
        self.acc_value = acc_value

    def print_information(self):
        print(self.acc_no)
        print(self.acc_name)
        print(self.acc_value)

