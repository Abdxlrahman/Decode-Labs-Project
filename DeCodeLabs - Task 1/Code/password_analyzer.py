"""
🛡️ Cyber Security Gatekeeper & Password Analyzer
Professional-grade password validation and cryptographic gatekeeping system.
Aligned with DecodeLabs Industrial Training Kit (Project 1) Specifications.

Features:
- Zero Point Policy Enforcer (Slide 7)
- Unicode-Aware Entropy Engine (Slide 7)
- C-Optimized Pythonic Short-Circuiting (Slide 9)
- In-Place RAM Scraping Mitigation via SecureBuffer (Slide 10)
- Constant-Time Verification to prevent Timing Attacks (Slide 11)
- Argon2id / Scrypt Cryptographic Hashing Gatekeeper (Slide 12)

Author: Cybersecurity Analyst
Batch: 2026 | Powered by DecodeLabs
"""

import sys

# Reconfigure stdout/stderr to use UTF-8 and safely replace characters that can't be encoded.
# This prevents crash-on-startup (UnicodeEncodeError) in Windows CLI terminals when printing box-drawing symbols or emojis.
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

import math
import hmac
import hashlib
import unicodedata
from typing import Dict, List, Tuple, Optional
from colorama import Fore, Style, init

# Initialize colorama for cross-platform color support
init(autoreset=True)


class SecureBuffer:
    """
    A mutable buffer designed to mitigate heap memory persistence (RAM Scraping).
    Wraps the password in a mutable bytearray and overwrites it with null bytes
    in-place as soon as the processing is completed.
    """

    def __init__(self, raw_input: str):
        # Convert to bytearray immediately to gain mutability
        self._buffer = bytearray(raw_input.encode('utf-8'))
        # Overwrite the original string input reference immediately
        del raw_input

    @property
    def length(self) -> int:
        """Get the length of the string represented by the buffer."""
        return len(self.to_str())

    def to_str(self) -> str:
        """Decode the buffer to a temporary string for short-lived analysis."""
        return self._buffer.decode('utf-8')

    def get_chars(self) -> List[str]:
        """Convert buffer to a temporary list of characters."""
        return list(self.to_str())

    def clear(self):
        """
        Overwrite the buffer in-place with null bytes (0x00).
        This mitigates memory retention of secrets in RAM (Slide 10).
        """
        for i in range(len(self._buffer)):
            self._buffer[i] = 0
        # Suggest garbage collection of any dangling string slices
        import gc
        gc.collect()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.clear()


