from kgame.image_actor import ImageActor
states = {
"blink":
    {
        "frames":["button-yellow","button-green","button-red"],
        "delay":0.1
    },
"red":"button-red",
"green":"button-green",
"yellow":"button-yellow",
}
class BallActor(ImageActor):
    def __init__(self,atlas,**args):
        super(BallActor,self).__init__(atlas,**args)
        self.states = states
        self.switch('yellow')
        self.handle_touch=True

    def on_click(self):
        self.scene.trigger_event([self.id,'click'])
    
        



