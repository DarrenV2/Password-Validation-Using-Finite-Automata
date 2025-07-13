# Authors: Darren Drummond, Frederica Forbes , Justin Edwards & Rajaire Thomas
# Date: July 13, 2025
# DFA Password Validation
**State Table** 

| **Current State**  | **Input: a** | **Input: b** | **Input: A** | **Input: B** | **Input: 0** | **Input: 1** |
| ------------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ |
| **q0** _(trap)_    | q0           | q0           | q0           | q0           | q0           | q0           |
| **q1** _(start)_   | q2           | q2           | q8           | q8           | q0           | q0           |
| **q2**             | q4           | q4           | q9           | q9           | q5           | q5           |
| **q3**             | q3           | q3           | q11          | q11          | q7           | q7           |
| **q4**             | q3           | q3           | q13          | q13          | q6           | q6           |
| **q5**             | q6           | q6           | q13          | q13          | q6           | q6           |
| **q6**             | q7           | q7           | q14          | q14          | q7           | q7           |
| **q7**             | q7           | q7           | q15          | q15          | q7           | q7           |
| **q8**             | q9           | q9           | q9           | q9           | q12          | q12          |
| **q9**             | q10          | q10          | q10          | q10          | q13          | q13          |
| **q10**            | q11          | q11          | q11          | q11          | q14          | q14          |
| **q11**            | q11          | q11          | q11          | q11          | q15          | q15          |
| **q12**            | q13          | q13          | q13          | q13          | q13          | q13          |
| **q13**            | q14          | q14          | q14          | q14          | q14          | q14          |
| **q14**            | q15          | q15          | q15          | q15          | q15          | q15          |
| **q15** _(accept)_ | q15          | q15          | q15          | q15          | q15          | q15          |