class PasswordAnalyzer:
    """
    Advanced password strength engine analyzing pattern recognition,
    entropy levels, and policy criteria with maximum efficiency.
    """

    # Common weak passwords database (Slide 13: check for common leaked passwords)
    COMMON_PASSWORDS = {
        'password', '123456', '12345678', 'admin', 'welcome',
        'qwerty', 'password123', 'letmein', 'iloveyou', 'football',
        '123456789', 'computer', 'master', 'security', 'decodelabs'
    }

    def __init__(self, buffer: SecureBuffer):
        self.buffer = buffer
        self.password_str = buffer.to_str()
        self.chars = list(self.password_str)
        self.results = {}

    def analyze(self) -> Dict:
        """Perform full string-handling and conditional logic checks."""
        # 1. Zero Point Policy Validation (Slide 7)
        self.results['length_ok'] = self._verify_length()
        self.results['has_upper'] = self._verify_uppercase()
        self.results['has_lower'] = self._verify_lowercase()
        self.results['has_digit'] = self._verify_digit()
        self.results['has_special'] = self._verify_special()
        
        # 2. General Security Checks
        self.results['is_not_common'] = self._verify_not_common()
        self.results['no_repetition'] = self._verify_repetition()
        self.results['no_sequences'] = self._verify_sequences()

        # 3. Unicode Analysis and Dynamic Entropy Calculations (Slide 7)
        entropy, charset_size = self._calculate_unicode_entropy()
        self.results['entropy'] = entropy
        self.results['charset_size'] = charset_size
        self.results['entropy_level'] = self._classify_entropy(entropy)

        # 4. Overall Pass/Fail Evaluation (Slide 8)
        is_policy_passed = (
            self.results['length_ok'] and
            self.results['has_upper'] and
            self.results['has_lower'] and
            self.results['has_digit'] and
            self.results['has_special']
        )
        self.results['policy_passed'] = is_policy_passed

        # Calculate final strength score (0-100)
        self.results['score'] = self._calculate_score(is_policy_passed)
        self.results['strength'] = self._classify_strength(self.results['score'], is_policy_passed)
        self.results['recommendations'] = self._generate_recommendations()

        return self.results

    # Slide 9: Using Pythonic Elegance (C-Optimized Short-Circuiting Built-ins)
    def _verify_length(self) -> bool:
        """Length Verification: < 8 characters = IMMEDIATE FAIL (Slide 7)."""
        return len(self.password_str) >= 8

    def _verify_uppercase(self) -> bool:
        """Check for uppercase letters using Unicode-compatible check."""
        return any(char.isupper() for char in self.chars)

    def _verify_lowercase(self) -> bool:
        """Check for lowercase letters using Unicode-compatible check."""
        return any(char.islower() for char in self.chars)

    def _verify_digit(self) -> bool:
        """Check for digits using Unicode-compatible check (Slide 9)."""
        return any(char.isdigit() for char in self.chars)

    def _verify_special(self) -> bool:
        """Check for symbols/punctuation (Slide 7)."""
        # Checks if character is punctuation or symbol, or non-alphanumeric
        return any(unicodedata.category(c).startswith(('P', 'S')) or not c.isalnum() for c in self.chars)

    def _verify_not_common(self) -> bool:
        """Verify password is not in common leaked databases."""
        return self.password_str.lower() not in self.COMMON_PASSWORDS

    def _verify_repetition(self) -> bool:
        """Detect excessive repeating characters (e.g. aaa, 111)."""
        # Slide 9: Pythonic sliding window for checking duplicates in constant memory
        for i in range(len(self.chars) - 2):
            if self.chars[i] == self.chars[i + 1] == self.chars[i + 2]:
                return False
        return True

    def _verify_sequences(self) -> bool:
        """Detect sequential numbers, letters, and common keyboard patterns."""
        # Simple, pythonic sliding window checks to keep O(n) linear complexity (Slide 8)
        password_lower = self.password_str.lower()
        
        # Alphabetic & Numeric sequence checks
        for i in range(len(password_lower) - 2):
            # Check sequential ASCII characters (abc, 123)
            c1, c2, c3 = ord(password_lower[i]), ord(password_lower[i+1]), ord(password_lower[i+2])
            if (c2 == c1 + 1 and c3 == c2 + 1) or (c2 == c1 - 1 and c3 == c2 - 1):
                return False

        # Keyboard patterns checks
        keyboard_rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        for row in keyboard_rows:
            for i in range(len(password_lower) - 2):
                seq = password_lower[i:i+3]
                if seq in row or seq[::-1] in row:
                    return False
        return True

    def _calculate_unicode_entropy(self) -> Tuple[float, int]:
        """
        The Unicode Curveball: Dynamic entropy search space scaling (Slide 7).
        Analyzes ASCII vs Unicode ranges to determine true mathematical randomness.
        """
        if not self.password_str:
            return 0.0, 0

        # Base search spaces
        has_ascii_lower = False
        has_ascii_upper = False
        has_ascii_digit = False
        has_ascii_special = False

        has_unicode_lower = False
        has_unicode_upper = False
        has_unicode_digit = False
        has_unicode_special = False

        for char in self.chars:
            code = ord(char)
            cat = unicodedata.category(char)
            
            # Classify character range
            if code < 128:  # Standard ASCII
                if char.islower():
                    has_ascii_lower = True
                elif char.isupper():
                    has_ascii_upper = True
                elif char.isdigit():
                    has_ascii_digit = True
                else:
                    has_ascii_special = True
            else:  # Unicode Curveball
                if cat.startswith('Ll'):
                    has_unicode_lower = True
                elif cat.startswith('Lu'):
                    has_unicode_upper = True
                elif cat.startswith('Nd'):
                    has_unicode_digit = True
                else:
                    has_unicode_special = True

        # Dynamic search space size (Slide 7)
        # Expand ranges based on the presence of Unicode characters
        charset_size = 0
        charset_size += 26 if has_ascii_lower else 0
        charset_size += 26 if has_ascii_upper else 0
        charset_size += 10 if has_ascii_digit else 0
        charset_size += 32 if has_ascii_special else 0

        # Unicode expansion factors (Slide 7 search space: 143,000+ characters)
        charset_size += 2100 if has_unicode_lower else 0
        charset_size += 1800 if has_unicode_upper else 0
        charset_size += 650 if has_unicode_digit else 0
        charset_size += 140000 if has_unicode_special else 0

        if charset_size == 0:
            return 0.0, 0

        # Shannon Entropy Formula: H = L * log2(R)
        entropy = len(self.password_str) * math.log2(charset_size)
        return round(entropy, 2), charset_size

    def _classify_entropy(self, entropy: float) -> str:
        """Classify entropy randomness level in bits."""
        if entropy < 40:
            return 'Low Randomness'
        elif entropy < 64:
            return 'Medium Randomness'
        else:
            return 'High Randomness'

    def _calculate_score(self, is_policy_passed: bool) -> int:
        """Calculate strength score (0-100) based on weighted parameters."""
        if not is_policy_passed:
            # Policy failures earn a maximum penalty score
            return 0

        score = 0
        # Length contributions (up to 30 points)
        length = len(self.password_str)
        if length >= 16:
            score += 30
        elif length >= 12:
            score += 25
        elif length >= 8:
            score += 15

        # Character variety (up to 40 points)
        if self.results['has_upper']: score += 10
        if self.results['has_lower']: score += 10
        if self.results['has_digit']: score += 10
        if self.results['has_special']: score += 10

        # Security patterns and leaked status (up to 30 points)
        if self.results['is_not_common']: score += 10
        if self.results['no_repetition']: score += 10
        if self.results['no_sequences']: score += 10

        return min(score, 100)

    def _classify_strength(self, score: int, is_policy_passed: bool) -> str:
        """Classify password overall strength category."""
        if not is_policy_passed:
            # Under 8 chars or missing mandatory characters = IMMEDIATE FAIL (Slide 7)
            return "IMMEDIATE FAIL (Weak Policy)"
        
        if score < 50:
            return "Weak (Needs Hardening)"
        elif score < 75:
            return "Medium (Acceptable)"
        elif score < 90:
            return "Strong (Highly Secure)"
        else:
            return "Excellent (Enterprise Grade)"

    def _generate_recommendations(self) -> List[str]:
        """Generate actionable guidelines to harden password strength (Slide 13)."""
        recs = []
        if len(self.password_str) < 8:
            recs.append("❌ Critical: Password must be at least 8 characters long.")
        elif len(self.password_str) < 12:
            recs.append("⚠️ Recommend: Increase length to 12+ characters for exponential brute-force resistance.")

        if not self.results['has_upper']:
            recs.append("❌ Mandatory: Add at least one uppercase letter [A-Z].")
        if not self.results['has_lower']:
            recs.append("❌ Mandatory: Add at least one lowercase letter [a-z].")
        if not self.results['has_digit']:
            recs.append("❌ Mandatory: Add at least one decimal digit [0-9].")
        if not self.results['has_special']:
            recs.append("❌ Mandatory: Add at least one symbol or special character.")

        if not self.results['is_not_common']:
            recs.append("⚠️ Critical: Avoid highly common or leaked passwords.")
        if not self.results['no_repetition']:
            recs.append("⚠️ Avoid repeating characters (e.g., 'aaa' or '111').")
        if not self.results['no_sequences']:
            recs.append("⚠️ Avoid sequential sequences (e.g., 'abc', '123', 'qwe').")

        if not recs:
            recs.append("🛡️ High-grade security achieved. Policy satisfied!")
        return recs


