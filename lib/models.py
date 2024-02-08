class Cult:

    all_cults = []
    
    def __init__(self, name, location, founding_year, slogan):
        self.name = name
        self.location = location
        self.founding_year = founding_year
        self.slogan = slogan
        Cult.all_cults.append(self)

    def __repr__(self):
        return f"Cult(name={self.name})"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if type(new_name) is str and 1 <= len(new_name) <= 20:
            self._name = new_name
        else:
            raise Exception("Name must be a string between 1 and 20 characters long")
        
    @property
    def founding_year(self):
        return self._founding_year
    
    @founding_year.setter
    def founding_year(self, new_year):
        if not hasattr(self, "founding_year") and type(new_year) == int and new_year <= 2024:
            self._founding_year = new_year
        else:
            raise Exception("Founding year must be before 2024, of type int, and cannot be changed once set")
        
    def get_blood_oaths(self):
        return [ oath for oath in BloodOath.all_oaths if oath.cult == self ]
    
    def get_followers(self):

        followers_list = [ oath.follower for oath in BloodOath.all_oaths if oath.cult == self ]

        return list(set(followers_list))
    
    def recruit_follower(self, follower_arg):
        return BloodOath(cult=self, follower=follower_arg)

    def get_cult_population(self):
        return len( self.get_followers() )

    def get_average_age(self):
        ages = [ follower.age for follower in self.get_followers() ]

        if len(ages) == 0:
            return 0.0

        return float( sum(ages) / len(ages) )
    
    def get_follower_mottos(self):
        return [ follower.life_motto for follower in self.get_followers() ]
    
    @classmethod
    def find_by_name(cls, searched_name):
        cults_with_name = [ cult for cult in Cult.all_cults if cult.name == searched_name ]
        if len(cults_with_name) == 0:
            return None
        else:
            return cults_with_name[0]
        
    @classmethod
    def get_least_popular(cls):
        # get list of cults
        sorted_cults = sorted( Cult.all_cults, key = lambda cult: len(cult.get_followers()) )
        return sorted_cults[0]
        # sort that list
        # create list of cults for each oath
        # if the first number of sorted list is equal to the number of followers in oath list
        # return first number of that list


class Follower:
    
    def __init__(self, name, age, life_motto):
        self.name = name
        self.age = age
        self.life_motto = life_motto

    def __repr__(self):
        return f"Follower(name={self.name})"

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if type(new_age) == int and 0 <= new_age <= 120:
            self._age = new_age
        else:
            raise Exception("Age must be an int between 0 and 120 inclusive")
        
    def get_blood_oaths(self):
        return [ oath for oath in BloodOath.all_oaths if oath.follower == self ]
    
    def get_cults(self):
        cults_list = [ oath.cult for oath in BloodOath.all_oaths if oath.follower == self ]
        return list( set( cults_list ) )


class BloodOath:

    all_oaths = []
    
    def __init__(self, cult, follower):
        self.cult = cult
        self.follower = follower
        BloodOath.all_oaths.append(self)

    def __repr__(self):
        return f"BloodOath(cult_name={self.cult.name} follower_name={self.follower.name})"

    @property
    def cult(self):
        return self._cult
    
    @cult.setter
    def cult(self, new_cult):
        if isinstance(new_cult, Cult) and not hasattr(self, "cult"):
            self._cult = new_cult
        else:
            raise Exception("Cult cannot be changed and must be of type Cult")

    @property
    def follower(self):
        return self._follower
    
    @follower.setter
    def follower(self, new_follower):
        if isinstance(new_follower, Follower) and not hasattr(self, "follower"):
            self._follower = new_follower
        else:
            raise Exception("Follower cannot be changed and must be of type Follower")