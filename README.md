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
