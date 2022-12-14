import kivy
import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image

GridSize = 6
NumImage = 6
MaxVisible = 2
rtime = 2

Selected = []
ids = []
temp2 = []
temp = []

#idlength = (GridSize**2)/2
idlength = 18

def handle_click(instance):
    if len(Selected) < MaxVisible:
        instance.parent.check_if_found()

def images_id(idlength):
    while len(ids) < idlength:
        num  = random.randint(1,6)
        ids.append(num)
    
    for x in ids:
        temp.append(x)

    while len(temp) > 0:
        randomnum = random.randint(0,(len(temp)-1))
        ids.append(temp[randomnum])
        temp.remove(temp[randomnum])



class cell(BoxLayout):
    
    def __init__(self, id, time):
        super().__init__()
        self.id = id
        self.rtime = time
        self.isperminant = False
        Image_Location = "assets/elephants {0}.png".format(id)
        self.Image_View = Image(source = Image_Location)
        self.Button_View = Button()
        self.Button_View.bind(on_press=handle_click)
        self.add_widget(self.Button_View)

    def reveal_image(self):
        self.remove_widget(self.Button_View)
        self.add_widget(self.Image_View)
        Selected.append(self)
        Clock.schedule_once(self.hide_image, self.rtime)


    def hide_image(self, delta):
        if self.isperminant == False:
            self.remove_widget(self.Image_View)
            self.add_widget(self.Button_View)
            Selected.remove(self)

    def check_if_found(self):
        revealed = False
        if len(Selected) == 0:
            self.reveal_image()
        else:
            for x in range(len(Selected)):
                if self.id == Selected[x].id:
                    self.reveal_forever()
                    Selected[x].isperminant = True
                    Selected.remove(Selected[x])
                    revealed = True
            if revealed == False:
                self.reveal_image()
            else:
                revealed = False
                

    def reveal_forever(self):
        self.remove_widget(self.Button_View)
        self.add_widget(self.Image_View)
        self.isperminant = True


class application(App):

    def build(self):
        layout = GridLayout(cols = GridSize)
        for row in range(GridSize):
            for collumn in range(GridSize):
                tempnum = row*GridSize + collumn
                layout.add_widget(cell(ids[tempnum], rtime))
        return layout


if __name__ == "__main__":
    images_id(idlength)
    app = application()
    app.run()






