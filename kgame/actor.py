from kivy.uix.widget import Widget
from kivy.graphics.context_instructions import Color

class Actor(Widget):

    def __init__(self,scene,**args):
        super(Actor,self).__init__(**args)
        self.scene= scene
        self.child_map = {}
        self.touched = False
        self.init_properties(**args)
        self.update_size_pos()

    def init_properties(self,**args):
        self.init_property('design_size',(0,0),**args)
        self.init_property('design_pos',(0,0),**args)
        self.init_property('design_touch',False,**args)

    def init_property(self,name,default,**args):
        if name in args:
            setattr(self,name,args[name])
        else:
            setattr(self,name,default)
    
    
    def update_size_pos(self):
        if self.scene is not None:
            self.scene.update_dimension(self)

    def resize(self,size):
        self.design_size = size
        self.update_size_pos()

    def move(self,pos):
        self.design_pos = pos
        self.update_size_pos()

    
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
        

