import os
from kivy.atlas import Atlas
from kgame.scene import Scene

class BallsScene(Scene):
    def init_configs(self):
        super(BallsScene,self).init_configs()
        self.atlas = Atlas(os.path.join(os.path.dirname(__file__),'../res/balls.atlas'))
        self.actor_configs.append({'id':'ball1','class':'actors.ball.BallActor','design_pos':(0,0),'design_size':(90,90)})
        self.actor_configs.append({'id':'ball2','class':'actors.ball.BallActor','design_pos':(0,100),'design_size':(90,90)})

    def load_triggers(self):
        self.triggers['ball1'] = {}
        self.triggers['ball1']['click'] = self.ball1_click

    def trigger_event(self,event):
        print event
        try:
            obj = self.triggers
            for item in event:
                obj = obj[item]
            obj()
        except Exception as e:
            print e
            pass

    def ball1_click(self):
        ball2 = self.child_map['ball2']
        if ball2.state == 'blink':
            ball2.switch('yellow')
        else:
            ball2.switch('blink')





 
