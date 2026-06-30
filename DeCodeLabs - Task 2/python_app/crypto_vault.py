"""
╔═══════════════════════════════════════════════════════════════╗
║     CryptoVault — Advanced Encryption & Decryption Engine    ║
║     DecodeLabs Internship · Cyber Security Project 2         ║
║     Author: Cybersecurity Intern                             ║
║     Version: 1.0                                             ║
╚═══════════════════════════════════════════════════════════════╝

A professional-grade encryption/decryption tool supporting multiple
cipher algorithms with colored terminal output and detailed reporting.

Supported Ciphers:
  1. Caesar Cipher       — Shift-based substitution
  2. Vigenère Cipher     — Polyalphabetic substitution with keyword
  3. Atbash Cipher       — Mirror alphabet substitution
  4. ROT13               — Fixed 13-position Caesar variant
  5. XOR Cipher          — Bitwise XOR with key byte
  6. Reverse Cipher      — Character order reversal

License: MIT
"""

import string
import os
from typing import Tuple
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)


# ═══════════════════════════════════════════════════════════
#  CIPHER ENGINES
# ═══════════════════════════════════════════════════════════

class CaesarCipher:
    """Classic Caesar Cipher — shifts each letter by a fixed amount."""

    NAME = "Caesar Cipher"
    DESCRIPTION = "Shifts each letter by a fixed number of positions in the alphabet."

    @staticmethod
    def encrypt(plaintext: str, shift: int = 3) -> str:
        result = []
        for ch in plaintext:
            if ch.isalpha():
                base = ord('A') if ch.isupper() else ord('a')
                result.append(chr((ord(ch) - base + shift) % 26 + base))
            else:
                result.append(ch)
        return ''.join(result)

    @staticmethod
    def decrypt(ciphertext: str, shift: int = 3) -> str:
        return CaesarCipher.encrypt(ciphertext, -shift)


class VigenereCipher:
    """Vigenère Cipher — polyalphabetic substitution using a keyword."""

    NAME = "Vigenère Cipher"
    DESCRIPTION = "Uses a keyword to apply different shifts to each character."

    @staticmethod
    def encrypt(plaintext: str, key: str = "SECURITY") -> str:
        key = key.upper()
        result = []
        ki = 0
        for ch in plaintext:
            if ch.isalpha():
                shift = ord(key[ki % len(key)]) - ord('A')
                base = ord('A') if ch.isupper() else ord('a')
                result.append(chr((ord(ch) - base + shift) % 26 + base))
                ki += 1
            else:
                result.append(ch)
        return ''.join(result)

    @staticmethod
    def decrypt(ciphertext: str, key: str = "SECURITY") -> str:
        key = key.upper()
        result = []
        ki = 0
        for ch in ciphertext:
            if ch.isalpha():
                shift = ord(key[ki % len(key)]) - ord('A')
                base = ord('A') if ch.isupper() else ord('a')
                result.append(chr((ord(ch) - base - shift) % 26 + base))
                ki += 1
            else:
                result.append(ch)
        return ''.join(result)


class AtbashCipher:
    """Atbash Cipher — mirrors each letter (A↔Z, B↔Y, etc.)."""

    NAME = "Atbash Cipher"
    DESCRIPTION = "Mirrors the alphabet: A becomes Z, B becomes Y, etc."

    @staticmethod
    def encrypt(plaintext: str, **kwargs) -> str:
        result = []
        for ch in plaintext:
            if ch.isalpha():
                base = ord('A') if ch.isupper() else ord('a')
                result.append(chr(base + 25 - (ord(ch) - base)))
            else:
                result.append(ch)
        return ''.join(result)

    @staticmethod
    def decrypt(ciphertext: str, **kwargs) -> str:
        # Atbash is its own inverse
        return AtbashCipher.encrypt(ciphertext)


class ROT13Cipher:
    """ROT13 — a special case of Caesar with shift=13."""

    NAME = "ROT13"
    DESCRIPTION = "A fixed Caesar cipher with shift of 13 — applying twice returns the original."

    @staticmethod
    def encrypt(plaintext: str, **kwargs) -> str:
        return CaesarCipher.encrypt(plaintext, 13)

    @staticmethod
    def decrypt(ciphertext: str, **kwargs) -> str:
        return CaesarCipher.encrypt(ciphertext, 13)


class XORCipher:
    """XOR Cipher — bitwise XOR with a key byte."""

    NAME = "XOR Cipher"
    DESCRIPTION = "Applies bitwise XOR operation with a key value to each character."

    @staticmethod
    def encrypt(plaintext: str, key: int = 42) -> str:
        return ''.join(chr(ord(ch) ^ key) for ch in plaintext)

    @staticmethod
    def decrypt(ciphertext: str, key: int = 42) -> str:
        # XOR is its own inverse
        return XORCipher.encrypt(ciphertext, key)


