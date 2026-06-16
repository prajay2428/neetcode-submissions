class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk=[]
        for asteroid in asteroids:
            alive = True
            while alive and stk and stk[-1]>0 and asteroid<0:
                if stk[-1] > -asteroid:
                    alive = False
                    

                elif stk[-1] == -asteroid:
                    stk.pop()
                    alive = False
                
                else:
                    stk.pop()

            if alive:
                stk.append(asteroid)

        return stk
                    
                