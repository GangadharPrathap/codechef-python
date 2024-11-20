'''
On the occasion of World Blood Donor Day, Chef has organized an event to reward regular blood donars in Chefland.
If the donor has made less than or equal to 3 donations, they receive a BRONZE donor badge.
If the donor has made more than 3 but less than equal to 6 donations, they receive a SILVER donor badge.
If the donor has made more than 6 donations, they receive a GOLD donor badge.
Given that a person has made X donations, find the badge they receive.'''
n=int(input())
for i in range(n):
    a=int(input())
    if(a<=3):
        print('BRONZE')
    elif(3<a<=6):
        print('SILVER')
    else:
        print('GOLD')
