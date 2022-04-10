# `collections`

## Contar ocorrencias como value_counts de pandas

from collections import Counter

char_list = ["a", "b", "c", "a", "d", "b", "b"]

print(Counter(char_list))
# Counter({'a': 2, 'b': 3, 'c': 1, 'd': 1})


## namedtuple = classe simlpes

se você precisa agrupar dados como numa classe, ao invez de obj ou criar uma clase, voce pode usar namedtuples para isso

from collections import namedtuple

Person = namedtuple("Person", "name gender")

oliver = Person("Oliver", "male")
khuyen = Person("Khuyen", "female")
print(oliver)
# Person(name='Oliver', gender='male')
print(khuyen)
# Person(name='Khuyen', gender='female')

## defaultdict = dicionario pytohn com valor default

Se chamar por uma key que nao está presente, retorna um valor default

from collections import defaultdict

classes = defaultdict(lambda: "Outside")
classes["Math"] = "B23"
classes["Physics"] = "D24"
print(classes["Math"])
# 'B23'
print(classes["English"])
# 'Outside' # valor default, se for dict comun, daria erro
