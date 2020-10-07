'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    let l = s.length;
    const vowels = ['a', 'e', 'i', 'o', 'u'];
    let v = [];
    let c = [];
    for (let char of s) {
        if (vowels.includes(char)) {
            v.push(char);
        } else {
            c.push(char);
        }
    }
    for (let vowel of v) {
        console.log(vowel);
    }
    for (let consonant of c) {
        console.log(consonant);
    }
}


function main() {
    const s = readLine();
    
    vowelsAndConsonants(s);
}
