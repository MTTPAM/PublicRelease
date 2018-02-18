#Embedded file name: otp.avatar.Emote
import types
from otp.otpbase import OTPLocalizer

class Emote:
    EmoteClear = -1
    EmoteEnableStateChanged = 'EmoteEnableStateChanged'

    def __init__(self):
        self.emoteFunc = None

    def isEnabled(self, index):
        if isinstance(index, types.StringType):
            index = OTPLocalizer.EmoteFuncDict[index]
        if self.emoteFunc == None:
            return 0
        if self.emoteFunc[index][1] == 0:
            return 1
        return 0


globalEmote = None
