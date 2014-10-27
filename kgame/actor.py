from kivy.uix.widget import Widget
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.core.window import Window
from kivy.atlas import Atlas
from kivy.clock import Clock
import ast

class Actor(Widget):
    states = {}
    state = 'init'
    rect = None
    frame = 0
    def __init__(self,**args):
        super(Actor,self).__init__(**args)
        print self.size
        if 'states' in args:
            self.states = args['states']
        elif 'file' in args:
            with open(args['file'],'r') as f:
                fc = f.read()
                self.states = ast.literal_eval(fc)
        if self.states is not None and 'init' in self.states:
            self.switch('init')
            
    def get_texture(self):
        result = None
        if atlas is not None and len(self.states)>0 and self.state in self.states:
            thing = self.states[self.state]
            if isinstance(thing,str):
                if thing in atlas.textures:
                    result= atlas.textures[thing]
            elif isinstance(thing,dict):
                key = thing['frames']
                delay = thing['delay']
                if key[self.frame] in atlas.textures:
                    result= atlas.textures[key[self.frame]]
                self.frame += 1
                if self.frame >= len(key):
                    self.frame = 0
                Clock.schedule_once(self.apply_state,delay)

        return result


    def switch(self,state):
        self.state = state
        self.frame = 0
        self.apply_state()
        
    def apply_state(self,dt=0):
        if self.rect is None:
            self.rect = Rectangle(texture=self.get_texture(),size=self.size,pos=self.pos)
            self.canvas.add(self.rect)
        else:
            self.rect.size = self.size
            self.rect.pos = self.pos
            self.rect.texture = self.get_texture()
