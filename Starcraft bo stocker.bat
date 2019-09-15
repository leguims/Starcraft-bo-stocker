:S
@echo off
cls
set %input%=
set %cmd%=
set %select%=
set %etapes%=
set %etapes2%=
set %boname%=
set %race%=
cls
color 0b
title Starcraft Build-order stocker version 1.1
echo  Cree par Eliot Hermabessiere et Cyprien Rousselot :)
echo.
echo                               _______________________________________________________
echo                                _____ __             ______           ______    __  __
echo                               / ___// /_____ ______/ ____/________ _/ __/ /_  / / / /
echo                               \__ \/ __/ __ `/ ___/ /   / ___/ __ `/ /_/ __/ / / / /
echo                              ___/ / /_/ /_/ / /  / /___/ /  / /_/ / __/ /_  / / / /
echo                             /____/\__/\__,_/_/   \____/_/   \__,_/_/  \__/ /_/ /_/
echo                              ______________________________________________________
echo.
echo                                    Bienvenue dans le stocker de BO starcraft
echo.                                
echo                                        -Ecrivez *info* pour voir les BO-
echo                                        -Ou *create* pour en ajouter un.-
echo.
echo.
set /p input= commande -
if %input%==create goto CR
if %input%==info goto IR
:Erreur
cls
color 0c
echo.
echo                                      ______                              
echo                                     / ____/_____ _____ ___   __  __ _____
echo                                    / __/  / ___// ___// _ \ / / / // ___/
echo                                   / /___ / /   / /   /  __// /_/ // /    
echo                                  /_____//_/   /_/    \___/ \__,_//_/   
echo.
echo                                  oops il ya un probleme dans la matrice
echo.
pause
color 0b
goto S



:CR
cls
set %race%=
echo.
echo                                        ______        __             
echo                                       / ____/_____ _/_/  ___   _____
echo                                      / /    / ___// _ \ / _ \ / ___/
echo                                     / /___ / /   /  __//  __// /
echo                                     \____//_/    \___/ \___//_/
echo.
echo                                          Choisissez une race:
echo.
echo                                        Zerg / Protoss / Terran
echo.
set /p race= commande -
echo.
if "%race%"=="/back" goto S
if "%race%"=="zerg" cd %~dp0\BO\zerg
if "%race%"=="terran" cd %~dp0\BO\terran
if "%race%"=="protoss" cd %~dp0\BO\protoss
goto C

:C
set %etapes%=
cls
echo    %race%
echo.
echo                                        ______        __             
echo                                       / ____/_____ _/_/  ___   _____
echo                                      / /    / ___// _ \ / _ \ / ___/
echo                                     / /___ / /   /  __//  __// /
echo                                     \____//_/    \___/ \___//_/
echo.
echo                               Listez les differentes etapes de vore BO puis
echo                                 ecrivez /finish quand vous aurez termine.
echo                                  /cancel pour annuler la creation de BO
echo.
set /p etapes=  --}
if "%etapes%"=="/cancel" goto S
if "%etapes%"=="/finish" goto S
echo %etapes% >> sans-nom.txt
goto C2





:C2
cls
set %etapes2%=
echo    %race%
echo.
echo                                        ______        __             
echo                                       / ____/_____ _/_/  ___   _____
echo                                      / /    / ___// _ \ / _ \ / ___/
echo                                     / /___ / /   /  __//  __// /
echo                                     \____//_/    \___/ \___//_/
echo.
echo                               Listez les differentes etapes de vore BO puis
echo                                 ecrivez /finish quand vous aurez termine.
echo                                  /cancel pour annuler la creation de BO
echo.
set /p etapes2=  --}
if "%etapes2%"=="/cancel" goto cancel
if "%etapes2%"=="/finish" goto N
echo %etapes2% >> sans-nom.txt
goto C2

:cancel
cls
del sans-nom.txt
goto S


:N
cls
set %boname%=
echo    %race%
echo.
echo                                        ______        __             
echo                                       / ____/_____ _/_/  ___   _____
echo                                      / /    / ___// _ \ / _ \ / ___/
echo                                     / /___ / /   /  __//  __// /
echo                                     \____//_/    \___/ \___//_/
echo.
echo                                       Nommez votre Build-Order
set /p Boname=  --}
ren sans-nom.txt "%boname%".txt
goto CF
echo oupps probleme
goto S



:CF
cls
echo    %race%
echo.
echo                                        ______        __             
echo                                       / ____/_____ _/_/  ___   _____
echo                                      / /    / ___// _ \ / _ \ / ___/
echo                                     / /___ / /   /  __//  __// /
echo                                     \____//_/    \___/ \___//_/
echo.
echo                                     Build-order ajoute avec succes
echo.
pause
goto S


:IR
cls
set %race%=
echo.
echo                                           ____        ____     
echo                                          /  _/____   / __/____ 
echo                                          / / / __ \ / /_ / __ \
echo                                        _/ / / / / // __// /_/ /
echo                                       /___//_/ /_//_/   \____/ 
echo.
echo                                          Choisissez une race:
echo.
echo                                        Zerg / Protoss / Terran
echo.
set /p race= commande -
if "%race%"=="/back" goto S
if %race%==zerg cd %~dp0\BO\zerg
if %race%==terran cd %~dp0\BO\terran
if %race%==protoss cd %~dp0\BO\protoss
goto I


:I
cls
set %select%=
echo    %race%
echo.
echo                                           ____        ____     
echo                                          /  _/____   / __/____ 
echo                                          / / / __ \ / /_ / __ \
echo                                        _/ / / / / // __// /_/ /
echo                                       /___//_/ /_//_/   \____/ 
echo.
echo                             ecrivez le nom du BO a afficher (sans le .txt)
echo                                  /back pour revenir en arriere
echo.
echo                                      Voici les BO Enregistre:
echo.
dir /b
echo.
set /p select= commande -
if "%select%"=="/back" goto IR
goto II
goto Erreur



:II
cls
set %cmd%=
echo    %race%
echo.
echo                                           ____        ____     
echo                                          /  _/____   / __/____ 
echo                                          / / / __ \ / /_ / __ \
echo                                        _/ / / / / // __// /_/ /
echo                                       /___//_/ /_//_/   \____/ 
echo.
echo                                     /back pour revenir en arriere
echo                                     /remove pour supprimer ce BO
echo                                       /modify pour le modifier
echo.
echo                                              %select%
echo.
type "%select%.txt"
echo.
set /p cmd= commande -
if %cmd%==/back goto I
if %cmd%==/remove goto remove
if %cmd%==/modify start notepad "%select%".txt
goto I


:remove
cls
color 0c
del "%select%".txt
echo    %race%
echo.
echo                                           ____        ____     
echo                                          /  _/____   / __/____ 
echo                                          / / / __ \ / /_ / __ \
echo                                        _/ / / / / // __// /_/ /
echo                                       /___//_/ /_//_/   \____/ 
echo.
echo                                            BO supprime
echo.
pause
color 0b
goto I