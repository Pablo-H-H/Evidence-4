import re

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        # Regular expression for validating IPv4
        ipv4_pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}'
                                  r'(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$')
        
        # Regular expression for validating IPv6
        ipv6_pattern = re.compile(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$')

        if ipv4_pattern.match(queryIP):
            return "IPv4"
        if ipv6_pattern.match(queryIP):
            return "IPv6"
        return "Neither"

# Example usage:
solution = Solution()
print(solution.validIPAddress("192.168.1.1"))         # "IPv4"
print(solution.validIPAddress("192.168.01.1"))        # "Neither"
print(solution.validIPAddress("192.168.1.0"))         # "IPv4"
print(solution.validIPAddress("2001:0db8:85a3:0000:0000:8a2e:0370:7334")) # "IPv6"
print(solution.validIPAddress("2001:db8:85a3:0:0:8A2E:0370:7334"))        # "IPv6"
print(solution.validIPAddress("2001:0db8:85a3:0000:0000:8a2e:0370:7334:")) # "Neither"
print(solution.validIPAddress("2001:0db8:85a3:0:0:8a2e:0370:7334:1234"))   # "Neither"
