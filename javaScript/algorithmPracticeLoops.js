// #1 Print odds 1-20
// Print out all odd numbers from 1 to 20
// The expected output will be 1, 3, 5, 7, 9, 11, 13, 15, 17, 19

function printOddNum () {
    for(var i = 0; i<=20; i++) {
        if(i%2 !== 0) {
            console.log(i);
        }
    }
}

printOddNum();




// #2 Sum and Print 1-5
// Sum numbers from 1 to 5, printing out the current number and sum so far at each step of the way
// The expected output will be: Num: 1, Sum: 1, Num: 2, Sum: 3, Num: 3, Sum: 6, Num: 4, Sum: 10, Num: 5, Sum: 15

function printSumAndNum () {
    var sum;
    for(var num = 1; num <= 5; num ++) {
        sum = sum + num;     
    }
    console.log("Num: " + num + ' Sum: '+  num);
}

printSumAndNum();


function printSumAndNum () {
    for(var num = 1; num <= 5; num ++) {
        console.log("Num: " + num);
    }
}

printSumAndNum();


var array = [1, 2, 3, 4, 5];
    
// Getting sum of numbers

var sum = array.reduce(function(a, b){
    return a + b;
    console.log(array[i])
 }, 0);


// for(var i in array ) {
//     console.log("Num: " + i ); 
// }

var array = [1, 2, 3, 4, 5];

for(var i in array ) {
    console.log(array[i] + array[i]);
}

    
var array = [1, 2, 3, 4, 5];
    
// Getting sum of numbers
var sum = array.reduce(function(a, b){
    return a + b;
}, 0);
    
console.log(sum);

var num = [1,2,3,4,5];
var sum = [];
for(var i in num) {
    sum.push(i);
    console.log(sum);
}