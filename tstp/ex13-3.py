

def TrueOrNot(obj1, obj2):
    print(obj1 is obj2)


class SomeObject:
    pass

class SomeOthObject:
    pass

object1 = SomeObject()
object2 = object1
object3 = SomeObject()

TrueOrNot(object1, object2)
TrueOrNot(object1, object3)
TrueOrNot("a", "b")
