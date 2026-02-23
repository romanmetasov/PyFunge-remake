&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--- Flow ---  <br>
'^' - Change IP moving direction to up<br>
'v' - Change IP moving direction to down<br>
'>' - Change IP moving direction to right<br>
'<' - Change IP moving direction to left<br>
'#' - Jump over the next instruction<br>
'\_' - Logic branching - if top element of stack 0 - change IP move direction to right, otherwise - to left<br>
'|' - Logic branching - if top element of stack 0 - change IP move direction to right, otherwise - to left<br>
'@' - End of program<br>
IP also can 'wrap around'<br>
('IP' - Instruction pointer)<br>
<br>
      --- Push ---<br>  
'0' - Push to stack **0**<br>
'1' - Push to stack **1**<br>
'2' - Push to stack **2**<br>
'3' - Push to stack **3**<br>
'4' - Push to stack **4**<br>
'5' - Push to stack **5**<br>
'6' - Push to stack **6**<br>
'7' - Push to stack **7**<br>
'8' - Push to stack **8**<br>
'9' - Push to stack **9**<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--- Stack ---<br>  
'+' - Push to stack **a** + **b**<br>
'-' - Push to stack **a** - **b**<br>
'*' - Push to stack **a** * **b**<br>
'/' - Push to stack **a** / **b**<br>
'\\' - Push to stack **b**, **a**<br>
':' - Duplicate top element of stack<br>
'$' - Delete top element of stack<br>
'%' - Push to stack **a**(mod **b**)<br>
'!' - Logic 'not' - pushes to stack 0 if top element of stack isn't 0, otherwise - pushes 1<br>
'"' - Toggle string mode (if on - all symbols will be pushed to stack like their decimal ASCII codes)<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--- I/O ---  <br>
'&' - Input number (and push it to stack)<br>
'~' - Input char (pushes to stack decimal ASCII code of character)<br>
'.' - Print number<br>
',' - Print char (prints the character whose decimal ASCII code is the top element of the stack)<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--- Changing program ---<br>  
'p' - Put charecter, whose decimal ASCII code is **c** to position **x**(column), **y**(row)<br>
'g' - Push to stack decimal ASCII code of character on position **x**(column), **y**(row)<br>
<br>
<br>
All commands delete the top elements of the stack that were used, except ':'<br>
Stack example:<br>
(top)114, 3, 8, 10, 96, ... (bottom)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;^&nbsp;&nbsp;&nbsp;^&nbsp;&nbsp;^ <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a/c b/y x<br>
