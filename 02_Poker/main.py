import random
import unittest
import matplotlib.pyplot as plt


class test_cases(unittest.TestCase):

    def test_pair(self):
        hand = [(11, 0), (9, 2), (3, 1), (9, 3), (2, 2)]
        self.assertTrue(check_pair(check(hand)))

    def test_triplets(self):
        hand = [(11, 0), (9, 2), (3, 1), (9, 3), (2, 2)]
        hand2 = [(11, 0), (9, 2), (9, 1), (9, 3), (2, 2)]
        self.assertFalse(check_triplet(check(hand)))
        self.assertTrue(check_triplet(check(hand2)))

    def test_two_pair(self):
        hand = [(11, 0), (9, 2), (3, 1), (9, 3), (2, 2)]
        hand2 = [(11, 0), (9, 2), (11, 1), (9, 3), (2, 2)]
        self.assertFalse(check_two_pair(check(hand)))
        self.assertTrue(check_two_pair(check(hand2)))

    def test_quad(self):
        hand = [(11, 0), (9, 2), (3, 1), (9, 3), (2, 2)]
        hand2 = [(11, 0), (9, 2), (9, 1), (9, 3), (9, 2)]
        self.assertFalse(check_quads(check(hand)))
        self.assertTrue(check_quads(check(hand2)))

    def test_full_house(self):
        hand = [(11, 0), (9, 2), (3, 1), (9, 3), (2, 2)]
        hand2 = [(9, 0), (9, 2), (3, 1), (9, 3), (3, 2)]
        self.assertFalse(check_full_house(check(hand)))
        self.assertTrue(check_full_house(check(hand2)))

    def test_straight(self):
        hand = [(11, 0), (9, 2), (3, 1), (9, 3), (2, 2)]
        hand2 = [(2, 0), (1, 2), (3, 1), (4, 3), (5, 2)]
        self.assertFalse(check_straight(hand))
        self.assertTrue(check_straight(hand2))


    def test_royal_flush(self):
        hand = [(11, 0), (10, 0), (12, 0), (13, 0), (1, 0)]
        hand2 = [(2, 0), (1, 2), (3, 1), (4, 3), (5, 2)]
        hand3 = [(11, 0), (10, 0), (12, 1), (13, 3), (1, 2)]
        self.assertTrue(check_royalflush(hand))
        self.assertFalse(check_royalflush(hand2))
        self.assertFalse(check_royalflush(hand3))


    def test_flush(self):
        hand = [(11, 0), (9, 2), (3, 1), (9, 3), (2, 2)]
        hand2 = [(11, 2), (9, 2), (3, 2), (8, 2), (2, 2)]
        self.assertFalse(check_flush(hand))
        self.assertTrue(check_flush(hand2))


    def test_straightflush(self):
        hand = [(11, 0), (9, 2), (3, 1), (9, 3), (2, 2)]
        hand2 = [(1, 2), (2, 2), (3, 2), (5, 2), (4, 2)]
        self.assertFalse(check_straightflush(hand))
        self.assertTrue(check_straightflush(hand2))

    def test_probabilities(self):
        list_of_occurences_of_hands = [0,0,0,0,0,0,0,0,0,0]
        for i in range(0,2000000):
            list_of_occurences_of_hands =check_hand(list_of_occurences_of_hands)
        print(list_of_occurences_of_hands)



def draw_cards():
    index = 0
    cards = [1,2,3,4,5,6,7,8,9,10,11,12,13,
             14,15,16,17,18,19,20,21,22,23,24,25,26,
             27,28,29,30,31,32,33,34,35,36,37,38,39,
             40,41,42,43,44,45,46,47,48,49,50,51,52] # erweiter des auf bis 52 und alles <14
    drawn_cards = []

    

    for i in range(5):
        index = random.randint(0, 51 - i)

        drawn_cards.append(((cards[index]%13)+1,cards[index]//13))

        cards.append(cards.pop(index))

    return drawn_cards


def check(cards_to_check):

    card_count = [0,0,0,0,0,0,0,0,0,0,0,0,0]

    for i in cards_to_check:
        card_count[i[0]-1] +=1

    while 0 in card_count:
        card_count.remove(0)

    while 1 in card_count:
        card_count.remove(1)

    return card_count


def check_quads(card_count):

    if 4 in card_count:
        return True
    
    else:
        return False

def check_pair(card_count):

    if 2 in card_count:
        return True
      
    else:
        return False
    
def check_triplet(card_count):

    if 3 in card_count:
        return True

    else: 
        return False

def check_full_house(card_count):

    if 2 in card_count and 3 in card_count:
        return True
    
    else: 
        return False

def check_two_pair(card_count):

    if 2 in card_count:
        card_count.pop(card_count.index(2))
        if 2 in card_count:
            return True
    
    else:
        return False

def check_straight(card_count):
    card_count.sort(key=lambda x:x[0])
    if card_count[0][0] == 1 and card_count[1][0] == 2 and card_count[2][0] == 3 and card_count[3][0] == 4 and card_count[4][0] == 5 and (check_flush(card_count ) == True):
        return True
    for i in range(0,len(card_count)-1):
        if card_count[i][0] != card_count[i+1][0]-1:
            return False
    return True

def check_royalflush(card_count):
    card_count.sort(key=lambda x:x[0])
    #check for aces for royal straight flush
    if card_count[0][0] == 1 and card_count[1][0] == 10 and card_count[2][0] == 11 and card_count[3][0] == 12 and card_count[4][0] == 13 and (check_flush(card_count ) == True):
        return True

def check_straightflush(card_count):
    card_count.sort(key=lambda x:x[0])
    #check for aces for royal straight flush
    if check_flush(card_count) and check_straight(card_count):
        return True



def check_flush(card_count):
    for i in range(0,len(card_count)-1):
        if card_count[i][1] != card_count[i+1][1]:
            return False
    return True

def check_hand(list_of_occurences_of_hands):
    hand = draw_cards()
    if check_royalflush(hand):
        list_of_occurences_of_hands[9] +=1
    elif check_straightflush(hand):
        list_of_occurences_of_hands[8] +=1
    elif check_quads(check(hand)):
        list_of_occurences_of_hands[7] +=1
    elif check_full_house(check(hand)):
        list_of_occurences_of_hands[6] +=1
    elif check_flush(hand):
        list_of_occurences_of_hands[5] +=1
    elif check_straight(hand):
        list_of_occurences_of_hands[4] += 1
    elif check_triplet(check(hand)):
        list_of_occurences_of_hands[3] +=1
    elif check_two_pair(check(hand)):
        list_of_occurences_of_hands[2] +=1
    elif check_pair(check(hand)):
        list_of_occurences_of_hands[1] +=1
    else:
        list_of_occurences_of_hands[0] +=1

    return list_of_occurences_of_hands




if __name__ == '__main__':
    unittest.main()

    x = draw_cards()
    
    print(x)

    print(check(x))

    print(check_two_pair(check(x)))

