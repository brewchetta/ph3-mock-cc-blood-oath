import pytest

from models import Cult, Follower, BloodOath

def create_cult(name="Super Cult", location="Super Cult Location", founding_year=1999, slogan="We are Super Cult!"):
    return Cult(name=name, location=location, founding_year=founding_year, slogan=slogan)

def create_follower(name='Bob', age=20, life_motto="Yay"):
    return Follower(name=name, age=age, life_motto=life_motto)

class TestCult:
    """ [TESTING SUITE: <Cult>] """

    # __INIT__ #

    def test_has_name(self):
        """ (INITIALIZERS AND PROPERTIES) A cult's name must be set upon initialization. """
        cult = create_cult()
        assert (cult.name == "Super Cult")

    def test_has_location(self):
        """ (INITIALIZERS AND PROPERTIES) A cult's founding_year must be set upon initialization. """
        cult = create_cult()
        assert (cult.founding_year == 1999)

    def test_has_founding_year(self):
        """ (INITIALIZERS AND PROPERTIES) A cult's founding_year must be set upon initialization. """
        cult = create_cult()
        assert (cult.founding_year == 1999)

    def test_has_slogan(self):
        """ (INITIALIZERS AND PROPERTIES) A cult's founding_year must be set upon initialization. """
        cult = create_cult()
        assert (cult.founding_year == 1999)
        cult = create_cult()

    # NAME PROPERTY #

    def test_name_setter(self):
        """ (INITIALIZERS AND PROPERTIES) A cult's name must be between 1 and 20 characters long. """
        cult = create_cult()
        cult.name = "Ultra Cult"
        assert (cult.name == "Ultra Cult")
        with pytest.raises(Exception):
            cult.name = ""
        with pytest.raises(Exception):
            cult.name = "123456789012345678901"

    def test_name_is_string(self):
        """ (INITIALIZERS AND PROPERTIES) A cult's name must be of type `str`. """
        cult = create_cult()
        assert (isinstance(cult.name, str))
        with pytest.raises(Exception):
            cult.name = 777
    
    # FOUNDING YEAR PROPERTY #

    def test_founding_year_setter(self):
        """ (INITIALIZERS AND PROPERTIES) A cult's founding_year cannot changed once set. """
        cult = create_cult()
        with pytest.raises(Exception):
            cult.founding_year = 2000

    def test_founding_year_is_int(self):
        """ (INITIALIZERS AND PROPERTIES) A cult's founding_year cannot changed once set. """
        cult_one = create_cult()
        assert(type(cult_one.founding_year) == int)
        with pytest.raises(Exception):
            create_cult(founding_year="not a year")

    def test_founding_year_cannot_be_future_years(self):
        """ (INITIALIZERS AND PROPERTIES) A cult's founding_year cannot be a future year. """

        import datetime
        this_year = datetime.date.today().year

        cult = create_cult(founding_year=this_year)
        assert(cult.founding_year == this_year)
        with pytest.raises(Exception):
            create_cult(founding_year=this_year + 10)


    # OBJECT RELATIONSHIPS #

    def test_has_many_blood_oaths(self):
        """ (OBJECT RELATIONAL METHODS) A cult must be able to associate to many blood_oaths. """
        cult_1 = create_cult()
        cult_2 = create_cult(name="Ultra Cult")
        follower = Follower('Bob', 20, "Yay")
        follower_2 = Follower('Jim', 21, "Yay")
        follower_3 = Follower('Pam', 22, "Yay")
        oath_1 = BloodOath(cult_1, follower)
        oath_2 = BloodOath(cult_1, follower_2)
        oath_3 = BloodOath(cult_2, follower_3)

        assert (len(cult_1.get_blood_oaths()) == 2)
        assert (len(cult_2.get_blood_oaths()) == 1)
        assert (oath_1 in cult_1.get_blood_oaths())
        assert (oath_2 in cult_1.get_blood_oaths())
        assert (oath_3 in cult_2.get_blood_oaths())
        assert (not oath_3 in cult_1.get_blood_oaths())

    def test_blood_oaths_of_type_blood_oath(self):
        """ (OBJECT RELATIONAL METHODS) A cult's blood oaths must each be of type `<BloodOath>`. """
        cult = create_cult()
        follower = create_follower()

        BloodOath(cult, follower)

        assert (isinstance(cult.get_blood_oaths()[0], BloodOath))

    def test_has_many_followers(self):
        """ (OBJECT RELATIONAL METHODS) A cult must be able to associate to many followers. """

        cult = create_cult()

        follower_1 = create_follower()
        follower_2 = create_follower()
        follower_3 = create_follower()

        oath_1 = BloodOath(cult, follower_1)
        oath_2 = BloodOath(cult, follower_2)

        assert (follower_1 in cult.get_followers())
        assert (follower_2 in cult.get_followers())
        assert (not follower_3 in cult.get_followers())

    def test_has_unique_followers(self):
        """ (OBJECT RELATIONAL METHODS) A cult's followers must each be unique."""

        cult = create_cult()

        follower_1 = create_follower()
        follower_2 = create_follower()

        oath_1 = BloodOath(cult, follower_1)
        oath_1 = BloodOath(cult, follower_1)
        oath_1 = BloodOath(cult, follower_2)

        assert (len(set(cult.get_followers())) == 2)

    def test_followers_of_type_follower(self):
        """ (OBJECT RELATIONAL METHODS) A cult's followers must each be of type followers"""

        cult = create_cult()
        follower = create_follower()
        oath = BloodOath(cult, follower)

        assert(isinstance(cult.get_followers()[0], Follower))

    # AGGREGATE / ASSOCIATION METHODS #

    def test_recruit_follower(self):
        """(AGGREGATE METHODS) The recruit_follower method takes a follower as an argument and associates the follower with that cult """

        cult = create_cult()
        follower = create_follower()
        
        cult.recruit_follower(follower)

        assert(cult.get_blood_oaths()[0].follower == follower)

    def test_get_cult_population(self):
        """(AGGREGATE METHODS) The get_cult_population method returns the cult population as an int """

        cult = create_cult()
        follower_1 = create_follower()
        follower_2 = create_follower()
        follower_3 = create_follower()

        BloodOath(cult, follower_1)
        BloodOath(cult, follower_2)
        BloodOath(cult, follower_3)

        assert(cult.get_cult_population() == 3)

    def test_get_average_age(self):
        """(AGGREGATE METHODS) The get_average_age method returns the average age of all cult members """

        cult = create_cult()
        follower_1 = create_follower(age=20)
        follower_2 = create_follower(age=30)
        follower_3 = create_follower(age=70)

        BloodOath(cult, follower_1)
        BloodOath(cult, follower_2)
        BloodOath(cult, follower_3)

        assert(cult.get_average_age(self) == 40.0)

    def test_get_average_age_with_no_members():
        """(AGGREGATE METHODS) The get_average_age method returns the average age of all cult members """

        cult = create_cult()

        assert(cult.get_average_age() == 0.0)

    def test_get_follower_mottos(self):
        """(AGGREGATE METHODS) The get_follower_mottos method returns a list of life_mottos for each cult member """

        cult_1 = create_cult()
        cult_2 = create_cult()
        follower_1 = create_follower(life_motto="Woo")
        follower_2 = create_follower(life_motto="Yay")
        follower_3 = create_follower(life_motto="Woot")

        BloodOath(cult_1, follower_1)
        BloodOath(cult_1, follower_2)
        BloodOath(cult_2, follower_3)

        assert(cult_1.get_follower_mottos() == ["Woo", "Yay"])
        assert(cult_2.get_follower_mottos() == ["Woot"])

    def test_find_by_name(self):
        """(AGGREGATE METHODS) The find_by_name class method returns a cult with the matching name """

        cult_1 = create_cult(name="Cult One")
        cult_2 = create_cult(name="Cult Two")

        assert(Cult.find_by_name("Cult One") == cult_1)
        assert(Cult.find_by_name("Cult Two") == cult_2)
        assert(Cult.find_by_name("Cult Zero") == None)

    def test_get_least_popular():
        """(AGGREGATE METHODS) The get_least_popular class method returns a cult with the fewest number of followers """

        cult_1 = create_cult(name="Cult One")
        cult_2 = create_cult(name="Cult Two")

        follower_1 = create_follower()
        follower_2 = create_follower()
        follower_3 = create_follower()
        
        BloodOath(cult_1, follower_1)
        BloodOath(cult_1, follower_2)
        BloodOath(cult_2, follower_3)

        assert(Cult.get_least_popular() == cult_2)

        cult_3 = create_cult(name="Cult Three")

        assert(Cult.get_least_popular() == cult_3)
        
    def test_find_follower_by_name():
        """(AGGREGATE METHODS) The find_follower_by_name method returns any followers in the cult with that specific name """

        cult = create_cult()

        follower_1 = create_follower(name="John")
        follower_2 = create_follower(name="Jim")
        follower_3 = create_follower(name="Bob")
        follower_4 = create_follower(name="John")
        
        BloodOath(cult, follower_1)
        BloodOath(cult, follower_2)
        BloodOath(cult, follower_3)
        BloodOath(cult, follower_4)

        assert(cult.find_follower_by_name("Jim") == [follower_2])
        assert(cult.find_follower_by_name("John") == [follower_1, follower_4])