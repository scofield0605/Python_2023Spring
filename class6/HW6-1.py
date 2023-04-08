class lession:
#建構式
    def _init_(self, time, name):
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
emma = lession.Math ()
ben = lession.english()
emma. introduce ()
ben.introduce ()