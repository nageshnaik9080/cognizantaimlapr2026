"""
Application entry point for the day2 project.
"""

import random


def generate_otp():
    """Generates a random 6-digit OTP (One Time Password)."""
    otp = random.randint(100000, 999999)
    return otp


if __name__ == "__main__":
    otp = generate_otp()
    print(f"Your OTP is: {otp}")
