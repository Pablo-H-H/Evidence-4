class Solution:
    def isValidIPv4(self, s: str) -> bool:
        # Define states
        states = [
            {'digit': 1},  # State 0: initial state
            {'digit': 1, 'dot': 2},  # State 1: digits of the first, second, third, or fourth number
            {'digit': 3},  # State 2: dot after a number
            {'digit': 3, 'dot': 4},  # State 3: digits of the second, third, or fourth number
            {'digit': 5},  # State 4: dot after the second number
            {'digit': 5, 'dot': 6},  # State 5: digits of the third or fourth number
            {'digit': 7},  # State 6: dot after the third number
            {'digit': 7}   # State 7: digits of the fourth number
        ]

        # Function to determine the character type
        def char_type(c):
            if c in '0123456789':
                return 'digit'
            if c == '.':
                return 'dot'
            return None

        # Check if the segment is valid
        def is_valid_segment(segment):
            if not segment:
                return False
            if len(segment) > 1 and segment[0] == '0':
                return False
            if not 0 <= int(segment) <= 255:
                return False
            return True

        # Split the input into segments by dots
        segments = s.split('.')
        
        # If there are not exactly 4 segments, it's not a valid IPv4 address
        if len(segments) != 4:
            return False

        # Check each segment
        for segment in segments:
            if not is_valid_segment(segment):
                return False

        return True

# Example usage:
solution = Solution()
print(solution.isValidIPv4("192.168.1.1"))    # True
print(solution.isValidIPv4("255.255.255.255")) # True
print(solution.isValidIPv4("256.256.256.256")) # False
print(solution.isValidIPv4("192.168.1"))      # False
print(solution.isValidIPv4("192.168@1.1"))    # False