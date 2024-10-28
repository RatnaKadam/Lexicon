function luckySum(a, b, c) {
    if (a === 13) return 0;
    if (b === 13) return a;
    if (c === 13) return a + b;
    return a + b + c;
}
function main()
{
    console.log(luckySum(13,14,15));
    console.log(luckySum(25,13,76));
    console.log(luckySum(34,56,13));
}

main();