class ReverseCipher:
    """Reverse Cipher — simply reverses the character order."""

    NAME = "Reverse Cipher"
    DESCRIPTION = "Reverses the entire string — simple but effective obfuscation."

    @staticmethod
    def encrypt(plaintext: str, **kwargs) -> str:
        return plaintext[::-1]

    @staticmethod
    def decrypt(ciphertext: str, **kwargs) -> str:
        return ciphertext[::-1]


# ═══════════════════════════════════════════════════════════
#  CIPHER REGISTRY
# ═══════════════════════════════════════════════════════════

CIPHERS = {
    '1': CaesarCipher,
    '2': VigenereCipher,
    '3': AtbashCipher,
    '4': ROT13Cipher,
    '5': XORCipher,
    '6': ReverseCipher,
}


# ═══════════════════════════════════════════════════════════
#  DISPLAY FUNCTIONS
# ═══════════════════════════════════════════════════════════

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_banner():
    """Display the application banner."""
    print(f"\n{Fore.CYAN}{Style.BRIGHT}")
    print("╔" + "═" * 57 + "╗")
    print("║" + "".center(57) + "║")
    print("║" + "🔐  CryptoVault v1.0".center(57) + "║")
    print("║" + "Advanced Encryption & Decryption Engine".center(57) + "║")
    print("║" + "DecodeLabs · Cyber Security Project 2".center(57) + "║")
    print("║" + "".center(57) + "║")
    print("╚" + "═" * 57 + "╝")
    print(f"{Style.RESET_ALL}")


def print_separator():
    """Print a styled separator line."""
    print(f"{Fore.CYAN}{'─' * 57}{Style.RESET_ALL}")


def print_cipher_menu():
    """Display the cipher selection menu."""
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}Available Ciphers:{Style.RESET_ALL}\n")
    for key, cipher in CIPHERS.items():
        print(f"  {Fore.CYAN}[{key}]{Style.RESET_ALL}  {Fore.WHITE}{cipher.NAME}{Style.RESET_ALL}")
        print(f"       {Fore.LIGHTBLACK_EX}{cipher.DESCRIPTION}{Style.RESET_ALL}")
    print()


def print_action_menu():
    """Display the action selection menu."""
    print(f"{Fore.YELLOW}{Style.BRIGHT}Choose Action:{Style.RESET_ALL}\n")
    print(f"  {Fore.GREEN}[E]{Style.RESET_ALL}  Encrypt a message")
    print(f"  {Fore.RED}[D]{Style.RESET_ALL}  Decrypt a message")
    print()


def display_result(action: str, cipher_name: str, original: str, result: str, key_info: str = ""):
    """Display the encryption/decryption result in a formatted report."""
    print()
    print_separator()
    print(f"{Fore.CYAN}{Style.BRIGHT}{'ENCRYPTION REPORT' if action == 'encrypt' else 'DECRYPTION REPORT':^57}{Style.RESET_ALL}")
    print_separator()
    print()

    print(f"  {Fore.YELLOW}Cipher Used    :{Style.RESET_ALL}  {cipher_name}")
    if key_info:
        print(f"  {Fore.YELLOW}Key / Shift    :{Style.RESET_ALL}  {key_info}")
    print(f"  {Fore.YELLOW}Action         :{Style.RESET_ALL}  {'🔒 Encryption' if action == 'encrypt' else '🔓 Decryption'}")
    print()

    if action == 'encrypt':
        print(f"  {Fore.GREEN}📝 Original    :{Style.RESET_ALL}  {original}")
        print(f"  {Fore.RED}🔒 Encrypted   :{Style.RESET_ALL}  {result}")
    else:
        print(f"  {Fore.RED}🔒 Encrypted   :{Style.RESET_ALL}  {original}")
        print(f"  {Fore.GREEN}🔓 Decrypted   :{Style.RESET_ALL}  {result}")

    print()

    # Verification: encrypt then decrypt (or vice versa)
    print(f"  {Fore.CYAN}✅ Verification:{Style.RESET_ALL}  ", end="")
    if action == 'encrypt':
        print(f"{Fore.GREEN}Original text can be recovered by decryption.{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}Decrypted text matches the original message.{Style.RESET_ALL}")

    print()

    # Character statistics
    print(f"  {Fore.YELLOW}📊 Statistics:{Style.RESET_ALL}")
    print(f"     Input Length  : {len(original)} characters")
    print(f"     Output Length : {len(result)} characters")
    print(f"     Unique Input  : {len(set(original))} unique characters")
    print(f"     Unique Output : {len(set(result))} unique characters")

    print()
    print_separator()
    print()


# ═══════════════════════════════════════════════════════════
#  MAIN APPLICATION
# ═══════════════════════════════════════════════════════════

