Mock Code Challenge - Blood Oath
==============

In this project, we will be practicing object relationships in Python, with a particular emphasis on the `has many` `through` relationship (aka: many-to-many). Please read the whole README before writing any code!

## Introduction

You've been approached by your local cult leaders to build out a foundation for a new app they are all using to gather recruits. As the open-minded freelancers that you are, you've agreed to do so!

## Setup

`pipenv install` will make sure we have ipdb included in our environment.  
`pipenv shell` allows us access to that environment.  

## Code Overview

You can now view all of your Python files for your models in the `lib` folder. They will be automagically available for you so long as you use the `python -i index.py` file to test your code.

Through this file, we've provided to you a console that you can use to test your code. To enter a console session, run `python -i index.py` from the command line. You'll be able to test out the functionality that you write there. Take a look at that file to see how you can pre-define variables and create object instances, rather than manually doing it in every single console session.

If you would prefer to use `ipdb` then uncomment the last line in `index.py` and run `python index.py` instead.




## Deliverables

### Domain Modeling

First step is to model the domain you are building out. As a non-discriminatory cult recruitment platform, `Cult`s will have many `Follower`s while `Follower`s will be allowed to join many `Cult`s. How do they keep track of this? `BloodOath`s of course! You cannot join a `Cult` without making a `BloodOath`.

* What are your models?
* What does your schema look like?
* What are the relationships between your models?

---

### Basic Class Attributes, Properties, and Methods

With your domain modeled, you now need to build out some basic functionality so both `Cult`s and `Follower`s can use your platform to make `BloodOath`s. A social network of cults if you will. So general searching type functionality.

Questions you should ask yourself:

* Do I need any other attributes?
* Should I write any other methods?
* Am I following _Single Source of Truth_?

## Initializers and Properties

### `Cult`

```python
def __init__(name, location, founding_year, slogan)
```
- cult should be initialized with a name, location, founding_year, and slogan

```python
@property
def name(self)

@name.setter
def name(name)
```
- returns the cult's name
- name must be of type `str`
- name must be between 1 and 20 characters long
- `raise Exception` if the setter fails

```python
@property
def founding_year()

@founding_year.setter
def founding_year(new_founding_year)
```
- returns the cult's founding year
- founding year must be of type `int`
- founding year cannot be beyond the current year
- founding year cannot be changed once set
- *Hint: `hasattr`*
- `raise Exception` if the setter fails

### `Follower`

```python
def __init__(name, age, life_motto)
```
- cult should be initialized with a name, age, and life_motto

```python
@property
def age()

@age.setter
def age(new_age)
```
- returns the follower's age
- age should be of type `int`
- age should be between 0 and 120 inclusive
- `raise Exception` if the setter fails

### `BloodOath`

```python
def __init__(cult, follower)
```
- BloodOath should be initialized with a cult and follower

```python
@property
def cult(self)

@cult.setter
def cult(new_cult)
```
- returns the cult for this blood oath
- the cult should be of type `Cult`
- should not be able to change the cult once set (hint: *hasattr*)
- `raise Exception` if the setter fails

```python
@property
def follower()

@follower.setter
def follower(follower)
```
- returns the follower for this blood oath
- the follower should be of type `Follower`
- should not be able to change the follower once set (hint: *hasattr*)
- `raise Exception` if the setter fails

```python
BloodOath.all_oaths
```
- returns a `list` of all the blood oaths

## Object Relationship Methods

### `Cult`

```python
def get_blood_oaths()
```
- returns a `list` of blood oaths for that cult
- blood oaths are of type `BloodOath`

```python
def get_followers()
```
- returns a `list` of **unique** followers for that cult
- followers are of type `Follower`

### `Follower`

```python
def get_blood_oaths()
```
- returns a `list` of blood oaths for that follower
- blood oaths are of type `BloodOath`

```python
def get_cults()
```
- returns a `list` of **unique** cults for that follower
- cults are of type `Cult`

## Aggregate and Association Methods

### `Cult`

```python
def recruit_follower(follower)
```
- Takes an argument of a `Follower` instance and associates that follower with the cult
- *Hint: What connects a follower to a cult?*

```python
def get_cult_population()
```
- returns an `int` that is the number of followers in this cult

```python
def get_average_age()
```
- returns a `float` that is the average age of this cult's followers
- returns `0.0` if there are no followers

```python
def get_follower_mottos()
```
- returns a `list` of mottos for each of this cult's followers

```python
@classmethod
def find_by_name(cls, name)
```
- takes a `str` argument that is a name and returns a `Cult` instance whose name matches that argument
- return `None` if no cult is found with that name

```python
@classmethod
def get_least_popular(cls)
```
- returns the `Cult` instance that has the least number of followers

```python
def find_followers_by_name(name)
```
- takes a `str` argument that is a name and returns a `list` of followers who have that name in the cult

### `Follower`

```python
def get_number_of_oaths()
```
- returns an `int` for the number of blood oaths that follower has taken
- returns `0` if that follower has taken no oaths

```python
def get_oldest_cult()
```
- returns the cult with the earliest starting year for that follower
- returns `None` if that follower isn't part of any cult