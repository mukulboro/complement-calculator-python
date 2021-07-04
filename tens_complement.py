class TensComplement:

    def __init__(self, number1, number2):
        self.num1 = number1
        self.num2 = number2
        self.complement = ""
        self.ones = ""
        self.sum = ""
        self.final_result = ""
        self.make_bits_equal()
        self.twos_complement()
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

    def twos_complement(self):
        """
        function to return 2s complement of second number
        :return:
        """
        for bit in self.num2:
            self.ones += str(9 - int(bit))
        integer_sum = int(self.ones) + 1

        self.complement = str(integer_sum)
        # mathi ko complement le agadi ko zero lai negate garchha, which may cause error in next step
        if len(self.complement) < len(self.num2):
            difference = len(self.num2)-len(self.complement)
            for i in range(difference):
                self.complement = "0"+self.complement

    def add_numbers(self):
        """
        function that adds the complemented bit to first bit
        :return:
        """
        integer_sum = int(self.complement) + int(self.num1)

        self.sum = str(integer_sum)

        if len(self.sum) < len(self.complement):
            difference = len(self.complement) - len(self.sum)
            for i in range(difference):
                self.sum = '0'+self.sum

    def check_overflow(self):
        """
        function that checks overflow (aka carry over) and gives output accordingly
        :return:
        """
        if len(self.sum) > len(self.num2):
            difference = int(len(self.sum) - len(self.num2))
            self.final_result = self.sum[difference:]
            return True
        else:
            temp=""
            for bit in self.sum:
                temp += str(9 - int(bit))

            integer_sum = int(temp) + 1

            self.final_result = str(integer_sum)
            return False