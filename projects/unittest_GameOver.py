import testUtility
import Dominion

class TestGameover:
    def setUp(self):
        self.player_name = testUtility.getPlayerNames()
        self.numberCurse = testUtility.getNumberCurse(self.player_name)
        self.numberVictory = testUtility.getNumberVictory(self.player_name)
        self.box = testUtility.getBoxes(self.numberVictory)
        self.supply_order = testUtility.getSupplyOrder()

        # pick cards from box to be in supply
        self.supply = testUtility.getSupply(self.box, self.player_name, self.numberVictory, self.numberCurse)
        self.trash = []
        self.player = Dominion.Player('Wen')


    def test_gameover(self):
        #this function is to test that the game is over by meeting one of two conditions
        #1. province in supply is empty
        #2. two sets of the supply is empty

        #initalize Supply
        self.setUp()
        # there are 3 players hence 12 cards
        assert len(self.supply['Province']) == 12
        assert len(self.supply['Estate']) == 12
        assert len(self.supply['Duchy']) == 12
        assert len(self.supply['Gold']) == 30

        #set province equal to 0
        for i in range(12):
            self.supply['Estate'].pop()

        for i in range(12):
            self.supply['Duchy'].pop()

        for i in range(30):
            self.supply['Gold'].pop()

        #call function
        assert Dominion.gameover(self.supply)
