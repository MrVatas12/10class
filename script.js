function show(hid)
{
    var elem=document.getElementById(hid)
    if (elem)
        elem.style.display="block";
}
function hide(a)
{
    var elem=document.getElementById(a)
    if (elem)
        elem.style.display="none"
}
function check()
{
    if (ответ.answer.value=="Сортавала")
        alert("Верно")
    else alert("Неверно")
}