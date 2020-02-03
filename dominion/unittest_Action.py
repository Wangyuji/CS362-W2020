import testUtility
import Dominion

class TestAction:
    def test_init(self):
        #initialize variables
        cost = 1
        actions = 1
        cards = 1
        buy = 1
        coins = 1
        actionCard = Dominion.Action_card("MegaCard",cost,actions,cards,buy,coins)

        # assert
        assert actionCard.name == "MegaCard"
        assert actionCard.cost == 1
        assert actionCard.actions == 1
        assert actionCard.cards == 1
        assert actionCard.buy == 1
        assert actionCard.coins == 1

    def test_use(self):
        #initalize variables
        player = Dominion.Player("Yujie")
        trash = []
        assert len(player.played) == 0
        assert len(player.hand) == 5
        actionCard = Dominion.Action_card("MegaCard",1, 1, 1, 1, 1)
        player.hand.append(actionCard)
        assert len(player.hand) == 6 #plus 1

        actionCard.use(player, trash)

        #assert
        assert len(player.played) == 1



    def test_augment(self):
        # The code will be similar like use part
        player = Dominion.Player("Yujie")
        actionCard = Dominion.Action_card("MegaCard",1, 1, 1, 1, 1)
        player.actions = 0
        player.buy = 0
        player.purse = 0
        assert player.actions == 0
        assert player.buy == 0
        assert player.purse == 0
        assert len(player.hand) == 5

        actionCard.augment(player)
        #because the cards are all plus 1
        assert player.actions == 1
        assert player.buy == 1
        assert player.purse == 1
        assert len(player.hand) == 6

    def test_play(self):
        pass