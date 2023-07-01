import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder


def Country_Pro():
    number=input("Enter your number: ")
    pepnumber =phonenumbers.parse(number)
    location = geocoder.description_for_number(pepnumber, "en")
    print(location)

    service_pro=phonenumbers.parse(number)
    print(carrier.name_for_number(service_pro, "en"))