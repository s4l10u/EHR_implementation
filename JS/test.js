async function foo() {
    return 42;
}

console.log(foo())

foo().then(result => {
    console.log(result); //42
})