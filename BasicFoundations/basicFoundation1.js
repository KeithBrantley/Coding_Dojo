// 1. Get 1 to 255 - Write a function that returns an array with all the numbers from 1 to 255.

function returnAnArray() {
    var arr = [];
    for (var i = 1; i <= 255; i++) {
        console.log(i);
        arr.push(i);
    }
    return arr;
}

returnAnArray();



// 2. Get even 1000 - Write a function that would get the sum of all the even numbers from 1 to 1000.  You may use a modulus operator for this exercise.

function sumOfEvenNumbers() {
    var sum = 0;
    for (var i = 0; i <= 1000; i += 2) {
        sum = sum + i;
        // console.log(x);
    }
    return sum;
}

sumOfEvenNumbers();


// 3. Sum odd 5000 - Write a function that returns the sum of all the odd numbers from 1 to 5000. (e.g. 1+3+5+...+4997+4999).

function sumOfOddNumbers() {
    var sum = 0;
    for (var i = 1; i <= 5000; i += 2) {
        sum = sum + i;
    }
    return sum;
}

sumOfOddNumbers();


// 4. Iterate an array - Write a function that returns the sum of all the values within an array. (e.g. [1,2,5] returns 8. [-5,2,5,12] returns 14).

function sumOfArray(arr) {
    var sumOfArr = 0;
    for (var i = 0; i < arr.length; i++) {
        sumOfArr += arr[i];
    }
    return sumOfArr;
}

sumOfArray([1, 2, 5]);


// 5. Find max - Given an array with multiple values, write a function that returns the maximum number in the array. (e.g. for [-3,3,5,7] max is 7)

function arrMaxNum(arr) {
    var max = Math.max.apply(...arr)
    return max;
}

findMax([6, 7, 2, 4, 9]);


// 6. Find average - Given an array with multiple values, write a function that returns the average of the values in the array. (e.g. for [1,3,5,7,20] average is 7.2)

function sumOfArray(arr) {
    var sumOfArr = 0;
    for (var i = 0; i < arr.length; i++) {
        sumOfArr += arr[i] / arr.length;
    }
    return sumOfArr;
}

sumOfArray([1, 3, 5, 7, 20]);


// 7. Array odd - Write a function that would return an array of all the odd numbers between 1 to 50. (ex. [1,3,5, .... , 47,49]). Hint: Use 'push' method.

function oddNumArray(arr) {
    var oddArray = [];
    for (var i = 0; i <= arr.length; i++) {
        if (i % 2 == 1) {
            oddArray.push(i);
        }
    }
    return oddArray;
}

oddNumArray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);


// 8. Greater than Y - Given value of Y, write a function that takes an array and returns the number of values that are greater than Y. For example if arr = [1, 3, 5, 7] and Y = 3, your function will return 2. (There are two values in the array greater than 3, which are 5, 7).

function greaterThanY(arr, y) {
    var y;
    var numGreaterThan = [];
    for (var i = 0; i <= arr.length; i++) {
        if (y < arr[i]) {
            numGreaterThan.push(i);
        }
    }
    return numGreaterThan.length;

}

greaterThanY([5, 8, 7, 10], 6);


// 9. Squares - Given an array with multiple values, write a function that replaces each value in the array with the value squared by itself. (e.g. [1,5,10,-2] will become [1,25,100,4])

function squaredItself(arr) {
    var squaredIndex = [];
    for (var i = 0; i <= arr.length; i++) {
        squaredIndex = arr.map(i => i * i);
    }
    return squaredIndex;
}

squaredItself([1, 5, 10, -2]);


// 10. Negatives - Given an array with multiple values, write a function that replaces any negative numbers within the array with the value of 0. When the program is done the array should contain no negative values. (e.g. [1,5,10,-2] will become [1,5,10,0])

function replaceNegNum(arr) {
    var negNum = arr.map(function(elem){
        if (elem<0){
            elem = 0;
        }
        return elem;
    });
    return negNum; 
}

replaceNegNum([1,5,10,-2]);


// 11/ Max/Min/Avg - Given an array with multiple values, write a function that returns a new array that only contains the maximum, minimum, and average values of the original array. (e.g. [1,5,10,-2] will return [10,-2,3.5])

function maxMinAvg(arr) {
    var newArr = [];
    var sum = 0;
    arr.map(function (elem) {
        sum = sum + elem;
    });
    newArr.push(Math.max.apply(null, arr));
    newArr.push(Math.min.apply(null, arr));
    newArr.push(sum / arr.length);
    return newArr;
}

maxMinAvg([1, 5, 10, -2]);

// 12. Swap Values - Write a function that will swap the first and last values of any given array. The default minimum length of the array is 2. (e.g. [1,5,10,-2] will become [-2,5,10,1]).

function swapIndex(arr) {
    var newArr = arr.slice();
    var temp = newArr[0];
    newArr[0] = newArr[newArr.length-1];
    newArr[newArr.length-1] = temp;
    return newArr; 
}

swapIndex([1,5,10,-2]);


// 13. Number to String - Write a function that takes an array of numbers and replaces any negative values within the array with the string 'Dojo'. For example if array = [-1,-3,2], your function will return ['Dojo','Dojo',2].

function numToString(arr){
    var newArr = [];
    for(var i = 0; i < arr.length; i++){
        if(arr[i] <= 0) {
           newArr.push("Dojo");
        }
        else {
            newArr.push(i);
        }
    }
    return newArr;
}

numToString([-1,-3,2]);
