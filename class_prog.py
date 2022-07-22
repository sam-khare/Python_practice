class Human:
    def __init__(self,name,occupation):
        self.name = name
        self.occupation =occupation

    def do_work(self):
        if self.occupation == 'tennis player':
            print(self.name,"plays tennis")
        elif self.occupation == 'actor':
            print(self.name,"shoots film")

    def speaks(self):
        print(self.name,",says How are you")
tom = Human('Tom Cruise','actor')
tom.do_work()
tom.speaks()