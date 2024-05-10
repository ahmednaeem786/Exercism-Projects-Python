class SpaceAge:
    planet_values = {'mercury': 0.240846,
                     'venus': 0.61519726,
                     'mars': 1.8808158,
                     'jupiter': 11.862615,
                     'saturn': 29.447498,
                     'uranus': 84.016846,
                     'neptune': 164.79132
                     }
    def __init__(self, seconds: int) -> None:
        self.seconds = seconds
    
    def on_mercury(self) -> float:
        return round((self.seconds / 31557600) / self.planet_values.get('mercury'), 2)
    
    def on_venus(self) -> float:
        return round((self.seconds / 31557600) / self.planet_values.get('venus'), 2)
    
    def on_earth(self) -> float:
        return round(self.seconds / 31557600, 2)
    
    def on_mars(self) -> float:
        return round((self.seconds / 31557600) / self.planet_values.get('mars'), 2)
    
    def on_jupiter(self) -> float:
        return round((self.seconds / 31557600) / self.planet_values.get('jupiter'), 2)
    
    def on_saturn(self) -> float:
        return round((self.seconds / 31557600) / self.planet_values.get('saturn'), 2)
    
    def on_uranus(self) -> float:
        return round((self.seconds / 31557600) / self.planet_values.get('uranus'), 2)
    
    def on_neptune(self) -> float:
        return round((self.seconds / 31557600) / self.planet_values.get('neptune'), 2)

#Used Dictionary in second iteration to avoid redundant calculation as well as better organization