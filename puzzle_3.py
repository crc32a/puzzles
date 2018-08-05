#!/usr/bin/env python

import sys
import os

# 7C jh 7h Qs = 10c

suits = ["c","d","h","s"]
ranks = ["a","1","2","3","4","5","6","7","9","10","j","q","k"]
order_key = {1: (0, 1, 2),
             2: (0, 2, 1),
             3: (1, 0, 2),
             4: (1, 2, 0),
             5: (2, 0, 1),
             6: (2, 1, 0)}

inv_order_key = {}

rank2val = {}

deck = []
inv_deck = {}

def printf(format,*args): sys.stdout.write(format%args)

for i in range(0,13):
    rank2val[ranks[i]] = i

i = 0
for s in suits:
    for r in ranks:
        deck.append( (r,s) )
        inv_deck[(r, s)] = i
        i += 1

for (k, v) in order_key.iteritems():
    inv_order_key[v] = k

def usage(prog):
    printf("usage %s <e|d> (r,s)...\n", prog)
    printf("\n")
    printf("encode or decode cards\n")


def encode_cards(cards):
    offset = getfirstlastcard(cards)
    printf("offset = %s\ncards = %s\n", offset, cards)
    encode_mid3(cards, offset)

def encode_mid3(cards, offset):
    first = cards.pop(0)
    last = cards.pop(-1)
    mid3 = []
    mid3 = cards[1:4]
    tmp_list = []
    for i in xrange(0,3):
        (r, s) = cards.pop(0)
        printf("tmp_list.append( (%s,(%s,%s)\n", inv_deck[(r,s)], r, s)
        tmp_list.append( (inv_deck[(r,s)],(r,s)) )
    tmp_list.sort()
    printf("sorted is %s\n", tmp_list)
    cards.append(first)
    for i in xrange(0, 3):
        v = order_key[offset][i]
        printf("order is %s\n", v)
        (r, v)  = tmp_list[v][1]
        cards.append( (r,v))
    cards.append(last)

        
def decode_cards(cards):
    first = cards.pop(0)
    printf("first card is %s\n", first)
    rank = first[0]    
    suit = first[1]
    tmp_list = []
    tmp_dict = {}
    for i in xrange(0,3):
        r = cards[i][0]
        s = cards[i][1]
        tmp_list.append ( (inv_deck[(r,s)],(r,s)))
    printf("tmp_list = %s\n", tmp_list)
    tmp_list.sort()
    for i in xrange(0,3):
        (r , v) = tmp_list[i][1]
        tmp_dict[(r,v)] = i
    tmp_tup = []
    for i in xrange(0,3):
        tmp_tup.append( tmp_dict[cards[i]])
    printf("tup ordering = %s\n", tuple(tmp_tup))
    offset = inv_order_key[tuple(tmp_tup)]
    printf("offset = %i\n", offset)
    r = ranks[(rank2val[rank] + offset)%13]
    s = suit
    return (r, s)


def getfirstlastcard(cards):
    #find the first matching suit
    suits_left = set(suits)
    
    i = 0
    while len(suits_left) >= 0:
        printf("card is %s suits_left is %s, %i\n", cards[i], suits_left, i)
        suit = cards[i][1]
        if suit not in suits_left:
            si = i
            break
        suits_left.remove(suit)
        i += 1

    #Our duplicate suits chosen is first_i and second_i
    for i in range(0, 5):
        if cards[si][1] == cards[i][1]: # This is the other card
            fi = i
            break
    printf("second card = %s\n", cards[si])

    #find the lesser of the distances between the cards in modulo 13
    fv = rank2val[cards[fi][0]]
    sv = rank2val[cards[si][0]]
    printf("dup suite card1 = %s\n", cards[fi])
    printf("dup suite card2 = %s\n", cards[si])
    printf("(%i - %i ) %% 13 = %d\n", fv, sv, (fv-sv)%13)
    printf("(%i - %i ) %% 13 = %d\n", sv, fv, (sv-fv)%13)
    if (fv-sv)%13 < (sv-fv)%13:
        tmp = cards[0]
        cards[0] = cards[si]
        cards[si] = tmp
        tmp = cards[4]
        cards[4] = cards[fi]
        cards[fi] = tmp
        return (fv - sv) % 13
        
    else:
        tmp = cards[0]
        cards[0] = cards[fi]
        cards[fi] = tmp
        tmp = cards[4]
        cards[4] = cards[si]
        cards[si] = tmp
        return (sv - fv) % 13 
    
if __name__ == "__main__":
    prog = sys.argv[0]
    cards = []
    n = len(sys.argv)
    i = 2
    suit_set = set(suits)
    rank_set = set(ranks)
    if len(sys.argv) <2:
        usage(prog)
        sys.exit()
    ed = sys.argv[1].lower()
    while i + 1 < n:
        rank = sys.argv[i]
        suit = sys.argv[i + 1].lower()
        if suit not in suit_set:
            printf("Error suit %s must be in %s\n", suit, suits)
            sys.exit()
        if rank not in rank_set:
            printf("Error rank %s not found in %s\n", rank, ranks)
            sys.exit()
        i += 2
        cards.append( (rank, suit) )
    if ed == "e" and len(cards) != 5:
        printf("You need to specify 5 cards\n")
        sys.exit()
    elif ed == "d" and len(cards) != 4:
        printf("You need to specify 4 cards\n")
        sys.exit()
    printf("working with cards %s\n", cards)
    if ed == "e":
        encode_cards(cards)
        printf("encoded is %s\n", cards)
        sys.exit()
    if ed == "d":
        card = decode_cards(cards)
        printf("card = (%s, %s)\n", card[0], card[1])
        sys.exit()
    printf("1st argument should be either \"e\" for encode or \"d\"\n")
    printf("for decode\n")
    sys.exit()
