class rectangle:
    def __init__(self,width,length):
        self.width = width
        self.length = length
    #fartobi.
    def area(self):
        return self.width * self.length
    #perimetri.
    def perimeter(self):
        return (self.width + self.length) * 2
    #moncemebi.
    def print_out(self,area,perimeter):
        self.area = area
        self.perimeter = perimeter
        return f' width : {self.width}.\n length : {self.length}.\n area : {area}.\n perimeter : {perimeter}.'
result = rectangle(4, 5)
print(result.print_out(result.area(),result.perimeter()))
