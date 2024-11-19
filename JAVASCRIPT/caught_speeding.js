function caught_speeding(speed, is_birthday) {
    let limit1 = is_birthday ? 65 : 60;
    let limit2 = is_birthday ? 85 : 80;

    if (speed <= limit1) return 0;
    else if (speed <= limit2) return 1;
    return 2;
}

function main() {
    // Test cases
    console.log("Test 1 - caught_speeding(60, false):", caught_speeding(60, false)); 
    console.log("Test 2 - caught_speeding(65, false):", caught_speeding(65, false)); 
    console.log("Test 3 - caught_speeding(65, true):", caught_speeding(65, true));   
    console.log("Test 4 - caught_speeding(85, false):", caught_speeding(85, false)); 
    console.log("Test 5 - caught_speeding(80, true):", caught_speeding(80, true));   
    console.log("Test 6 - caught_speeding(90, true):", caught_speeding(90, true));   
}


main();