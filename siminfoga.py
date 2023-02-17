# Phone Number Details
#author technicalhayden

import phonenumbers
from phonenumbers import timezone, geocoder, carrier, phonemetadata
import socket
number = input("Enter your Number with +_ _: ")

phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone, "en")
reg = geocoder.description_for_number(phone, "en")
meta = phonemetadata.PhoneMetadata
i = phonenumbers.is_valid_number(phone, )
h = phonemetadata.PhoneMetadata(phone, "en")

print(phone)
print(time)
print(car)
print(reg)
print(i)
print(h)

