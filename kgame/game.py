from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
import ast
from kivy.atlas import Atlas
from actor import Actor
from importlib import import_module



class GameScreen(Widget):
    def __init__(self,**kwargs):
        super(GameScreen,self).__init__(**kwargs)
        self.size = Window.size


class GameApp(App):
    screen = None
    game = None

    def __init__(self,game_file):
        super(GameApp,self).__init__()
        print 'starting game: %s'%(game_file)
        self.game = import_module(game_file) 
        self.screen = GameScreen()
    def build(self):
        self.load_game()
        return self.screen

    def load_game(self):
        self.load_scene(import_module(self.game.scenes[0]))

    def load_scene(self,scene):
        print scene
        for actor in scene.actors:
            self.load_actor(actor,scene)

    def load_actor(self,actor,scene):
        actor_class = Actor
        if 'def' in actor:
            actor['states'] = import_module(actor['def']).states
        if 'class' in actor and len(actor['class']) > 0:
            actor_class = import_module(actor['class'])
        thing = actor_class(scene.atlas,**actor)
        self.screen.add_widget(thing)

