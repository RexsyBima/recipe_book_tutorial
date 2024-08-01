from src.hello import x
from src import hello
print(x)
print(hello.x)

from src.utils import read_json

datas = read_json('usernames.json')
print(datas)