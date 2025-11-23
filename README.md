
# LVM Learning-VM

This is an educational virtual machine developed as part of the MIREA University course "Cross-Platform Software Systems Development."

## Installing
From the working directory, run the following command:
```
pip install textual textual-dev
git clone  https://github.com/f1inst0ne/LVM-LearningVM
cd LVM-LearningVM
```

## How to use ?

For Linux/Windows, use the following command:
```
python3 app.py
```
To run the web version:
```
textual serve "python app.py"
```
And visit the following URL:
http://localhost:8000

## ASM syntax
The language used to describe the assembly operations is YAML. The script starts with 
```
commands: 
```
The general syntax looks like this:

```
commands:
  - OPERATION:
    PARAM1: VALUE1
    PARAM2: VALUE2
```
Example:
```
commands:
 - write_const:
    dest_addr: 0
    value: 10
 - read:
    dest_addr: 7
    source_addr: 5
```

A total of 4 operations are implemented:

- Load Constant
```
- write_const:
    dest_addr: VAL1
    value: VAL2
```

- Read from Memory
```
- read:
    dest_addr: VAL1
    addr_of_source_addr: VAL2
```
- Write to Memory
```
- write_values:
    source_addr: VAL1
    dest_addr: VAL2
```
- Unary Operation: Unary Minus
```
  - un_sub:
    dest_addr: VAL1
    source_addr: VAL2
```

## **Important note!**

The default memory size is 30 elements. Should you need to expand or reduce it, modify the **execute()** function in the **interpreter.py** file.

## Why did I do this, and who needs it?
All I want is a little pass and to be happy!!!! And now, behold this ASCII art
```
                _________________________________________
⠀⠀⠀⠀(\__/)⠀⠀⠀⠀|⠀А ты сделал свое задание на допуск ?   |
⠀⠀⠀⠀⠀(•ㅅ•)⠀⠀  |  _____________________________________|
 ＿ノ⠀ヽ⠀ノ⠀＼＿⠀\/ ⠀
/⠀️⠀Y⠀⌒Ｙ⌒⠀Ｙ⠀️⠀️ヽ⠀⠀
(⠀️⠀️⠀️(三ヽ人⠀⠀/⠀⠀⠀|
|⠀️⠀️⠀️ﾉ⠀¯¯\⠀￣￣ヽノ
ヽ＿＿＿⠀⠀＞､＿_／ 
⠀⠀⠀｜⠀(⠀王⠀)〈 
⠀⠀⠀/⠀⠀ﾐ`——彡⠀\
```
