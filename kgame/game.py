from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
import ast
from kivy.atlas import Atlas
from actor import Actor
from scene import Scene
from util import import_it



class GameApp(App):
    current_scene = None
    game = None

    def __init__(self,game_file):
        super(GameApp,self).__init__()
        print 'starting game: %s'%(game_file)
        self.game = import_it(game_file) 
    def build(self):
        config = self.game.scenes[0]
        self.current_scene = import_it(config['class'])(self,**config)
        return self.current_scene

