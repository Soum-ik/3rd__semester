def genertor():
    yield 'P'
    yield 'Y'
    yield 'T'
    yield 'H'
    yield 'O'
    yield 'N'

result = genertor();

for k in result:
    print(k);
