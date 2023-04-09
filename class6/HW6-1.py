class lesson:
#建構式
    def __init__(self, time, name):
        self.time = time
        self.name=name
    @classmethod
    def Math (cls):
        return cls ('Monday','Emma')

    @classmethod
    def english (cls):
        return cls ("Thruday", "Peter") 
    def introduce (self):
        print("the lession is taught by {} on {}.".format (self.name, self.time))
emma = lesson.Math ()
ben = lesson.english()
emma.introduce()
ben.introduce()