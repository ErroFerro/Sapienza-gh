def check_thumbs_sx(hand_landmarks):
    all_y = [lm.y for lm in hand_landmarks.landmark]
    all_x = [lm.x for lm in hand_landmarks.landmark]
    
    # new
    thumb_x = all_x[2:5]
    other_x = all_x[5:] #but not 0

    indici_nocche=[5, 9, 13, 17]
    nocche=[all_y[i] for i in indici_nocche]
    indici_tips=[8, 12, 16, 20]
    tips=[all_y[i] for i in indici_tips]
    
    dita_chiuse = all(
        all_y[tip] > all_y[nocca]
        for tip, nocca in zip(indici_tips, indici_nocche)
    )

    if min(thumb_x) < max(other_x) and\
        abs(hand_landmarks.landmark[4].y - hand_landmarks.landmark[17].y) < 0.2 and\
        abs(hand_landmarks.landmark[4].y - hand_landmarks.landmark[9].y) < 0.2 and\
            hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x and\
            dita_chiuse:
        return True
    else:
        return False