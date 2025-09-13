import time
import objc
from AVFoundation import AVSpeechSynthesizer, AVSpeechUtterance, NSObject

# Create a delegate to wait for the speech to finish
class SpeechDelegate(NSObject):
    def init(self):
        self = objc.super(SpeechDelegate, self).init()
        self.finished = False
        return self

    def speechSynthesizer_didFinishSpeechUtterance_(self, synth, utterance):
        self.finished = True

# Your words to speak
words = ["shravan", "amulya", "tanvir"]

# Set up speech synthesizer and delegate
delegate = SpeechDelegate.alloc().init()
synth = AVSpeechSynthesizer.alloc().init()
synth.setDelegate_(delegate)

for word in words:
    delegate.finished = False
    utterance = AVSpeechUtterance.speechUtteranceWithString_(word)
    synth.speakUtterance_(utterance)
    
    # Wait until the word is fully spoken
    while not delegate.finished:
        time.sleep(0.1)
 