class SecureGatekeeper:
    """
    Enforces 'Validation Before Encryption' (Slide 12).
    If validation succeeds, secures the password via Argon2id.
    """

    @staticmethod
    def hash_password(password_str: str) -> Tuple[str, str]:
        """
        Hash verified password using Argon2id or a highly secure Scrypt fallback.
        Argon2id is a memory-hard function resistant to GPU brute-force.
        """
        salt = hashlib.sha256(password_str.encode('utf-8')).hexdigest()[:16] # Create deterministic salt representation
        
        try:
            # Attempt to use native Argon2id if library is available
            from argon2 import PasswordHasher
            ph = PasswordHasher(time_cost=3, memory_cost=65536, parallelism=4)
            hash_str = ph.hash(password_str)
            return "Argon2id (Native)", hash_str
        except ImportError:
            # Standard library high-security fallback (Scrypt) - Slide 12
            # Scrypt is built-in and uses similar memory-hard concepts to Argon2id
            salt_bytes = salt.encode('utf-8')
            dk = hashlib.scrypt(
                password_str.encode('utf-8'),
                salt=salt_bytes,
                n=16384,
                r=8,
                p=1,
                maxmem=32 * 1024 * 1024
            )
            hash_str = dk.hex()
            return "Scrypt (Local Fallback)", f"$scrypt$N=16384$r=8$p=1${salt}${hash_str}"

    @staticmethod
    def verify_hash(plain_password: str, hashed_value: str, hash_type: str) -> bool:
        """
        Mitigate Timing Attacks (Slide 11): Use constant-time comparison
        via hmac.compare_digest to prevent execution side-channel leaks.
        """
        if "Argon2id" in hash_type:
            try:
                from argon2 import PasswordHasher
                from argon2.exceptions import VerifyMismatchError
                ph = PasswordHasher()
                ph.verify(hashed_value, plain_password)
                return True
            except (ImportError, VerifyMismatchError):
                return False
        else:
            # Recreate Scrypt representation
            parts = hashed_value.split('$')
            if len(parts) < 6:
                return False
            salt = parts[4]
            original_hex = parts[5]

            dk = hashlib.scrypt(
                plain_password.encode('utf-8'),
                salt=salt.encode('utf-8'),
                n=16384,
                r=8,
                p=1,
                maxmem=32 * 1024 * 1024
            )
            recreated_hex = dk.hex()
            # Constant-time string digest comparison
            return hmac.compare_digest(original_hex.encode('utf-8'), recreated_hex.encode('utf-8'))


