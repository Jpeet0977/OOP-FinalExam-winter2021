import datetime

class VideoGame:
    def __init__(self, name, rating, release_date):
        assert type(name) == str, 'Name of the game has to be a string'
        assert type(rating) == str, 'Rating of the game has to be a string'
        assert type(release_date) == datetime.date, 'Release date of the game has to be of type Datetime'
        rating_possibility = ['EC', 'E', 'E10+', 'T', 'M', 'RP', "AO'"]
        if rating not in rating_possibility:
            raise ValueError(f"Rating has to be one of the following: {rating_possibility}")
        self.__name = name
        self.__rating = rating
        self.__release_date = release_date

    @property
    def name(self):
        return(self.__name)
    
    @property
    def rating(self):
        return(self.__rating)
    
    @rating.setter
    def set_rating(self, new_rating):
        self.__rating = new_rating
        # Uncomment this bottom line if you want a return of the new setter...
        #return self.__rating
    
    @property
    def release_date(self):
        return(self.__release_date)
    
    def __str__(self):
        return f"{self.name} Rated: {self.rating} \nRelease Date: {self.release_date.strftime('%b, %Y')}"


class RPG(VideoGame):
    rpg_game_id = 0
    def __init__(self, name, rating, release_date, massively_multiplayer = True):
        VideoGame.__init__(self, name, rating, release_date)
        assert type(name) == str, 'Name of the game has to be a string'
        assert type(rating) == str, 'Rating of the game has to be a string'
        assert type(release_date) == datetime.date, 'Release Date must be of type datetime'
        assert type(massively_multiplayer) == bool, 'MMO must be True or False'
        self.massively_multiplayer = massively_multiplayer
    
        RPG.rpg_game_id += 1
        self.rpg_game_id = RPG.rpg_game_id

    @property
    def game_id(self):
        return self.rpg_game_id
    
    def __str__(self):
        if self.massively_multiplayer == True:
            multiplayer_or_not = 'Multiplayer'
        else:
            multiplayer_or_not = 'Single Player'
        return f"{self.name} Rated: {self.rating}\nRelease Date: {self.release_date.strftime('%d %b, %Y')}\nRPG Game ID: {self.game_id}\nType: {multiplayer_or_not}"

if __name__ == '__main__':
    #Example given
    print('This is a Test of the example in the PDF')
    print('~'*50)
    pong = VideoGame(name='Pong', rating='E', release_date = datetime.date(1972, 11, 29))
    print(pong)
    print('~'*50)
    print()

    print('Testing the getters and setters to ensure that they work')
    print('~'*50)

    #This will print current raiting that has been set.
    print('The current raiting of Pong:')
    print(pong.rating)
    # We are changing the rating using the setter.
    pong.set_rating = 'E10+'
    print('The new rating of Pong after using setter: ')
    print(pong.rating)
    #Print the release_date with the getter.
    print('Release Date of Pong:')
    print(pong.release_date)
    print('~'*50)
    print()

    print('This is a test of the example given in the PDF')
    print('~'*50)
    # Testing the WoW example given in class. If you play WoW Pranjal, let me know! Could do some raiding this summer :D
    wow = RPG(name='World of Warcraft', rating='T', release_date = datetime.date(2004, 11, 23))
    print(wow)
    #Testing to see the getters and setters also work in the RPG class
    #wow.set_rating = 'M'
    #print(wow.rating)
    print('~'*50)
    print()

    print('This is a test of 2 created VideoGame objects')
    print('~'*50)
    TrackMania = VideoGame('TrackMania', 'E', datetime.date(2000, 1, 1))
    print(TrackMania)
    print()
    division2 = VideoGame('Division 2', 'M', datetime.date(2016, 1, 1))
    print(division2)
    print('~'*50)
    print()

    print('This is a test of 2 created RPG objects')
    print('~'*50)
    escapeFromTarkov = RPG('Escape From Tarkov', 'M', datetime.date(2018, 1, 1))
    print(escapeFromTarkov)
    print()
    jediFO = RPG('Jedi Fallen Order', 'M', datetime.date(2019, 1, 1), False)
    print(jediFO)

