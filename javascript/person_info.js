// creating a Person class

class Person{
    constructor(firstName,lastName,age,email){
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
        this.email = email;
    }

    toString(){
        
        return `${this.firstName} ${this.lastName} (age: ${this.age}, email:${this.email})`
    }
}

new_person = new Person("John","Smith",20,"john@email.com");

console.log(new_person.age);
console.log(new_person.toString());

