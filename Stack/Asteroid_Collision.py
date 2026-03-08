def asteroidCollision(asteroids):
    stk = []

    for curr in asteroids:
        alive = True

        while stk and stk[-1] > 0 and curr < 0:
            if abs(curr) > stk[-1]:
                stk.pop()
                continue
            elif abs(curr) == stk[-1]:
                stk.pop()
                alive = False
                break
            else:
                alive = False
                break

        if alive:
            stk.append(curr)

    return stk

asteroids = [5, 10, -5]
print(asteroidCollision(asteroids))
asteroids = [8, -8]
print(asteroidCollision(asteroids))
asteroids = [10, 2, -5]
print(asteroidCollision(asteroids))