print("Hello World")

def test_func(apple):
    for i in range(3):
        apple()

def apple_eater():
    print("I want to eat apple!")

print(test_func(apple_eater))