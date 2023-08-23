class Member:
    # Class mthod

    user_nam = 0

    def __init__(self, name):
        self.name = name

        Member.user_nam += 1


# instans method
print(Member.user_nam)

member_one = Member("Abeer")
member_two = Member("Ali")
member_three = Member("Ali")

print(Member.user_nam)


def fname(self):
    return f" Hello {self.name}"


print(member_two.name)
print(member_one.name)


# static method
def count(a, b):
    return a * b


print(Member.count(6 + 5))
