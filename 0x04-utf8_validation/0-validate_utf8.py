#!/usr/bin/python3
"""
UTF-8 validation module
"""

def validUTF8(data):
    '''Returns True if data is a valid UTF-8 encoding, else False
    data is a list of integers, each integer representing a byte'''

    num_bytes = 0

    # Masks to check the significant bits
    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        # Ensure num is within byte range
        if num > 255:
            return False

        # Get the binary representation of the byte
        byte = num & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte & mask1) == 0:
                continue
            elif (byte & (mask1 >> 1)) == (mask1 >> 1):
                num_bytes = 1
            elif (byte & (mask1 >> 2)) == (mask1 >> 2):
                num_bytes = 2
            elif (byte & (mask1 >> 3)) == (mask1 >> 3):
                num_bytes = 3
            else:
                return False
        else:
            # Check if the byte is a valid continuation byte
            if (byte & mask1) != mask1 or (byte & mask2) != 0:
                return False

        num_bytes -= 1

    return num_bytes == 0
