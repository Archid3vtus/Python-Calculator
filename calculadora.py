import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
class calculadora(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_border_width(10)
        self.set_default_size(300,300)
        self.set_resizable(False)

        header = Gtk.HeaderBar(title='Calculadora', show_close_button=True)
        self.set_titlebar(header)

        self.grid = Gtk.Grid(column_spacing=5,row_spacing=5, column_homogeneous=True, row_homogeneous=True)
        self.add(self.grid) 

        self.add_text_view()
        self.clear = False

        self.add_buttons()

   
    def add_text_view(self):
        scrolled_window = Gtk.ScrolledWindow()
        self.grid.attach(scrolled_window, 0, 0, 3, 1)

        self.text = Gtk.TextView(editable=False)
        scrolled_window.add(self.text)

    def add_buttons(self):
        chars = ['0','.','=','+','1','2','3','-','4','5','6','*','7','8','9','/']
        buttons = []
        a = 5

        for x in range(len(chars)):
            if x % 4 == 0:
                a -= 1
            buttons.append(Gtk.Button(label=chars[x]))
            self.grid.attach(buttons[x], x%4, a, 1, 1)
        
        buttons.append(Gtk.Button(label='c'))
        self.grid.attach(buttons[16], 3, 0, 1, 1)

        for button in buttons:
            button.connect('clicked', self.button_clicked)

    def button_clicked(self,widget):
        buffer = self.text.get_buffer()
        if widget.get_label() == '=':
            teste = eval(buffer.get_text(buffer.get_start_iter(),buffer.get_end_iter(), True))
            buffer.set_text(str(teste))
            self.clear = True
        elif widget.get_label() == 'c':
            buffer.set_text('')
        else:
            if self.clear and widget.get_label() in ['0','1','2','3','4','5','6','7','8','9']:
                buffer.set_text('')
            buffer.set_text(buffer.get_text(buffer.get_start_iter(),buffer.get_end_iter(), True) + widget.get_label())
            self.clear = False

window = calculadora()
window.connect('destroy', Gtk.main_quit)
window.show_all()
Gtk.main()