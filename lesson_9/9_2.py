from typing import Tuple


def convert_to_hex(color: Tuple[int, int, int]):
    hex_str = "".join([f"{num:02X}" for num in color])
    return f"#{hex_str}"


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


if __name__ == "__main__":
    print("HEX:", convert_to_hex(RED))
    print("HEX:", convert_to_hex(GREEN))
    print("HEX:", convert_to_hex(BLUE))
