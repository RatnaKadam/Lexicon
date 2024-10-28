function monkeyTrouble(aSmile, bSmile) {
    return aSmile === bSmile;
}

function main() {
    // Test cases 
    console.log(monkeyTrouble(false, false)); 
    console.log(monkeyTrouble(true, false)); 
    console.log(monkeyTrouble(false, true)); 
    console.log(monkeyTrouble(true, true));  
}

// Call the main function to execute
main();