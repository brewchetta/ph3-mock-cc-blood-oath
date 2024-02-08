from lib.models import Cult, Follower, BloodOath
from faker import Faker
from random import choice as random_choice

# you can use faker to create test data
# for example: f1 = Follower(name=faker.name(), age=20, life_motto="Yay mottos!")
faker = Faker()

##### TEST DATA ##########

c1 = Cult(name="Flatiron Cult", location=faker.country(), founding_year=2012, slogan=faker.text())
c2 = Cult(name="TKE", location=faker.country(), founding_year=1899, slogan=faker.text())
c3 = Cult(name="Scientology", location=faker.country(), founding_year=1950, slogan=faker.text())

cults = [c1, c2, c3]

ages = list(range(0,121))
f1 = Follower(name=(faker.name()), age=(random_choice(ages)), life_motto={faker.text()})
f2 = Follower(name=(faker.name()), age=(random_choice(ages)), life_motto={faker.text()})
f3 = Follower(name=(faker.name()), age=(random_choice(ages)), life_motto={faker.text()})
f4 = Follower(name=(faker.name()), age=(random_choice(ages)), life_motto={faker.text()})
f5 = Follower(name=(faker.name()), age=(random_choice(ages)), life_motto={faker.text()})
f6 = Follower(name=(faker.name()), age=(random_choice(ages)), life_motto={faker.text()})
f7 = Follower(name=(faker.name()), age=(random_choice(ages)), life_motto={faker.text()})
f8 = Follower(name=(faker.name()), age=(random_choice(ages)), life_motto={faker.text()})
f9 = Follower(name=(faker.name()), age=(random_choice(ages)), life_motto={faker.text()})
followers = [f1, f2, f3, f4, f5, f6, f7, f8, f9]

b1 = BloodOath(cult=(random_choice(cults)), follower=(random_choice(followers)))
b2 = BloodOath(cult=(random_choice(cults)), follower=(random_choice(followers)))
b3 = BloodOath(cult=(random_choice(cults)), follower=(random_choice(followers)))
b4 = BloodOath(cult=(random_choice(cults)), follower=(random_choice(followers)))
b5 = BloodOath(cult=(random_choice(cults)), follower=(random_choice(followers)))
b6 = BloodOath(cult=(random_choice(cults)), follower=(random_choice(followers)))
b7 = BloodOath(cult=(random_choice(cults)), follower=(random_choice(followers)))
b8 = BloodOath(cult=(random_choice(cults)), follower=(random_choice(followers)))
b9 = BloodOath(cult=(random_choice(cults)), follower=(random_choice(followers)))
b10 = BloodOath(cult=(random_choice(cults)), follower=(random_choice(followers)))
b11 = BloodOath(cult=(random_choice(cults)), follower=(random_choice(followers)))
b12 = BloodOath(cult=(random_choice(cults)), follower=(random_choice(followers)))
b13 = BloodOath(cult=(random_choice(cults)), follower=(random_choice(followers)))
b14 = BloodOath(cult=(random_choice(cults)), follower=(random_choice(followers)))
b15 = BloodOath(cult=(random_choice(cults)), follower=(random_choice(followers)))

##### ######### ##########

# import ipdb; ipdb.set_trace()