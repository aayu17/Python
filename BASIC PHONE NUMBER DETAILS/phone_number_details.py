import phonenumbers as pn #pip installl phonenumbers
from phonenumbers import carrier, geocoder, timezone
#phone number +91*********
phone = pn.parse('+919717825681 ')
# check validity of number
print(pn.is_valid_number(phone))
# telecom operator name
print(carrier.name_for_number(phone, 'en'))
# region name
print(geocoder.description_for_number(phone, 'en'))
# timezone of a number
print(timezone.time_zones_for_number(phone))
