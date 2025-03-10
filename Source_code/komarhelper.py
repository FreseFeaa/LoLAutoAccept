import pyautogui
from python_imagesearch.imagesearch import  imagesearch
import time

pyautogui.FAILSAFE = False  #Настройка pyautogui, чтоб за экран курсор не ломал
TIMELAPSE = 1 # Время задержки

acceptButtonImg = 'img/acceptButtonImg.png'
acceptedButtonImg = 'img/acceptedButtonImg.png'
championSelectionImg_flash = 'img/championSelectionImg_flash.png'
championSelectionImg_emote = 'img/championSelectionImg_emote.png'
playButtonImg = 'img/playButtonImg.png'
buttonBan = 'img/buttonBan.png'
supportIcon ='img/supportIcon.png'
banСhamp  = 'img/banchamp.png'
banActiveButton= 'img/banActiveButton.png'
cryTeammateButton = 'img/cryTeammateButton.png'

def checkGameButton():  #Поиск игры
    print("\nПоиск игры...")
    while True:
        coordAcceptButton = imagesearch(acceptButtonImg, 0.8)
        # print("Координаты кнопки принять игру: " + str(coordAcceptButton[0]) +" " + str(coordAcceptButton[1]) )
        if coordAcceptButton[0] != -1:
            pyautogui.click(coordAcceptButton[0], coordAcceptButton[1])
            print("\nИгра принята!")
            break
        time.sleep(TIMELAPSE)

    

def checkChampionSelection():  #Проверка есть ли выбор чемпионов
    flash = imagesearch(championSelectionImg_flash)
    # print("Координаты флеша: " + str(flash[0]) +" " + str(flash[1]))
    emote = imagesearch(championSelectionImg_emote)
    # print("Координаты эмодзи: " +str(emote[0]) +" " + str(emote[1]))

    if emote[0] != -1 or flash[0] != -1:
        return True
    else:
        return False

def checkOtklonenieRebenka():  # Проверка на отклонённую игру
    accepted = imagesearch(acceptedButtonImg, 0.9) #Игра принята
    # print("Координаты кнопки принятой игры: " +  str(accepted[0]) +" " + str(accepted[1]))
    play = imagesearch(playButtonImg, 0.9) #Значок группы
    # print("Координаты значка группы: " + str(play[0]) +" " + str(play[1]))
    if accepted[0] == -1 and play[0] != -1:
        return True
    else:
        return False
    
def banPhase():
    buttonBanStart = imagesearch(buttonBan, 0.8)
    # print("Координаты неактивной кнопки бана: " + str(buttonBanStart[0]) +" " + str(buttonBanStart[1]))
    if buttonBanStart[0] != -1 :
        return True
    else:
        return False
    
def banSvein(): 
    
    supportIconCoord = imagesearch(supportIcon, 0.8)
    # print("Координаты икноки сапорта: " + str(supportIconCoord[0]) +" " + str(supportIconCoord[1]))

    if supportIconCoord[0] != -1:
        pyautogui.click(supportIconCoord[0]+10, supportIconCoord[1]+10)
        time.sleep(TIMELAPSE)
        banСhampCoord = imagesearch(banСhamp, 0.8)
        # print("Координаты икноки Свейна: " + str(banСhampCoord[0]) +" " + str(banСhampCoord[1]))

        if banСhampCoord[0] != -1:
            pyautogui.click(banСhampCoord[0]+10, banСhampCoord[1]+10)
            banActiveButtonCoord = imagesearch(banActiveButton, 0.8)

            if banActiveButtonCoord[0] != -1:
                pyautogui.click(banActiveButtonCoord[0]+10, banActiveButtonCoord[1]+10)
                cryTeammateButtonCoord = imagesearch(cryTeammateButton, 0.8)
                if cryTeammateButtonCoord[0] != -1:
                    pyautogui.click(cryTeammateButtonCoord[0], cryTeammateButtonCoord[1])
                    pyautogui.click(banActiveButtonCoord[0]+10, banActiveButtonCoord[1]+10)
                print('Свейн забанен успешно!')
            else:
                print('Не удалось нажать на кнопку бана')
        else:
            print('Не удалось выбрать свейна')
    else:
         print('Не удалось выбрать иконку саппорта')
    

def main():
    poisk = True
    while poisk is True:
        checkGameButton()
        time.sleep(TIMELAPSE)
        while True:
            otklonenieRebenka = checkOtklonenieRebenka()
            if otklonenieRebenka is True:
                # print("Ебанные дети отклонили игру, ждём блять...")
                break
            
            selectChamp = checkChampionSelection()
            if selectChamp is True:
                print("Начало фазы выбора персонажей")
                time.sleep(TIMELAPSE)
                
                while True:
                    time.sleep(TIMELAPSE)
                    banstart = banPhase()
                    if banstart is True:
                        time.sleep(TIMELAPSE)
                        banSvein()
                        break
                    
                poisk = False
                break

            time.sleep(TIMELAPSE)
    print('Конец работы Komaru Helper, Удачной катки!')
    time.sleep(TIMELAPSE)

if __name__ == '__main__':
    print("Komaru Helper приветсвует вас!")
    main()