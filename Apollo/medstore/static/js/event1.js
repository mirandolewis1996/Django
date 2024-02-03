var btn1  = document.getElementById("btn1")
var block1 = document.getElementById("block1")

btn1.addEventListener("click",function(){
    block1.classList.toggle("act1")
})


var searcheight = document.getElementById("searcheight")
var searchsec = document.getElementById("searchsec")

searcheight.addEventListener("mouseover",function(){
    searchsec.classList.add("popheight")
})

searcheight.addEventListener("mouseout",function(){
    searchsec.classList.remove("popheight")
})