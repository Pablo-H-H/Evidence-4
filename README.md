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

192.168.1.1 
IPv4

192.168.01.1 
Neither

192.168.1.0 
IPv4

2001:0db8:85a3:0000:0000:8a2e:0370:7334 
IPv6

2001:db8:85a3:0:0:8A2E:0370:7334 
IPv6

2001:0db8:85a3:0000:0000:8a2e:0370:7334: 
Neither

2001:0db8:85a3:0:0:8a2e:0370:7334:1234 
Neither


## Analysis:

### Complexity Analysis of REGEX
The regular expression defined in regex is in the form of multiple alternatives separated by the operator | (alternation), where each alternative is a specific word delimited by word boundaries (\b). Let's break down the complexity:

Number of Alternatives:
There are 8 alternatives in the pattern, each representing a specific word with word boundaries.
Each alternative is evaluated sequentially until a match is found or all alternatives have been evaluated.

Evaluation of Each Alternative:
Each alternative has a fixed length and can therefore be evaluated in constant O(1) time.

Total Complexity:
The overall complexity of the pattern will depend on the length of the input string and the number of alternatives.
In the worst case, each of the n positions in the input string will be evaluated against the 8 alternatives.
This results in a complexity of O(n⋅m), where n is the length of the input string and m is the number of alternatives in the regular expression.
In this case, since there are 8 alternatives, we can consider m as a constant, so the total complexity of the algorithm would be O(n), where n is the length of 
the input string.

Additional considerations

Regex Engine Efficiency:
The regex engine in Python is quite efficient for patterns of this nature (alternations between specific words). There are no complex repetition operators that 
could induce exponential behavior at runtime.

Input String Size:
The size of the input string can influence the execution time, but given the structure of the pattern, each character in the string will be evaluated a constant 
number of times (8 in this case).


### Comparison with other algorithms
The complexity of the prolog model is O(n) where n is the number of letters that the word has, this is because each iteration of i, if i exists within n, then i 
increments.
Consequently, the time complexity of my solution generally remains at O(n).

Using a regular expression (regex) instead of a loop with multiple comparators can have several advantages, depending on the context and the specific requirements 
of the problem you are trying to solve. Below we will explain why using a regex is better than using code that uses cycles and comparisons with "if" comparators.

Efficiency
Regular expressions are optimized to perform pattern searches efficiently. Regex engines are designed to process and search complex patterns quickly, often faster 
than a manual loop with multiple comparisons, especially when the number of patterns to be compared is large.

Flexibility
Regular expressions are very powerful and flexible. They can handle a wide range of patterns, including matching options like word boundaries, special characters, 
repetitions, and more, in a way that would be complicated and error-prone to implement manually.

Consistency
The regex engine follows well-defined and consistent rules for pattern searching. This can reduce errors compared to manual implementation, where logical errors 
may be more common.

Complexity Comparison

Cycle with Comparators:
If you have a list of words to compare and the length of the input string is n and the number of words is m, the complexity is O(n⋅m).

Regex:
For the same word list and string length, the complexity is also O(n), since the number of patterns (m) is constant and small compared to the length of the input 
string.

### Conclusion
Regex is the best solution because it tends to be more eficient, flexible, and consistent that conventional programming that can be slower, less flexible and can induce logical errors 

## References

Python Software Foundation. (n.d.). re — Regular expression operations. Retrieved from https://docs.python.org/3/library/re.html
