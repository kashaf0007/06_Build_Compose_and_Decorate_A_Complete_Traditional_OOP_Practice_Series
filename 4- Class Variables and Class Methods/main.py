# 4. Class Variables and Class Methods
class bank:
    bank_name = "ABC Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

bank1 : bank = bank
print(bank1.bank_name)
bank.change_bank_name("XYZ Bank")
print(bank1.bank_name)