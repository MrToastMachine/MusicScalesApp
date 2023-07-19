from allImports import *

pygame.init()

FPS = 30
RES = (1000, 720)
clock = pygame.time.Clock()
win = pygame.display.set_mode(RES)


#FONT SETUP
buttonFont = pygame.font.SysFont('Aldhabi', 40)
titleFont = pygame.font.SysFont('Aldhabi', 40)
textFont = pygame.font.SysFont('Aldhabi', 40)

scaleHeading = TextDisplay(win, 130, 530, titleFont, "Current Scale")
rootNoteHeading = TextDisplay(win, 600, 530, titleFont, "Current Root Note")

myKeyboard = Keyboard(win, buttonFont)

mainMenu = Block(win, 0, 500, RES[0], RES[1] - 500, colourScheme['mainMenu'])
settingsButton = Button(win, 80, 620, 300, 50, colourScheme["button_bg"], buttonFont, "Settings")
controlsButton = Button(win, 570, 620, 300, 50, colourScheme["button_bg"], buttonFont, "Controls")

sidebarNoteMenu = Block(win,RES[0]-50,0,RES[0],RES[1],black)
noteBarButtHeight = RES[1]/12

for i, note in enumerate(allNotes):
    Button(win, RES[0]-50,i*noteBarButtHeight, 50, noteBarButtHeight-2, white, Button.setRootNote, buttonFont, note.capitalize())


def drawFrame():
    win.fill(colourScheme['background'])

    myKeyboard.drawWhites()
    myKeyboard.drawSharps()
    
    Block.drawMenu()
    TextDisplay.drawAllText()

    pygame.display.update()

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            Button.checkClicked(mousePos)
            print(f"CURRENT_ROOT_NOTE = {CURRENT_ROOT_NOTE}")
            myKeyboard.highlightScale(CURRENT_ROOT_NOTE, CURRENT_SCALE)

        elif event.type == pygame.KEYDOWN:
            if allNotes.count(event.unicode.lower()) >= 1:
                print(CURRENT_ROOT_NOTE)
                CURRENT_ROOT_NOTE = event.unicode
                print(CURRENT_ROOT_NOTE)
                myKeyboard.highlightScale(CURRENT_ROOT_NOTE, CURRENT_SCALE)
            elif event.unicode == 'p':
                myKeyboard.highlightScale(CURRENT_ROOT_NOTE, CURRENT_SCALE)
            elif event.key == pygame.K_SPACE:
                myKeyboard.showScale = not myKeyboard.showScale                
    
    drawFrame()
        
"""
Thoughts:
- Be able to choose major or minor scale
- Choose root note and all others in scale get highlighted
- Number all notes in key
- Create new scale feature (Enter numbers for each note in scale)

- Later... Add in chord mode to display chords
    + 1st, 3rd and 5th etc...
- Much much later >> Show notes on guitar frets
"""
