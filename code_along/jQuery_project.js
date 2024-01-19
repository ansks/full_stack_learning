var player1 = prompt('Player 1: enter your name, you will be blue.');
var player1Color = 'rgb(86, 151, 255)';

var player2 = prompt('Player 2: enter your name, you will be red.');
var player2Color = 'rgb(237, 45, 73)';

var game_on = true;
var table = $('.board tr')

function reportWin(rowIndex, colIndex){
    console.log('You have won starting at this row and column');
    console.log(rowIndex, colIndex)
}

function changeColor(rowIndex, colIndex, color){
    return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color', color)
}

function returnColor(rowIndex, colIndex){
    return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color')
}

function checkBottom(colIndex){

    // var colorReport = returnColor(5, colIndex)

    for (let row = 5; row > -1; row--) {
        
        if(returnColor(row, colIndex) == 'rgb(128, 128, 128)'){
            return row;
        } 
        
    }

}

function colorMatch(one, two, three, four) {
    return (one == two && one == three && one == four && one != 'rgb(128, 128, 128)' && one != undefined)
}


// horizontal win check
function horizontalWinCheck() {
    for (let row = 0; row < 6; row++) {
        for (let col = 0; col < 4; col++) {
            if (colorMatch(returnColor(row, col), returnColor(row, col+1), 
            returnColor(row, col+2), returnColor(row, col+3))){
            
                console.log('horiz');
                reportWin(row, col);
                return true;

            } else {
                continue;
            } 
            
        }
    }
}

// Vertical win check 
function verticalWinCheck() {
    for (let col = 0; col < 7; col++) {
        for (let row = 0; row < 3; row++) {
            if (colorMatch(returnColor(row, col), returnColor(row+1, col), 
            returnColor(row+2, col), returnColor(row+3, col))) {
                console.log('vertz');
                reportWin(row, col);
                return true;
            } else {
                continue;
            }
        }
    }
}


// Diagonal win check

function diagonalWinCheck(){
    for (let col = 0; col < 5; col++) {
        for (var row = 0; row < 7; row++) {
            if (colorMatch(returnColor(row, col), returnColor(row+1, col+1), 
            returnColor(row+2, col+2), returnColor(row+3, row+3))){
                console.log('diag');
                reportWin('diagonal Win');
                return true
            } else if (colorMatch(returnColor(row, col), returnColor(row-1, col+1), 
            returnColor(row-2, col+2), returnColor(row-3, col+3))){
                console.log('diag');
                reportWin('diagonal Win');
                return true
            } else {
                continue;
            }
        }
    }
}

//  Initiating the game.
var currentPlayer = 1;
var currentName = player1;
var currentColor = player1Color;

$('h3').text(player1 + ' it is your turn, drop pick a column to drop.')

$('.board button').on('click', function(){
    
    var col = $(this).closest('td').index();
    var bottamAvail = checkBottom(col);

    changeColor(bottamAvail, col, currentColor);

    if (horizontalWinCheck() || verticalWinCheck() || diagonalWinCheck()){
        $('h3').text(currentName + ', you have won the game.');
        $('h3').fadeOut('fast');
        $('h2').fadeOut('fast');

    } 

    currentPlayer = currentPlayer * -1;

    if(currentPlayer === 1){
        currentName = player1;
        $('h3').text(currentName + ', it is your turn.')
        currentColor = player1Color;
    } else {
        currentName = player2;
        $('h3').text(currentName + ', it is your turn.')
        currentColor = player2Color;
    }



})


// // console.log('Connected!')

// // Click Method
// // $('h1').click(function() {
// //     // $(this).text('New Heading')

// //     $('h1').toggleClass('blueClass')
// // })


// // // Keypress Method
// // $('input').eq(0).keypress(function() {
// //     // $(this).text('New Heading')

// //     $('h1').toggleClass('redClass')
// // })

// // console.log($('li'))

// // // Event
// // $('input').eq(0).keypress(function(event) {
// //     // $(this).text('New Heading')

// //     // $('h1').toggleClass('redClass')

// //     // console.log(event)

// //     if (event.which === 97){
// //         $('li').toggleClass('redClass')
// //     }

// // })


// // // on Method
// // $('h1').on('click', function(){
// //     $(this).toggleClass('redClass')
// // })