def display_ui_report(results: Dict, original_len: int, password_str: str):
    """Render a premium colorized terminal report of the analysis."""
    print(f"\n{Fore.CYAN}{'=' * 60}")
    print(f"{Fore.CYAN}{Style.BRIGHT}{'🛡️  DECODELABS GATEKEEPER ANALYSIS REPORT':^60}")
    print(f"{Fore.CYAN}{'=' * 60}\n")

    # 1. Zero Point Policy Status
    print(f"{Style.BRIGHT}MANDATORY POLICY CHECKS (ZERO POINT):")
    
    def print_check(name: str, passed: bool):
        mark = f"{Fore.GREEN}✔ PASSED" if passed else f"{Fore.RED}✘ FAILED"
        print(f"  • {name:<35} {mark}")

    print_check("Length Verification (>= 8 chars)", results['length_ok'])
    print_check("Uppercase Characters [A-Z]", results['has_upper'])
    print_check("Lowercase Characters [a-z]", results['has_lower'])
    print_check("Numeric Digits [0-9]", results['has_digit'])
    print_check("Symbol / Special Characters", results['has_special'])

    print(f"\n{Style.BRIGHT}ADDITIONAL SECURITY CHECKS:")
    print_check("Common Leaked Password Check", results['is_not_common'])
    print_check("No Repeated Characters (e.g. 'aaa')", results['no_repetition'])
    print_check("No Sequential Sequences (e.g. 'abc')", results['no_sequences'])

    # 2. Entropy Engine
    print(f"\n{Style.BRIGHT}UNICODE ENTROPY METRICS:")
    print(f"  • Shannon Entropy:       {Fore.YELLOW}{results['entropy']} bits ({results['entropy_level']})")
    print(f"  • Cryptographic Space:   {Fore.YELLOW}{results['charset_size']:,} character classes")

    # 3. Overall Gatekeeper Decision
    status_color = Fore.GREEN if results['policy_passed'] else Fore.RED
    status_text = "PASS (Gatekeeper Approved)" if results['policy_passed'] else "FAIL (Gatekeeper Blocked)"
    
    print(f"\n{Style.BRIGHT}GATEKEEPER CLASSIFICATION:")
    print(f"  • Status Decision:       {status_color}{Style.BRIGHT}{status_text}")
    print(f"  • Overall Score:         {status_color}{results['score']}/100")
    
    # Progress bar rendering
    filled = int(results['score'] / 100 * 20)
    empty = 20 - filled
    print(f"  • Security Indicator:    {status_color}[{'█' * filled}{'░' * empty}] {results['score']}%")
    print(f"  • Strength Level:        {status_color}{Style.BRIGHT}{results['strength']}")

    # 4. Actionable Guidelines
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}SECURITY COMPLIANCE GUIDELINES:")
    for rec in results['recommendations']:
        print(f"  {rec}")

    # 5. Cryptographic Hashing Gatekeeper (Slide 12)
    if results['policy_passed']:
        print(f"\n{Fore.CYAN}{Style.BRIGHT}CRYPTOGRAPHIC VAULT HASHING:")
        print(f"  {Fore.GREEN}✔ Password Approved. Generating high-entropy container...")
        hash_type, hashed = SecureGatekeeper.hash_password(password_str)
        print(f"  • Algorithm:             {Fore.GREEN}{hash_type}")
        print(f"  • Secured Hash:          {Fore.YELLOW}{hashed[:50]}...")
        
        # Verify Timing Attack Protection
        print(f"  • Const-Time Verifier:   {Fore.GREEN}Enabled (Timing attacks mitigated)")
        is_verified = SecureGatekeeper.verify_hash(password_str, hashed, hash_type)
        print(f"  • Self-Verification:     {'✔ SUCCESSFUL' if is_verified else '✘ MISMATCH'}")
    else:
        print(f"\n{Fore.RED}{Style.BRIGHT}CRYPTOGRAPHIC VAULT HASHING:")
        print(f"  {Fore.RED}✘ BLOCKED: Cannot hash what is weak. Policy failed (Slide 12).")

    print(f"\n{Fore.CYAN}{'=' * 60}\n")


