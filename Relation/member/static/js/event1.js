var crebtn1 = document.getElementById('crebtn1')
var crebtn2  = document.getElementById('crebtn2')
var rmbtn1 = document.getElementById("rmbtn1")


crebtn1.addEventListener("click",function(){
	crebtn2.classList.add("act1")
	
})

rmbtn1.addEventListener("click",function(){
	crebtn2.classList.remove("act1")

})

// over
