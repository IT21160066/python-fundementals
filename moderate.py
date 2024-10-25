# lists
from operator import index

books = ['Abc', 'Hh', 'cb']
print(books)
books.append('Jj')
print(books)
books.extend(['tt', 'yy'])
print(books)
books.insert(2, 'test')
print(books)
# books[1:2] = ['test2', 'test3', 'test4']
# print(books)

books.sort(key=str.lower)
print(books)

# tuples - once tuple is created it cannot be modified
# cannot even  add or remove items

names = ('kamal', 'john')
print(names[0])
print(len(names))
print(names.index('kamal'))

names_copy = names + ('peter', 'bob')
print(names_copy)

# dictionaries - allows to create key value pairs
# can modify

dog = {'name': 'dog', 'age': 8, 'color': 'green'}
print('test >>>', list(dog.items()))
print(dog['name'])
print(dog.get('color', 'brown'))
print(dog.pop('color'))
print(dog)
print(dog.popitem())
print(dog)
print('color' in dog)
print(dog.keys())
print(list(dog.keys()))
print(list(dog.values()))
print(len(dog))

dog['height'] = 'tall'
print(dog)
del dog['height']
print(dog)
dog_copy = dog.copy()
print(dog_copy)

# loops

condition = True
while condition:
    print('The condition true')
    condition = False

count = 0
while count < 5:
    print(count)
    count = count  + 1

items = [1,2, 3, 4, 5]
for index, item in enumerate(items):
    print('index >>', index, 'item >>', item)

items = [1,2, 3, 4, 5]
for item in items:
    if item == 2:
        continue
    print(item)

# functions

def hello(name='amal', age=8):
    print('hello', name, 'age', age)
hello()

def change(val):
    val['name'] = 'jj'
    print(val['name'])

value = {'name': 'bb'}
change(value)

print(value)

def sample(name):
    print(name)
    return name, 8, 'hhh'

print('returned value >>', sample('john'))

# variable scope

age = 8

def test():
    name = 'aa'
    print(age, name)
test()

print(age)

# nested functions

def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(' ')
    for word in words:
        say(word)

talk('hello hi')


def count():
    count = 0

    def increment():
        nonlocal count
        count += 1
        print(count)
    increment()

count()