// // Annimation
// // $('input').eq(1).on('click', function(){
// //     $('.container').fadeOut(200)
// // })

// /*
// 0. Identify the player.
// 1. Check the clicked circle.
// 2. Check the color of the circle.
// 3. Update the player. 
// $('h3').text( + 'It is your turn, please pick a column to drop your ' +  + ' chip')

// <player name> + It is your turn, please pick a column to drop your <red/blue> chip

// */ 

// // var player1 = prompt("Player 1: Enter you name and you chip color would be Blue.")
// var player1Colour = 'rgb(178, 125, 153)'

// // var player2 = prompt("Player 2: Enter you name and you chip color would be Red.")
// var player2Colour = 'rgb(178, 255, 153)'

// // var baseClass =  {
    
// // }

// var redClass = {
//     'height': '100px',
//     'width': '100px',
//     'background-color': 'red',
//     'border-radius': '50%',
//     'display': 'inline-block',
//     'border': 'black 2px solid',
//     'margin': '1px'
// }

// var redClass = {
//     'height': '100px',
//     'width': '100px',
//     'background-color': 'red',
//     'border-radius': '50%',
//     'display': 'inline-block',
//     'border': 'black 2px solid',
//     'margin': '1px'
// }



// var tableVar = $('table')

// // var rowVar = $('table')
// // var dataClass = $('td')

// // console.log(rowClass)
// // console.log(dataClass)



// //  Solution
// // $('td').css(baseClass)




// // function score(){

// // }

// // $('#c1').click(function(){
// //     $(this).css(redClass)
// // })

// // console.log($('#c2').index())

// // var gameOver = False;

// // while(gameOver){
    
// //     var listItems = $('li')



// // }



// // function checkRow(){
// //     var rowClass = $('tr');

// //     for (index = 0; index < rowClass; index++) {

// //     }

// // }

// // $('td').click(function(event){
    
// //     // console.log(values)

// //     if($(event.target).is('#c1')){

// //         console.log('Anshul')

// //     } else if ($(event.target).is('#c2')) {
        

// //     } else if ($(event.target).is('#c3')) {


// //     } else if ($(event.target).is('#c4')) {
        

// //     } else if ($(event.target).is('#c5')) {


// //     } else if ($(event.target).is('#c6')) {

// //     }

// // })

// // $('tr').click(function(event2){
// //     if($(event2.target).is('#r1')){

// //         console.log('Anshul_Row')
// //     }
// // })
    

// // for (let index = 0; index < 42; index++) {
    
// // }


// // function changeColor(rowIndex, columIndex, color) {
// //     $('table').eq(rowIndex).find('td').eq(columIndex).find('button').css('background-color', color)
// // }


// function reportWin(){
//     console.log("You won starting at this row, col");
//     console.log(rowIndex);
//     console.log(colIndex);
// }

// function changeColor(rowIndex, colIndex, color){
//     $('table').eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color', color)
// }

// function returnColor(rowIndex, colIndex){
//     $('table').eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color')
// }


// var game_on  = true;

// function checkBottom(colIndex) {

//     var colorReport = returnColor(5, colIndex)

//     for (let row = 5; row > -1; row--) {
//         colorReport = returnColor(row, colIndex);
        
//         if (colorReport == 'rgb(125, 125, 125)'){
//             return row
//         }
//     }
// }


// while(game_on){

//     $('table td').on('click', function(){
//         var clickIdx = $(this).index()
//     })

//     for (let rowIndex = tableVar.find('tr').length; rowIndex <-1 ; rowIndex--) {

//         scoreA = 0
//         scoreB = 0
        
//         var rowVar = tableVar.find('tr').eq(rowIndex)
    
//         for (let colIndex = 0; colIndex < rowVar.find('td').length; colIndex++) {
            
//             var colIndex = rowVar.find('td').eq(colIndex)
    
    
//             if(returnColor(rowIndex, colIndex) == player1Colour){
//                 scoreA += 1
//             } else {
//                 scoreA -= 1
//             }
            
//             if(returnColor(rowIndex, colIndex) == player2Colour){
//                 scoreB += 1
//             } else {
//                 scoreB -= 1
//             }
    
//             if (scoreA == 4){
//                 reportWin();
//                 game_on = false;
//             } else if (scoreB == 4){
//                 reportWin();
//                 game_on = false;
//             }
     
//         }
//     }
// }
    


