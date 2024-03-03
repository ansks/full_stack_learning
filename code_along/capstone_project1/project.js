
// Getting variable 
var header  = document.querySelector("h1");
var body  = document.querySelector("body")

// console.log("The value is " + header)

header.style.color = "yellow";

function colorChanger() {

    var hexValues = '0123456789ABCDEF';
    var finalColor = "#";

    for (index = 0; index <  6; index++) {

        finalColor += hexValues[Math.floor(Math.random()*16)];
        
    }

    return finalColor
}


function colorPicker(){
    header.style.color = colorChanger();
    // body.style.color = colorChanger();
}


setInterval("colorPicker()", 500)