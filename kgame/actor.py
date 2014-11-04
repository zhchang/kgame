from kivy.uix.widget import Widget
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.core.window import Window
from kivy.atlas import Atlas
from kivy.clock import Clock

class Actor(Widget):

    def __init__(self,scene,**args):
        super(Actor,self).__init__(**args)
        self.states = {}
        self.rect = None
        self.frame = 0
        self.touched = False
        self.scene= scene
        self.child_map = {}
        self.handle_touch = False
        self.clock = None
        self.design_size = (0,0)
        self.design_pos= (0,0)
        if 'design_size' in args:
            self.design_size = args['design_size']
        if 'design_pos' in args:
            self.design_pos= args['design_pos']
        if 'states' in args:
            self.states = args['states']
        if 'handle_touch' in args:
            self.handle_touch = args['handle_touch']
        if self.states is not None and 'init' in self.states:
            self.switch('init')
        self.update_size_pos()
            
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
    
    def update_size_pos(self):
        if self.scene is not None:
            self.scene.update_dimension(self)

    def resize(self,size):
        self.design_size = size
        self.update_size_pos()

    def move(self,pos):
        self.design_pos = pos
        self.update_size_pos()

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

    def on_touch_down(self,touch):
        result = super(Actor,self).on_touch_down(touch)
        if self.handle_touch and not result and self.collide_point(touch.x,touch.y):
            self.touched = True
            return True 
        return False 

    def on_touch_move(self,touch):
        super(Actor,self).on_touch_move(touch)

    def on_touch_up(self,touch):
        result = super(Actor,self).on_touch_up(touch)
        if not result and self.touched and self.collide_point(touch.x,touch.y):
            self.on_click()
        self.touched = False
            
    def on_click(self):
        self.scene.trigger_event(('on_click',self.id))
    
    def add_widget(self,widget):
        super(Actor,self).add_widget(widget)
        if widget.id is not None:
            self.child_map[widget.id] = widget
        

