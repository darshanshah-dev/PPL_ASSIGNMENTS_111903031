import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Calculator(Gtk.Window) :
    def __init__(self) :
        Gtk.Window.__init__(self, title = "Calculator")

        hd = Gtk.HeaderBar()
        hd.set_show_close_button(True)
        hd.props.title = "Calculator"
        self.set_titlebar(hd)

        grid = Gtk.Grid()
        self.add(grid)
        self.expression = Gtk.Entry()
        self.expression.set_editable(False)

        grid.attach(self.expression, 0, 0, 10, 1)
        
        self.result = Gtk.Entry()
        self.result.set_editable(False)

        grid.attach_next_to(self.result, self.expression, Gtk.PositionType.BOTTOM, 10, 1)
        
        mod = Gtk.Button(label = "%")
        mod.connect("clicked", self.onModClicked)
        grid.attach_next_to(mod, self.result, Gtk.PositionType.BOTTOM, 1, 1)
        
        clearE = Gtk.Button(label = "CE")
        clearE.connect("clicked", self.onCEClicked)
        grid.attach_next_to(clearE , mod, Gtk.PositionType.RIGHT,1 , 1)

        clear = Gtk.Button(label = "C")
        clear.connect("clicked", self.onClearClicked)
        grid.attach_next_to(clear , clearE, Gtk.PositionType.RIGHT,1 , 1)

        delete = Gtk.Button(label = "<<=")
        delete.connect("clicked", self.onDeleteClicked)
        grid.attach_next_to(delete, clear, Gtk.PositionType.RIGHT, 1, 1)

        inverse = Gtk.Button(label = "1/x")
        inverse.connect("clicked", self.onInverseClicked)
        grid.attach_next_to(inverse, mod, Gtk.PositionType.BOTTOM, 1, 1)

        power = Gtk.Button(label = "x ^ n")
        power.connect("clicked", self.onPowerClicked)
        grid.attach_next_to(power, inverse, Gtk.PositionType.RIGHT, 1, 1)

        root = Gtk.Button(label = "x ^ 0.5")
        root.connect("clicked", self.onRootClicked)
        grid.attach_next_to(root, power, Gtk.PositionType.RIGHT, 1, 1)

        divide = Gtk.Button(label = "/")
        divide.connect("clicked", self.onDivideClicked)
        grid.attach_next_to(divide, root, Gtk.PositionType.RIGHT, 1 , 1)

        multiply = Gtk.Button(label = "*")
        multiply.connect("clicked", self.onMultiplyClicked)
        grid.attach_next_to(multiply, divide, Gtk.PositionType.BOTTOM, 1, 1)

        subtract = Gtk.Button(label = "-")
        subtract.connect("clicked", self.onSubtractClicked)
        grid.attach_next_to(subtract, multiply, Gtk.PositionType.BOTTOM, 1, 1)

        add = Gtk.Button(label = "+")
        add.connect("clicked", self.onAddClicked)
        grid.attach_next_to(add, subtract, Gtk.PositionType.BOTTOM, 1, 1)

        

        one = Gtk.Button(label = "1")
        one.connect("clicked", self.onOneClicked)
        grid.attach_next_to(one, mod, Gtk.PositionType.BOTTOM, 1, 1)

        two = Gtk.Button(label = "2")
        two.connect("clicked", self.onTwoClicked)
        grid.attach_next_to(two, one, Gtk.PositionType.RIGHT, 1, 1)

        three = Gtk.Button(label = "3")
        three.connect("clicked", self.onThreeClicked)
        grid.attach_next_to(three, two, Gtk.PositionType.RIGHT, 1, 1)

        four = Gtk.Button(label = "4")
        four.connect("clicked", self.onFourClicked)
        grid.attach_next_to(four, one, Gtk.PositionType.BOTTOM, 1, 1)

        five = Gtk.Button(label = "5")
        five.connect("clicked", self.onFiveClicked)
        grid.attach_next_to(five, four, Gtk.PositionType.RIGHT, 1, 1)

        six = Gtk.Button(label = "6")
        six.connect("clicked", self.onSixClicked)
        grid.attach_next_to(six, five, Gtk.PositionType.RIGHT, 1, 1)

        seven = Gtk.Button(label = "7")
        seven.connect("clicked", self.onSevenClicked)
        grid.attach_next_to(seven, four, Gtk.PositionType.BOTTOM, 1, 1)

        eight = Gtk.Button(label = "8")
        eight.connect("clicked", self.onEightClicked)
        grid.attach_next_to(eight, seven, Gtk.PositionType.RIGHT, 1, 1)

        nine = Gtk.Button(label = "9")
        nine.connect("clicked", self.onNineClicked)
        grid.attach_next_to(nine, eight, Gtk.PositionType.RIGHT, 1 , 1)

        decimal = Gtk.Button(label = ".")
        decimal.connect("clicked", self.onDecimalClicked)
        grid.attach_next_to(decimal, nine, Gtk.PositionType.BOTTOM, 1, 1)

        zero = Gtk.Button(label = "0")
        zero.connect("clicked", self.onZeroClicked)
        grid.attach_next_to(zero, decimal, Gtk.PositionType.LEFT, 1, 1)

        answer = Gtk.Button(label = "=")
        answer.connect("clicked", self.onAnswerClicked)
        grid.attach_next_to(answer, zero, Gtk.PositionType.BOTTOM, 2, 2)

        plusMinus = Gtk.Button(label = "+/-")
        plusMinus.connect("clicked", self.onPlusMinusClicked)
        grid.attach_next_to(plusMinus, zero, Gtk.PositionType.LEFT, 1, 1)
    
    def onZeroClicked(self, widget):
        self.setExpression("0")
        return

    def onOneClicked(self, widget):
        self.setExpression("1")
        return

    def onTwoClicked(self, widget):
        self.setExpression("2")
        return

    def onThreeClicked(self, widget):
        self.setExpression("3")
        return

    def onFourClicked(self, widget):
        self.setExpression("4")
        return

    def onFiveClicked(self, widget):
        self.setExpression("5")
        return

    def onSixClicked(self, widget):
        self.setExpression("6")
        return

    def onSevenClicked(self, widget):
        self.setExpression("7")
        return

    def onEightClicked(self, widget):
        self.setExpression("8")
        return 

    def onNineClicked(self, widget):
        self.setExpression("9")
        return

    def onDecimalClicked(self, widget):
        self.setExpression(".")
        return

    def onPowerClicked(self, widget):
        self.setExpression(" ** ")
        return

    def onModClicked(self, widget):
        self.setExpression(" % ")
        return

    def onInverseClicked(self, widget):
        self.setExpression("1 / ")
        return

    def onRootClicked(self, widget):
        self.setExpression(" ** 0.5 ")
        return

    def onDivideClicked(self, widget):
        self.setExpression(" / ")
        return

    def onMultiplyClicked(self, widget):
        self.setExpression(" * ")
        return

    def onSubtractClicked(self, widget):
        self.setExpression(" - ")
        return

    def onAddClicked(self, widget):
        self.setExpression(" + ")
        return

    def onClearClicked(self, widget):
        self.expression.set_text("")
        self.result.set_text("")
        return
    
    def onCEClicked(self, widget):
        string = self.expression.get_text()
        for i in range(len(string)) :
            if( string[i] == '+' or string[i] == '-' or string[i] == '*' or string[i] == '/') :
                break
        self.expression.set_text(string[:len(string) - i - 1])
        return
    
    def onDeleteClicked(self, widget):
        string = self.expression.get_text()
        self.expression.set_text(string[:len(string) - 1])
        return
    
    def setExpression(self, character):
        string = self.expression.get_text() + character
        self.expression.set_text(string)
        return

    def onAnswerClicked(self, widget):
        try:
            self.result.set_text(str(eval(self.expression.get_text())))
            string = self.result.get_text()
            self.expression.set_text(string)
        except:
            self.result.set_text("Invalid Input")
        return

    def onPlusMinusClicked(self, widget):
        try :
            num = float(self.result.get_text())
            num = -num
            self.expression.set_text(str(num))
        except : 
            pass
        return
    
window = Calculator()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()