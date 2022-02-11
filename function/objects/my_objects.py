class Ball:
    pass

def Learn_dynamic_creation():
    ball = Ball()
    ball.color = 'red'
    ball.radius = 10
    print(ball.color, ball.radius, ball.__dict__)


def learn_inheritance():
    class MyInt(int):
        tag = 'my tag'


pure_number = int(5)
my_number = MyInt(5)

    print(
        'Pure number:', getattr(pure_number, 'tag', 'Has no tag')

    )

    print(
        'My number:', getattr(my_number, 'tag', 'Has no tag')

    )  
    my_number.tag = ...



print(issubclass(Ball, object))


