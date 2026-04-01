# 11. Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.

am=int(input('Enter integer amount in rupees: '))

note_5h=am//500
note_2h=am%500//200
note_1h=am%500%200//100
note_50=am%500%200%100//50
note_20=am%500%200%100%50//20
note_10=am%500%200%100%50%20//10
note_05=am%500%200%100%50%20%10//5
note_02=am%500%200%100%50%20%10%5//2
note_01=am%500%200%100%50%20%10%5%2//1

num= note_5h+note_2h+note_1h+note_50+note_20+note_10+note_05+note_02+note_01

print(f'Minimum no. of notes to represent amount {am} rupees is {num}.')