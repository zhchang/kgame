from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
import ast
from ball_actor import BallActor 
#import ball_actor



class GameScreen(Widget):
    def __init__(self,**kwargs):
        super(GameScreen,self).__init__(**kwargs)
        self.size = Window.size
        self.add_widget(ball_actor.BallActor(size=(128,128),file='balls.actor',pos=(100,100)))



class GameApp(App):
    screen = None
    def __init__(self):
        super(GameApp,self).__init__()
        self.screen = GameScreen()
    def build(self):
        return self.screen

if __name__ == '__main__':
    GameApp().run()
