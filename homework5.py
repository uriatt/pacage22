"""
Documents of Valid Number
"""
class ValidCarNumber:
    def _is_valid(self,number):
        self.number=number
vcn=ValidCarNumber()
vcn._is_valid(777)
print(vcn.number)
import re
pattern="[a-zA-Z0-9]+777(AUDI|BMW|TAYOTA)"
user_input=input("Write your car number for checking  valid:")
if(re.search(pattern,user_input)):
    print("valid number")
else:
    print("invalid number")