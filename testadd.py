def scott(xx, yy, ghost):
    return xx + yy + ghost

if __name__ == '__main__':
    print('testing scott')
    assert(scott(3, 7, 11) == 21)
    print('success!')
