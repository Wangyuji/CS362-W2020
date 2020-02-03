import testUtility
import Dominion

class TestCard:
    def setUp(self):
        self.player_name = testUtility.getPlayerNames()
        self.numberCurse = testUtility.getNumberCurse(self.player_name)
        self.numberVictory = testUtility.getNumberVictory(self.player_name)
        self.box = testUtility.getBoxes(self.numberVivtory)
        self.supply_order = testUtility.getSupplyOrder()

        # pick cards from box to be in supply
        self.supply = testUtility.getSupply(self.box, self.player_name, self.numberVictory, self.numberCurse)
        self.trash = []
        self.player = Dominion.Player('Wen')

    def test_init(self):
        self.setUp()
        cost = 1
        buypower = 5

        #instantiate the card object
        card = Dominion.Coin_card(self.player.name, cost, buypower)

        assert card.name == 'Wen'
        assert card.buypower == buypower
        assert card.cost == cost
        assert card.category == "coin"
        assert card.vpoints == 0

    def test_react(self):
        pass