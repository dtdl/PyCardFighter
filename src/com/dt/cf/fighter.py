'''
Created on Oct 17, 2020

@author: GoldenSource
'''

      

class HealthPoint(object):
    '''
    classdocs
    '''
    __maxPoint = None
    __currentPoint = None

    def __init__(self, maxp, currentp):
        '''
        Constructor
        '''
        self.__maxPoint = maxp
        self.__currentPoint = currentp
      
    def setCurrentPoint(self, currentp):
        self.__currentPoint = currentp

    def getCurrentPoint(self):
        return self.__currentPoint

    def getMaxPoint(self):
        return self.__maxPoint
    
    


class Apprentice(object):
    '''
    classdocs
    '''
    __healthP = HealthPoint(100, 100)
#     __manaPoint = HealthPoint(100, 100)
#     __mentalPoint = HealthPoint(100, 100)
    
    __strong = 10
    __wisdom = 10
    
    
    __cardSet = None
    

    def __init__(self, hp, strong, wisdom):
        self.__healthP = HealthPoint(hp, hp)
        self.__strong = strong
        self.__wisdom = wisdom
        '''
        Constructor
        '''
      


class Warrior(Apprentice):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
      


class Wizard(Apprentice):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
      
class Hunter(Apprentice):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
      

class Assassin(Apprentice):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''


    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    pass
   
#     print(help(World))
    hp = HealthPoint(100, 90)
    print(hp.getMaxPoint())
    print(hp.getCurrentPoint())
    hp.setCurrentPoint(0)
    print(hp.getCurrentPoint())
