LButton::
{
    static lastClickTime := 0.01
    currentTime := A_TickCount  ; Temps actuel en ms
    timeDifference := currentTime - lastClickTime

    if (timeDifference > 150)  ; Clic lent : clic simple
    {
        Click down
        KeyWait, LButton
        Click up
        lastClickTime := currentTime
        return
    }
    else  ; Clic rapide : double clic simulé
    {
        Click down
        KeyWait, LButton
        Click up
        Sleep, 50
        Click  ; second clic
        lastClickTime := currentTime
        return
    }
}
