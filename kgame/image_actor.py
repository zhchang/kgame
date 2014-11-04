from actor import Actor
from kivy.clock import Clock
from kivy.graphics.vertex_instructions import Rectangle
from kivy.atlas import Atlas

class ImageActor(Actor):
    def __init__(self,scene,**args):
        super(ImageActor,self).__init__(scene,**args)

    def init_properties(self,**args):
        super(ImageActor,self).init_properties(**args)
        self.states = {}
        self.rect = None
        self.frame = 0
        self.clock = None
        if 'states' in args:
            self.states = args['states']
        if self.states is not None and 'init' in self.states:
            self.switch('init')

    def get_texture(self):
        result = None
        if self.scene.atlas is not None and len(self.states)>0 and self.state in self.states:
            thing = self.states[self.state]
            if isinstance(thing,str):
                if thing in self.scene.atlas.textures:
                    result= self.scene.atlas.textures[thing]
            elif isinstance(thing,dict):
                key = thing['frames']
                delay = thing['delay']
                if key[self.frame] in self.scene.atlas.textures:
                    result= self.scene.atlas.textures[key[self.frame]]
                self.frame += 1
                if self.frame >= len(key):
                    self.frame = 0
                self.clock = Clock.schedule_once(self.apply_state,delay)

        return result

    def switch(self,state):
        Clock.unschedule(self.apply_state)
        self.state = state
        self.frame = 0
        self.apply_state()
        
    def apply_state(self,dt=0):
        self.clock = None
        if self.rect is None:
            self.rect = Rectangle(texture=self.get_texture(),size=self.size,pos=self.pos)
            self.canvas.add(self.rect)
        else:
            self.rect.size = self.size
            self.rect.pos = self.pos
            self.rect.texture = self.get_texture()

