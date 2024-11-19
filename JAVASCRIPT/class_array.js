class Person {
    constructor(firstName, lastName, age, email) {
        if (firstName !== undefined) this.firstName = firstName;
        if (lastName !== undefined) this.lastName = lastName;
        if (age !== undefined) this.age = age;
        if (email !== undefined) this.email = email;
    }
}

// Define the function outside of the Person class
function createPersonsArray() {
    const persons = [
        new Person('Maria', 'Peterson', 22, 'mp@email.com'),
        new Person('Bob'), // Missing lastName, age, and email
        new Person('Stefen', 'Larson', 25), // Missing email
        new Person('Peter', 'Jansson', 24, 'ptr@live.com')
    ];

    return persons; 
}

// Call the function to create the array of Person instances
const persons = createPersonsArray();
console.log(persons);

