import Dominion

class TestPlayer:
    def makeMegaCard(self):
        #The code will be similar like Action
        #initialize variables
        cost = 1
        actions = 1
        cards = 1
        buys = 1
        coins = 1
        #call function
        actionCard = Dominion.Action_card("MegaCard",cost,actions,cards,buys,coins)
        return actionCard

    def test_draw(self):
        #initialize variables
        player = Dominion.Player("Yujie")

        player.hand = []
        player.deck = []
        assert len(player.stack()) == 0

        player.discard = [Dominion.Province()]*10
        player.draw()
        #assert
        #the size of hand is 1 and size of deck is 9
        assert len(player.hand) == 1
        assert len(player.deck) == 9


    def test_action_balance(self):
        #initalize variables
        player = Dominion.Player("Yujie")
        card = self.makeMegaCard()
        #set action equal 2 so that will be ez to calculate
        card.actions = 2
        player.deck.append(card)

        assert len(player.stack()) == 11
        #70/11 = 6 ...4(remain)

        actionBal = player.action_balance()
        #assert
        checkBal = 70/11
        assert actionBal == checkBal



    def test_cardsummary(self):
        #initialize variables
        player = Dominion.Player("Yujie")

        player.hand = []
        player.deck = []
        assert len(player.stack()) == 0
        player.deck = [Dominion.Province()]*10 + [Dominion.Gold()]*10

        testSummary = player.cardsummary()

        # assert
        assert testSummary['Gold'] == 10
        assert testSummary['Province'] == 10
        assert testSummary['VICTORY POINTS'] == 60

    def test_calculatepoints(self):
        #initilize variables
        player = Dominion.Player("Duke")
        player.hand = []
        player.deck = []
        assert len(player.stack()) == 0
        player.deck = [Dominion.Province()]*10 + [Dominion.Duchy()]*10 + [Dominion.Gardens()]*10
        playPoints = player.calcpoints()
        #assert
        assert playPoints == 120