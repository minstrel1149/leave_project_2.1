import random
import string

first_name_samples = '김이박최정강조윤장임'
middle_name_samples = '민서예지도하주윤채현지준'
last_name_samples = '준윤우원호후서연아은진태'

def random_name():
    name = ''
    name += random.choice(first_name_samples)
    name += random.choice(middle_name_samples)
    name += random.choice(last_name_samples)
    return name