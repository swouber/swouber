# SWOUBER
Swouber is a free open source programming language based on python it acts like assembly and pythom combined it also supports pip and other python package managers

---

## Example Swouber Script (`example.sbr`):

```sbr
md math

fctn greet(name):
    print("Hello", name)

greet("Swouber")
print(math.sqrt(25))
```
Output:

```
Hello Swouber
5.0
```

Swouber other module integration

```
md pygame
md sys

fctn main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Swouber Pygame Example")
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((30, 30, 30))
        
        font = pygame.font.Font(None, 36)
        text = font.render("Hello from Swouber + Pygame!", True, (200, 200, 200))
        screen.blit(text, (50, 220))
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()
```

Make sure to install the module  with

```
pip install pygame
```

# Installation

IT IS NOT RECOMMENDED TO INSTALL VIA THE BINARIES AS IT DOESNT SUPPORT MODULES

this is the correct way 

you need to clone the repo

```
git clone https://github.com/swouber/swouber.git
```
when clone is complete

install python

```
sudo apt update
sudo apt install python3
sudo apt install pip3
```

or on windows

```
start https://www.python.org/ftp/python/3.13.5/python-3.13.5-amd64.exe
```

When python installation is complete run this wrapper

move the working directory to to the bin directory so its accesible

`swouberc.bat` - For Windows Only

`swouberc.sh` - For Linux/Unix Systems

if your on a windows system just simply type

```
swouberc
```

if your on linux unix 

you need to use chmod to install it

```
sudo chmod +x /usr/local/bin/swouberc.sh/

sudo swouberc
swouberc
```

Now Swouberc is installerd