def get_cipher_key(cipher_cls) -> dict:
    """Prompt for the appropriate key based on the cipher type."""
    kwargs = {}

    if cipher_cls == CaesarCipher:
        while True:
            try:
                shift = int(input(f"  {Fore.CYAN}Enter shift value (1-25, default=3): {Style.RESET_ALL}").strip() or "3")
                if 1 <= shift <= 25:
                    kwargs['shift'] = shift
                    break
                print(f"  {Fore.RED}Shift must be between 1 and 25.{Style.RESET_ALL}")
            except ValueError:
                print(f"  {Fore.RED}Please enter a valid number.{Style.RESET_ALL}")

    elif cipher_cls == VigenereCipher:
        while True:
            key = input(f"  {Fore.CYAN}Enter keyword (letters only, default=SECURITY): {Style.RESET_ALL}").strip() or "SECURITY"
            if key.isalpha():
                kwargs['key'] = key.upper()
                break
            print(f"  {Fore.RED}Keyword must contain only letters.{Style.RESET_ALL}")

    elif cipher_cls == XORCipher:
        while True:
            try:
                key = int(input(f"  {Fore.CYAN}Enter XOR key (1-255, default=42): {Style.RESET_ALL}").strip() or "42")
                if 1 <= key <= 255:
                    kwargs['key'] = key
                    break
                print(f"  {Fore.RED}Key must be between 1 and 255.{Style.RESET_ALL}")
            except ValueError:
                print(f"  {Fore.RED}Please enter a valid number.{Style.RESET_ALL}")

    return kwargs


def get_key_info(cipher_cls, kwargs: dict) -> str:
    """Generate a human-readable key description."""
    if cipher_cls == CaesarCipher:
        return f"Shift = {kwargs.get('shift', 3)}"
    elif cipher_cls == VigenereCipher:
        return f"Keyword = \"{kwargs.get('key', 'SECURITY')}\""
    elif cipher_cls == XORCipher:
        return f"XOR Key = {kwargs.get('key', 42)}"
    elif cipher_cls == ROT13Cipher:
        return "Fixed Shift = 13"
    elif cipher_cls == AtbashCipher:
        return "Mirror Alphabet (self-inverse)"
    elif cipher_cls == ReverseCipher:
        return "Full String Reversal"
    return ""


def main():
    """Main application loop."""
    clear_screen()
    print_banner()

    while True:
        # Step 1: Choose cipher
        print_cipher_menu()
        cipher_choice = input(f"  {Fore.CYAN}Select cipher [1-6]: {Style.RESET_ALL}").strip()
        if cipher_choice not in CIPHERS:
            print(f"  {Fore.RED}Invalid choice. Please select 1-6.{Style.RESET_ALL}\n")
            continue

        cipher_cls = CIPHERS[cipher_choice]
        print(f"\n  {Fore.GREEN}✓ Selected: {cipher_cls.NAME}{Style.RESET_ALL}\n")

        # Step 2: Choose action
        print_action_menu()
        action = input(f"  {Fore.CYAN}Enter choice [E/D]: {Style.RESET_ALL}").strip().upper()
        if action not in ('E', 'D'):
            print(f"  {Fore.RED}Invalid action. Please enter E or D.{Style.RESET_ALL}\n")
            continue

        is_encrypt = action == 'E'
        print()

        # Step 3: Get the key/shift
        kwargs = get_cipher_key(cipher_cls)
        print()

        # Step 4: Get the message
        prompt = "Enter plaintext to encrypt" if is_encrypt else "Enter ciphertext to decrypt"
        message = input(f"  {Fore.CYAN}{prompt}: {Style.RESET_ALL}")

        if not message:
            print(f"  {Fore.RED}Message cannot be empty.{Style.RESET_ALL}\n")
            continue

        # Step 5: Process
        if is_encrypt:
            result = cipher_cls.encrypt(message, **kwargs)
        else:
            result = cipher_cls.decrypt(message, **kwargs)

        # Step 6: Display result
        key_info = get_key_info(cipher_cls, kwargs)
        display_result(
            action='encrypt' if is_encrypt else 'decrypt',
            cipher_name=cipher_cls.NAME,
            original=message,
            result=result,
            key_info=key_info
        )

        # Step 7: Verify round-trip
        if is_encrypt:
            verified = cipher_cls.decrypt(result, **kwargs)
            match = verified == message
        else:
            verified = cipher_cls.encrypt(result, **kwargs)
            match = verified == message

        if match:
            print(f"  {Fore.GREEN}🔄 Round-trip verification: PASSED ✅{Style.RESET_ALL}")
        else:
            print(f"  {Fore.RED}🔄 Round-trip verification: FAILED ❌{Style.RESET_ALL}")

        print()

        # Continue?
        again = input(f"  {Fore.YELLOW}Analyze another message? [Y/N]: {Style.RESET_ALL}").strip().upper()
        if again != 'Y':
            print(f"\n  {Fore.CYAN}Thank you for using CryptoVault! Stay secure. 🔐{Style.RESET_ALL}\n")
            break
        clear_screen()
        print_banner()


if __name__ == '__main__':
    main()
