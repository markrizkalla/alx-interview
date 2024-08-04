#!/usr/bin/python3

def validUTF8(data):

    for j in range(len(data)):
        byte = data[j] & 0xFF
        n = 0
        for i in range(7, 0, -1):
            if (byte >> i) == 1:
                n += 1
            else:
                break

        if n == 0:
            continue

        if n == 1 or n > 4 or j + n > len(data):
            return False

        for k in range(n+j):
            tbyte = data[k] & 0xFF
            if (tbyte >> 6) != 2:
                return False

        j = j + (n-1)

    return True