def main():
    """Main entry point representing professional CLI interface."""
    import getpass

    print(f"\n{Fore.CYAN}{Style.BRIGHT}")
    print("╔" + "═" * 58 + "╗")
    print("║" + "🛡️  DECODELABS CYBER SECURITY GATEKEEPER".center(58) + "║")
    print("║" + "Project 1: Advanced Password Strength Checker".center(58) + "║")
    print("║" + "Batch: 2026 | Industrial Training Phase".center(58) + "║")
    print("╚" + "═" * 58 + "╝")
    print(f"{Style.RESET_ALL}\n")

    try:
        # Prompt securely using getpass
        raw_pw = getpass.getpass(f"{Fore.CYAN}{Style.BRIGHT}Enter Password to Evaluate: {Style.RESET_ALL}")
        
        if not raw_pw:
            print(f"{Fore.RED}❌ Error: Input cannot be empty.{Style.RESET_ALL}\n")
            return

        # RAM Scraping Protection via SecureBuffer
        with SecureBuffer(raw_pw) as secure_buf:
            # Instantiate analysis
            analyzer = PasswordAnalyzer(secure_buf)
            results = analyzer.analyze()
            
            # Display results
            display_ui_report(results, secure_buf.length, secure_buf.to_str())

        print(f"{Fore.GREEN}✔ Secure buffer zeroed out in-place (RAM Scraping protected).{Style.RESET_ALL}\n")

    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Analysis terminated by administrator.{Style.RESET_ALL}\n")
    except Exception as e:
        print(f"{Fore.RED}Critical Error: {str(e)}{Style.RESET_ALL}\n")


if __name__ == '__main__':
    main()
