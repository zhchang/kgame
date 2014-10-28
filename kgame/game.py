from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
import ast
from kivy.atlas import Atlas
from actor import Actor



class GameScreen(Actor):
    def __init__(self,**kwargs):
        super(GameScreen,self).__init__(None,**kwargs)
        self.size = Window.size
        self.handle_touch = False


class GameApp(App):
    screen = None
    game = None

    def __init__(self,game_file):
        super(GameApp,self).__init__()
        print 'starting game: %s'%(game_file)
        self.game = self.import_it(game_file) 
        self.screen = GameScreen()
    def build(self):
        self.load_game()
        return self.screen

    def load_game(self):
        self.load_scene(self.import_it(self.game.scenes[0]))

    def load_scene(self,scene):
        print scene
        for actor in scene.actors:
            self.load_actor(actor,scene)

    def load_actor(self,actor,scene):
        actor_class = Actor
        if 'class' in actor and len(actor['class']) > 0:
            actor_class = self.import_it(actor['class'])
        thing = actor_class(scene.atlas,**actor)
        self.screen.add_widget(thing)

    def import_it(self,name):
        mods = name.split('.')
        clz = None
        try:
            print 'importing %s'%(name)
            result = __import__(name)
            print 'import success %s'%(result)
        except:
            thing = '.'.join(mods[:-1])
            result = __import__(thing)
            clz = mods[-1]
            mods = mods[:-1]
        for mod in mods[1:]:
            result= getattr(result,mod)
        if clz is not None:
            result = getattr(result,clz)
        return result

