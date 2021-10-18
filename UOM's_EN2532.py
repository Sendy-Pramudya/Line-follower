from controller import Robot
 
langkah = 1
robot = Robot()

timestep = int(robot.getBasicTimeStep())

leftmotor = robot.getDevice('motor_1')
rightmotor = robot.getDevice('motor_2')
leftmotor.setPosition(float('inf'))
rightmotor.setPosition(float('inf'))

irl2 = robot.getDevice('IRL2')
irl2.enable(timestep)

irl1 = robot.getDevice('IRL1')
irl1.enable(timestep)

ircl = robot.getDevice('IRCL')
ircl.enable(timestep)

ircr = robot.getDevice('IRCR')
ircr.enable(timestep)

irr1 = robot.getDevice('IRR1')
irr1.enable(timestep)

irr2 = robot.getDevice('IRR2')
irr2.enable(timestep)

dsleft = robot.getDevice('ds_left')
dsleft.enable(timestep)

dsright = robot.getDevice('ds_right')
dsright.enable(timestep)

dsfront = robot.getDevice('ds_front')
dsfront.enable(timestep)

def lurus():
    rightmotor.setVelocity(4.5)
    leftmotor.setVelocity(4.5)
def kiri():
    rightmotor.setVelocity(4)
    leftmotor.setVelocity(-4)
def kanan():
    rightmotor.setVelocity(-4)
    leftmotor.setVelocity(4)
def stop():
    rightmotor.setVelocity(0)
    leftmotor.setVelocity(0)

while robot.step(timestep) != -1:
  
    rightmotor.setVelocity(10)
    leftmotor.setVelocity(10)
    
     
    irl2_val = irl2.getValue()
    irl1_val = irl1.getValue()
    ircl_val = ircl.getValue()
    ircr_val = ircr.getValue()
    irr1_val = irr1.getValue()
    irr2_val = irr2.getValue()
    dsright_val = dsright.getValue()
    dsleft_left = dsleft.getValue()
    dsfront_val = dsfront.getValue()

    r1r2 = irr1_val + irr2_val
    lcl1l2 = irl1_val + irl2_val
    rcr1r2 = ircr_val + irr1_val + irr2_val
    l1l2 = ircl_val + irl1_val + irl2_val
    lcrc = ircr_val + ircl_val
    all = rcr1r2 + l1l2
    
    
    print ('{:.2f} {:.2f} {:.2f} {:.2f} {:.2f} {:.2f} {:.2f} {:.2f}'.format (lcl1l2, lcrc, r1r2, l1l2, rcr1r2, all, dsfront_val, langkah))
   

    if langkah == 1:
        if rcr1r2 > 1400 and l1l2 < 1400:
            kiri()
        elif all < 1200:
            lurus()
        elif rcr1r2 < 1400 and l1l2 > 1400:
            kanan()
        elif lcl1l2 < 500:
            stop()
            kiri()
        else:
            if (all > 3600 and dsright_val < 1000) or (all > 3600 and dsleft_left < 1000):
                lurus()
        if all < 3000 and dsleft_left < 1000:
            langkah = 2 
    elif langkah == 2:
        if rcr1r2 < 1400 and l1l2 > 1400:
            kanan()
        elif r1r2 < 500 :
            kanan()        
        elif dsfront_val < 200:
            stop()
        else :
            lurus()
        if l1l2 > 1830:
            langkah = 3
    elif langkah == 3:
        if rcr1r2 > 1400 and l1l2 < 1400:
            kiri()
        elif all < 1200:
            kiri()
        elif rcr1r2 < 1400 and l1l2 > 1400:
            kanan() 
        elif lcl1l2 < 500:
            stop()
            kiri()
        elif dsfront_val < 200:
            stop()
        else :
            lurus()
        if dsleft_left < 804:
            langkah = 4
    elif langkah == 4:
        if lcl1l2 < 500 and rcr1r2 > 600:
            kiri()  
        elif l1l2 < 500 and l1l2 > 350 and r1r2 < 600 and r1r2 > 350 and dsfront_val > 200:
            lurus()      
        elif dsfront_val < 100:
            stop()
        elif r1r2 < 150 and lcl1l2 < 150:
            stop()
        elif all < 806:
            stop()
    