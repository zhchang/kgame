from __future__ import division
from kivy.uix.widget import Widget
from kivy.core.window import Window
from util import import_it
from actor import Actor

class Scene(Actor):
    def __init__(self,game,**args):
        self.game = game
        super(Scene,self).__init__(None,**args)
        self.init_configs()
        self.load()

    def init_properties(self,**args):
        super(Scene,self).init_properties(**args)
        self.init_property('fill_mode','stretch',**args)
        self.init_property('design_dimension',(1080,1920),**args)
        ratio_x = Window.size[0] / self.design_dimension[0]
        ratio_y = Window.size[1] / self.design_dimension[1]
        self.size = Window.size 
        self.pos = (0,0)
        if self.fill_mode == 'fit_width':
            print 'fitting width'
            self.size = (Window.size[0],self.design_dimension[1] * ratio_x)
            self.pos = (0,(Window.size[1] - self.size[1]) / 2)
        elif self.fill_mode == 'fit_height':
            print 'fitting height'
            self.size= (self.design_dimension[0] * ratio_y,Window.size[1])
            self.pos = ((Window.size[0] - self.size[0]) / 2,0)
        self.x,self.y = self.pos
        self.width,self.height = self.size
        print self.size


    def update_size_pos(self):
        pass

    def update_dimension(self,actor):
        
        ratio_x = self.size[0] / self.design_dimension[0]
        ratio_y = self.size[1] / self.design_dimension[1]
        print Window.size
        print self.size
        print self.design_dimension
        print (ratio_x,ratio_y)
        actor.pos = (self.x+actor.design_pos[0] * ratio_x, self.y+actor.design_pos[1] * ratio_y)
        actor.size= (actor.design_size[0] * ratio_x, actor.design_size[1] * ratio_y)
        actor.x,actor.y = actor.pos
        actor.width,actor.height= actor.size
        
    
    def init_configs(self):
        self.handle_touch = False
        self.actor_configs = []
        self.triggers = {} 
        self.actors = []
        self.atlas = None
    
    def load(self):
        self.load_actors()
        self.load_triggers()
    
    def load_actors(self):
        for actor_config in self.actor_configs:
            self.load_actor(actor_config)

    
    def load_actor(self,actor_config):
        actor_class = Actor
        if 'class' in actor_config and len(actor_config['class']) > 0:
            actor_class = import_it(actor_config['class'])
        thing = actor_class(self,**actor_config)
        self.add_widget(thing)


    def trigger_event(self,event):
        pass



