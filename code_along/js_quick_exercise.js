// alert("Hello, Anshul")
// console.log("Hello")

// Exercise 1:
// var wtPound = prompt("Enter your weight");

// var wtKg = wtPound*0.454;

// alert("Your weight in kilogram is: \n Wait for it. \n" + wtKg);

// console.log("Conversion Done!")


// // While Loop
// var x = 1;
// var constraint = 10

// console.log("the even number number less than " + constraint + " are: \n")

// while( x <= constraint){    
    
//     if (x%2 === 0){
//         console.log(x)
//     }

//     // x = x + 1
//     // x  +=  1;

//     x++;

// }

// For Loop 

// var alpha_string = "Anshul Kumar Singh";

// for (var i = 0; i < alpha_string.length; i+=2) {
    
//     console.log(alpha_string[i])
    
// }

// Loop Exercise 1 & 2:

// var i = 0;

// while(i < 5){
//     console.log("hello")
//     i++
// }

// for (let index = 0; index < 5; index++) {
    
//     console.log("hello")
    
// }

// console.log("Using while loop")
// var i = 1;

// while(i <= 25) {

//     if (i % 2 !== 0) {
//         console.log(i)
//     }
//     i++
// }


// console.log("Using for loop")
// for (let index = 0; index < 26; index++) {
//     if(index % 2 !== 0 ){
//         console.log(index)
//     }
// }


// alert("Welcome to the spy test")

// var firstName = prompt("Enter your first name: ")
// var lastName = prompt("Enter your last name: ")
// var age = prompt("Enter your age: ")
// var height = prompt("Enter your height in centimeter: ")
// var petName = prompt("Enter your pet name: ")


// // The Spy has the same first letter of her First Name and Last Name
// // The Spy is between the Age of 20 and 30 (exclusive of 20 and 30)
// // The Spy is at least 170 centimeters tall.
// // The Spy has a pet name that ends with the letter "y".

// // Name condition
// if (firstName[0] == lastName[0]){
//     nameCondition = true
// } else {
//     nameCondition = false
// }

// // Age condition
// if (age > 20 && age < 30){
//     ageCondition = true
// } else {
//     ageCondition = false
// }

// // Height condition
// if (height >= 170){
//     heightCond = true
// } else {
//     heightCond = false
// }

// if (petName[petName.length -1] == 'y'){
//     petnameCond = true
// } else {
//     petnameCond = false
// }


// if( nameCondition && ageCondition && heightCond && petnameCond){
//     console.log("Welcome to the Grid, Mr. Spy!")
// } else {
//     console.log("Who the hell are you ? \n That\'s not a question. Get out before I bring out my gun.")
// }


// JS Programming Assignment:

// p1
// PROBLEM 1: SLEEPING IN
//
// Write a function called sleepIn that takes in two boolean parameters: weekday
// and vacation.
//
// The parameter weekday is true if it is a weekday, and the parameter vacation is
// true if we are on vacation. We sleep in if it is not a weekday or
// we're on vacation. Return true if we sleep in. So some example input and output:
//
// sleepIn(false, false) → true
// sleepIn(true, false) → false
// sleepIn(false, true) → true


function sleepIn(weekday, vacation) {
    
    if (!weekday || vacation) {
        return true
    } else {
        return false
    }
}

// P2
// PROBLEM 2: MONKEY TROUBLE
//
// We have two monkeys, a and b, and the parameters aSmile and bSmile indicate if
// each is smiling. We are in trouble if they are both smiling or if neither of
// them is smiling. Return true if we are in trouble.
//
// Example Input and Output
//
// monkeyTrouble(true, true) → true
// monkeyTrouble(false, false) → true
// monkeyTrouble(true, false) → false

function monkeyTrouble(aSmile, bSmile) {
    if (aSmile && bSmile){
        console.log("We are in trouble!, both are smiling")
        return true
    } else if (!aSmile && !bSmile ){
        console.log("We are in trouble!, they are not smiling")
        return true
    } else {
        console.log("We are fine. Only one stupid is smiling. Throw a stone at smiling one.")
        return false
    }
}

// P3
// PROBLEM 3: STRING TIMES
//
// Given a string and a non-negative int n, return a larger
// string that is n copies of the original string.
//
// Example input and output:
//
// stringTimes("Hi", 2) → "HiHi"
// stringTimes("Hi", 3) → "HiHiHi"
// stringTimes("Hi", 1) → "Hi"

function stringTimes(stringInput, timesInput) {
    var times = 0;
    var result = "";

    while (times < timesInput) {
        result = result + stringInput
        times++
    }

    return result
}

