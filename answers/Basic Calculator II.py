class Solution:
     def calculate(self, s: str) -> int:
          st = []
          num = 0
          back_operator = "+"

          for i in range(len(s) + 1):
               ch = s[i] if i < len(s) else '\0'
               if ch.isdigit():
                    num = num * 10 + int(ch)
               if not ch.isdigit() and ch != ' ' or i == len(s):
                    if back_operator == '+':
                         st.append(num)
                    if back_operator == '-':
                         st.append(-num)
                    if back_operator == '*':
                         st.append(st.pop() * num)
                    if back_operator == '/':
                         st.append(int(st.pop() / num))
                    
                    back_operator = ch
                    num = 0
          return sum(st)