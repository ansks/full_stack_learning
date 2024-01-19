/* 
Two things has to happen on the front end.

1. Somebody will press restart button. -> All squares will be clear
2. Someone will click on square and value will appear. X -> O -> ''

*/



// Restart Game button
var restart = document.querySelector("#restart_btn")

// Grab all the squares
var all_squares  = document.querySelectorAll("td")


// Clear all the squares 
function clearSquares() {
    for (let index = 0; index < all_squares.length; index++) {
        all_squares[index].textContent = ''
    }
}

restart.addEventListener("click", clearSquares);


//  Method 1: Grab manually each id and update it after checking its content. 
// var oneOne = document.querySelector('#one')

// oneOne.addEventListener("click", function(){
//     if (oneOne.textContent == ''){
//         oneOne.textContent = 'X';
//     } else if (oneOne.textContent == 'X'){
//         oneOne.textContent = 'O';
//     }else {
//         oneOne.textContent = '';
//     }
// })


// Method 2: simply take the 'this' object.

// Check the square markers
function changeMarker() {
    
    if (this.textContent === ''){
        this.textContent = 'X'
    } else if (this.textContent === 'X'){
        this.textContent = 'O'
    } else {
        this.textContent = ''
    }

}


// For loop to add event listeners to all the squares 

for (let index = 0; index < all_squares.length; index++) {
    
    all_squares[index].addEventListener("click", changeMarker)
    
}