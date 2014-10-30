from kivy.uix.widget import Widget
from kivy.core.window import Window
from util import import_it
from actor import Actor

class Scene(Actor):
    def __init__(self,game,**args):
        super(Scene,self).__init__(None,**args)
        self.game = game
        print self.init_configs
        self.init_configs()
        self.load()
        
    
    def init_configs(self):
        self.handle_touch = False
        self.actor_configs = []
        self.actors = []
        self.size = Window.size
        self.atlas = None
    
    def load(self):
        for actor_config in self.actor_configs:
            self.load_actor(actor_config)
    
    def load_actor(self,actor_config):
        actor_class = Actor
        if 'class' in actor_config and len(actor_config['class']) > 0:
            actor_class = import_it(actor_config['class'])
        thing = actor_class(self,**actor_config)
        self.add_widget(thing)




