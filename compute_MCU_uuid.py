# Short script to compute the MCU UUID from the three hexadecimals coming out from the s.get_mcu_uuid() function.
# This script emulates what is done in the libabc.py file, but with a different input.

if __name__ == "__main__":
    strings = ["0x001D0026", "0x3331470F", "0x37383632"]

    # Compute the MCU UUID
    m = [format(int(string, 16), '08b') for string in strings]
    uuid = int(m[0] + m[1] + m[2], 2)
    print("MCU  UUID:", uuid)