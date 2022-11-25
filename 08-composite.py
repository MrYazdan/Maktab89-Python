from random import randint


class Human:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def __repr__(self):
        return f"Human -> {self.fname} {self.lname}"


class Phone:
    def __init__(self, country_code, phone_number, operator):
        self.country_code = country_code
        self.phone_number = phone_number
        self.operator = operator


class Email:
    def __init__(self, email, email_provider):
        self.email = email
        self.email_provider = email_provider


class Profile:
    def __init__(self, human, phone, email):
        self.__profile_id = randint(111, 999)
        self.human = human  # instance ?
        self.phone = phone
        self.email = email


# Components:
ali = Human(fname="Ali", lname="Zandi", age=36)
ali_mail = Email("ali@outlook.com", "microsoft")
ali_phone = Phone("+98", "09134445555", "mci")
profile = Profile(ali, ali_phone, ali_mail)

print(profile.human.lname)


def check_phone_with_email_is_valid(*arg):
    pass


# Composition
class Profile:
    def __init__(self, fname, lname, age, country_code, phone_number, operator, email, email_provider):

        assert check_phone_with_email_is_valid(phone_number, email)

        self.email = Email(email_provider=email_provider, email=email)
        self.phone = Phone(country_code=country_code, phone_number=phone_number, operator=operator)
        self.human = Human(fname=fname, lname=lname, age=age)
