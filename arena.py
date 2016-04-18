class Arena(object):
    def __init__(self, const):
        self.change_const = const
        print self.change_const

obj_arena = Arena(5)
obj_arena.change_const = 42
print obj_arena.change_const



