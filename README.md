# secrete-message-automation

pyautogui is python module for desktop automation, you can do any key pressing or mouse events with this module.<br><br>
some functions : <br>
pyautogui.press()   --> this function is used to press any key (eg. 'enter', 'shift', 'ctrl', 'alt', 'a', 'b', etc) <br>
pyautogui.hotkey('ctrl', 'c')    --> to press hotkey (e.g. win+r, ctrl+c)<br>
pyautogui.typewrite('hello world')  -->   to typewrite the characters<br>

I want to do some encryption on this plan text, thats why my code looks like a shit, but anyway it works, and now no one can read the plan text until they run the code<br>
I have troube converting the text messages to ascii 1 by 1, that's why I have writen a ascii generator<br>
run the following to generate python code<br>

python pyascii_converter.py<br>
enter : hello      <-- enter you text here to convert into python code<br>
{chr(104)}{chr(101)}{chr(108)}{chr(108)}{chr(111)}     <-- output will look like this <br>

now copy the output and paste it in f string -->  f" " <br>

pyautogui.typewrite(f"{chr(104)}{chr(101)}{chr(108)}{chr(108)}{chr(111)}")<br>
the above line is the same as :<br>
pyautogui.typewrite("hello")<br>
