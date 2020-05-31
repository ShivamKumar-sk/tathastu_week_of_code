def Player1(balls,p1,p2,p3):
    sr1=p1*100/balls
    sr2=p2*100/balls
    sr3=p3*100/balls
    print('Strike Rate of first Player: ',sr1)
    print('Strike Rate of second Player: ',sr2)
    print('Strike Rate of third Player: ',sr3)
    MoreBalls(balls,sr1,sr2,sr3)

def MoreBalls(balls,sr1,sr2,sr3):
    score1=sr1*(balls+60)/100
    score2=sr2*(balls+60)/100
    score3=sr3*(balls+60)/100
    print('Runs of first Player is:',score1)
    print('Runs of second Player is:',score2)
    print('Runs of third Player is:',score3)

def Sixes(p1,p2,p3):
    print('Sixes of first Player is:',p1//6)
    print('sixes of second Player is:',p2//6)
    print('sixes of third Player is:',p3//6)

balls=60
player1=int(input('enter runs of first player: '))
player2=int(input('enter runs of second player: '))
player3=int(input('enter runs of third player: '))
Player1(balls,player1,player2,player3)
Sixes(player1,player2,player3)