// P4
// Given 3 numerical values, a b c, return their sum. However, if one of the values is
// 13 then it does not count towards the sum and values to its right do not count.
// So for example, if b is 13, then both b and c do not count.
//
// Hint (Explore using multiple return statements inside a single function!)
//
// Example input and output
//
// luckySum(1, 2, 3) → 6
// luckySum(1, 2, 13) → 3
// luckySum(1, 13, 3) → 1

function luckySum(a, b, c) {

    if ( a < 13 && b < 13 && c < 13) {
        return a + b + c
    } else if (a == 13){
        return null
    } else if (b == 13) {
        return a
    } else {
        return a + b
    }
}


// PROBLEM 5:
//
// You are driving a little too fast, and a police officer stops you. Write code to
// compute the result, encoded as an int value: 0=no ticket, 1=small ticket,
// 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61
// and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2.
// Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
//
// Here are some example inputs and outputs:
//
// caught_speeding(60, false) → 0
// caught_speeding(65, false) → 1
// caught_speeding(65, true) → 0

function caught_speeding(speed, is_birthday){
    //Code Goes Here
    if (!is_birthday){
        if (speed <= 60){
            result = 0 
        } else if (speed > 60 && speed <= 80  ){
            result = 1 
        } else {   
            result = 2
        }
    } else {
        if (speed <= 65){
            result = 0 
        } else if (speed > 65 && speed <= 85  ){
            result = 1 
        } else {   
            result = 2
        }
    }

    return result

  }


  // BONUS: MAKE BRICKS
//
// We want to make a row of bricks that is goal inches long. We have a number of
// small bricks (1 inch each) and big bricks (5 inches each). Return true if it
// is possible to make the goal by choosing from the given bricks. This is a
// little harder than it looks and can be done without any loops in a single line!
//
// If you can't figue this one out, don't worry, that's why its a bonus!
//
// makeBricks(3, 1, 8) → true
// makeBricks(3, 1, 9) → false
// makeBricks(3, 2, 10) → true

function makeBricks(small, big, goal){
    //Code Goes Here

    maxBrick = small*1 + big*5
    
    if (goal > maxBrick) {
        return false
    } else if ((goal%(5*big)) <= small){
        return true
    } else {
        return false
    }

  }


// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!

// Create the functions for the tasks

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array


// REMOVE STUDENT

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//

// DISPLAY ROSTER

// Create a function called display that prints out the orster to the console.


// Start by asking if they want to use the web app

// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.


// var roster = []

// function addName() {
    
//     var namePerson = prompt("Provide the name to add ");
//     roster.push(namePerson);

// }

// function removeName(name){

//     var namePerson = prompt("Provide the name to remove ?");
//     var index = roster.indexOf(namePerson)
    
//     roster.splice(index, 1)

// }

// alert("Welcome to roster planning!");

// var startWebApp = prompt("Would you like to start the webapp? , y or n")
// var action = "empty";

// if (startWebApp === "y"){
    
//     while(action !== "quit"){
//         action = prompt("Select one of the following actions\n add, remove, display or quit." )

//         if (action == 'add') {
//             addName();
//         } else if (action == 'remove'){
//             removeName();
//         } else if (action == 'display'){
//             console.log(roster);
//         } else {
//           alert("Input not recognized.") ;
//         }
//     }
// }

// alert("Thank you for using the webapp.");



// Part 6 - Objects Exercise

////////////////////
// PROBLEM 1 //////
//////////////////

// Given the object:
var employee = {
    name: "John Smith",
    job: "Programmer",
    age: 31
  }
  
  // Add a method called nameLength that prints out the
  // length of the employees name to the console.

  console.log("Length of employee's name: " + employee["name"].length)
  
  
  ///////////////////
  // PROBLEM 2 /////
  /////////////////
  
  // Given the object:
  var employee = {
    name: "John Smith",
    job: "Programmer",
    age: 31
  }
  
  // Write program that will create an Alert in the browser of each of the
  // object's values for the key value pairs. For example, it should alert:
  
  // Name is John Smith, Job is Programmer, Age is 31.
  
  alert("Name is " + employee["name"] + ", Job is " + employee["job"] + ", Age is " + employee['age']+ ".")
  
  ///////////////////
  // PROBLEM 3 /////
  /////////////////
  
  // Given the object:
  var employee = {
    name: "John Smith",
    job: "Programmer",
    age: 31,
    lastName: function(){
        console.log(this.name.split(" ")[1])
    }
  }
  
  // Add a method called lastName that prints
  // out the employee's last name to the console.
  
  // You will need to figure out how to split a string to an array.
  // Hint: http://www.w3schools.com/jsref/jsref_split.asp
  




