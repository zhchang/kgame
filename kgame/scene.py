from __future__ import division
from kivy.uix.widget import Widget
from kivy.core.window import Window
from util import import_it
from actor import Actor

class Scene(Actor):
    def __init__(self,game,**args):
        self.design_dimension = (1080,1920)
        self.game = game
        super(Scene,self).__init__(None,**args)
        self.init_configs()
        self.load()

    def update_size_pos(self):
        self.update_dimension(self)

    def update_dimension(self,actor):
        ratio_x = Window.size[0] / self.design_dimension[0]
        ratio_y = Window.size[1] / self.design_dimension[1]
        actor.pos = (actor.design_pos[0] * ratio_x, actor.design_pos[1] * ratio_y)
        actor.size= (actor.design_size[0] * ratio_x, actor.design_size[1] * ratio_y)
        actor.x = actor.pos[0]
        actor.y = actor.pos[1]
        actor.width = actor.size[0]
        actor.height = actor.size[1]
        
    
    def init_configs(self):
        self.handle_touch = False
        self.actor_configs = []
        self.triggers = {} 
        self.actors = []
        self.size = Window.size
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



