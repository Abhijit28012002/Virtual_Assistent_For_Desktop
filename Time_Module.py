from datetime import datetime
from Talk_Module import Speak_Funtion
def get_Time():
    time=datetime.now().strftime('Now the time is %H:%M')
    Speak_Funtion(time)
    return time