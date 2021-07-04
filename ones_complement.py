class OnesComplement:
    def __init__(self, number1, number2):
        self.num1 = str(number1)
        self.num2 = str(number2)
        self.complement = ""
        self.sum = ""
        self.carry_over=""
        self.to_be_added =""
        self.final_result=""
        self.make_bits_equal()
        self.ones_complement()
        self.add_numbers()
        self.check_overflow()

    def make_bits_equal(self):
        """
        function to take two binary inputs and make them equal in length.
        :return:
        """
        difference = abs(len(self.num1) - len(self.num2))
        if len(self.num1) == len(self.num2):
            print("Equal")
        elif len(self.num1) > len(self.num2):
            for i in range(difference):
                self.num2 = "0" + self.num2
        elif len(self.num2) > len(self.num1):
            for i in range(difference):
                self.num1 = "0" + self.num1

    def ones_complement(self):
        """
        function to return 1s complement of second number
        :return:
        """
        ones =""
        for bit in self.num2:
            if bit == "1":
                ones += "0"
            else:
                ones += "1"
        self.complement = ones

    def add_numbers(self):
        """
        function that adds the complemented bit to first bit
        :return:
        """
        integer_sum = int(self.complement, 2) + int(self.num1, 2)
        binary_sum = bin(integer_sum)
        self.sum = str(binary_sum[2:])

        if len(self.sum) < len(self.complement):
            difference = len(self.complement) - len(self.sum)
            for i in range(difference):
                self.sum = '0'+self.sum

    def check_overflow(self):
        temp =""
        """
        function that checks overflow (aka carry over) and gives output accordingly
        :return:
        """
        if len(self.sum) > len(self.num2):
            difference = len(self.sum) - len(self.num2)
            self.carry_over = self.sum[:difference]
            self.to_be_added = self.sum[difference:]
            integer_sum = int(self.to_be_added, 2) + int(self.carry_over, 2)
            binary_sum = bin(integer_sum)
            self.final_result = str(binary_sum)[2:]
            return True
        else:
            for digit in self.sum:
                if digit == "1":
                    temp += "0"
                else:
                    temp += "1"
            self.final_result = "-"+ temp
            return False





