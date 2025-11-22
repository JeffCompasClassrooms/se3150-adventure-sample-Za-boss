import pytest
from Room1_example import *
from player import Player
from unittest.mock import call, patch


@pytest.fixture
def load_and_exit(mocker):
    mocker.patch('builtins.input', side_effect=["quit", "y"])
@pytest.fixture
def move_and_exit(mocker):
    mocker.patch('builtins.input', side_effect=["go east", "quit", "y"])
def describe_test_room_entry():
    def it_loads_the_correct_description_initially(load_and_exit):
        player = Player(
            name="bobert",
            health=100,
            condition="healthy",
            current_room=0
        )
        room = Room()
        assert room.description == (
            "You find yourself in a well-illuminated room with a small wooden chest in the center\n"
            "A note on the chest reads \"Answer me these questions three, and rewards I will bestow upon ye\"\n"
            "There is a corridor to your east, a flight of stairs leading up, and a flight of stairs leading down"
        )
    def it_loads_the_correct_amount_of_questions(load_and_exit):
        player = Player(
            name="bobert",
            health=100,
            condition="healthy",
            current_room=0
        )
        room = Room()
        assert room.questions == [
            "I guard my treasure day and night,\nScales like armor, breath of blight.\nBrave the fire if you dare\nWhat creature waits within its lair?", 
            "Born from stone, yet I walk as men.\nStrike me down, I rise again.\nSilent sentinel, carved with grace\nWhat stands watch in an ancient place?", 
            "I vanish in sunlight, appear in the gloam,\nA pathway to danger or to a new home.\nStep through my shimmer, your fate may unfold\nWhat am I, woven of magic untold?"
        ]
    def it_loads_the_correct_amount_of_answers(load_and_exit):
        player = Player(
            name="bobert",
            health=100,
            condition="healthy",
            current_room=0
        )
        room = Room()
        assert room.answers == [
            ["dragon", "a dragon", "wyrm", "a wyrm"], 
            ["a golem", "golem"], 
            ["a portal", "portal", "a gate", "gate", "dimension door"]
        ]
    def it_loads_a_new_description_after_reentry(move_and_exit):
        player = Player(
            name="bobert",
            health=100,
            condition="healthy",
            current_room=0
        )
        room = Room()
        room.enter(player)
        room.enter(player)
        assert room.description == "The light that filled this room has been snuffed out, and the chest is gone"
    def it_deletes_the_chest_after_reentry(move_and_exit):
        player = Player(
            name="bobert",
            health=100,
            condition="healthy",
            current_room=0
        )
        room = Room()
        room.enter(player)
        room.enter(player)
        assert room.objects == []

def describe_riddling_functionality():
    pass

def describe_misc_functionality():
    pass




