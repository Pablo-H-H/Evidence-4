# Evidence-4

## Description:
Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.

A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses while "192.168.01.1", "192.168.1.00", and "192.168@1.1" are invalid IPv4 addresses.

A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:

1 <= xi.length <= 4
xi is a hexadecimal string which may contain digits, lowercase English letter ('a' to 'f') and upper-case English letters ('A' to 'F').
Leading zeros are allowed in xi.

Validating IP addresses is an essential task in the development and maintenance of network systems and web-based applications. Using techniques such as regex for this validation offers a robust, efficient and 
easy-to-implement solution that guarantees the security, integrity and functionality of applications and systems.

## Models

The deterministic finite automaton paradigm is useful for validation problems where the input must follow a strict and defined pattern. In this solution:

Problem Decomposition: Validation is divided into individual segments, simplifying the validation logic.
Clear Definition of States and Transitions: Each DFA state corresponds to a specific part of the input being validated, and the transitions clearly define the validation rules.
Ease of Implementation and Understanding: Using DFA allows a clear and efficient implementation of the validation algorithm, also facilitating the understanding and maintenance of the code.

![Diagrama sin título-IPv4 Regex drawio](https://github.com/Pablo-H-H/Evidence-4/assets/111140061/f3934b60-0755-45ad-a820-da0e6164e11d)

IPv4 validation
DFA structure for IPv4:

The automaton has five main states: one initial state and four for each segment of the IPv4 address.
Each transition between states validates a segment of the IPv4 address.
Validation Rules:

Each segment must be a number between 0 and 255, with no leading zeros, except for the number 0.
The segments are defined by the regular expression 25[0-5] | 2[0-4][0-9] | 1[0-9]{2} | [1-9]?[0-9].
Periods (.) separate each segment.
DFA flow:

The DFA starts at the initial state, transitions through the segment states validating each one according to the rules, and reaches the final state if all segments are valid.
IPv6 validation
DFA structure for IPv6:

The automaton has nine main states: one initial state and eight for each segment of the IPv6 address.
Each transition between states validates a segment of the IPv6 address.
Validation Rules:

Each segment must be a group of 1 to 4 hexadecimal characters.
The segments are defined by the regular expression [0-9a-fA-F]{1,4}.
The colon (:) separates each segment.
DFA flow:

The DFA starts at the initial state, transitions through the segment states validating each one according to the rules, and reaches the final state if all segments are valid.

## Implementation:

The implementation can be seen in the official page of LeetCode or in this repository in the solution.py archive
LeetCode Solution URL: https://leetcode.com/problems/validate-ip-address/solutions/5252156/regex-for-the-win/


Test:

Here is a set of test that can be used in the solution.py archive and the expected outputs.

192.168.1.1 = IPv4
192.168.01.1 = Neither
192.168.1.0 = IPv4
2001:0db8:85a3:0000:0000:8a2e:0370:7334 = IPv6
2001:db8:85a3:0:0:8A2E:0370:7334 = IPv6
2001:0db8:85a3:0000:0000:8a2e:0370:7334: = Neither
2001:0db8:85a3:0:0:8a2e:0370:7334:1234 = Neither


## Analysis:

### Syntactic Analysis Paradigm:

We could have used a parser to decompose the IP address into its components (for example, segments for IPv4 or groups for IPv6) and then validate each component individually.
Compensations:
Implementing a parser can be more complex and resource-intensive than a simple Regex.
The complexity of the solution could increase due to the need to handle special cases and exceptions.

Dado que las expresiones regulares están optimizadas para el rendimiento y suelen ser altamente eficientes, la complejidad temporal de la solución utilizando regex generalmente sería O(n), donde n es la longitud 
de la cadena de la dirección IP.
