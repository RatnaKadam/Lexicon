var employee = {  
    name: "John Smith",  
    job: "Programmer",  
    age: 31,
    
    nameLength() {
        console.log("Name length:", this.name.length);
    },
    
    lastName(){
        let nameArray = this.name.split(" "); 
        console.log("Last name:", nameArray[nameArray.length - 1]); 
    }
};

employee.nameLength();
employee.lastName();

for (let key in employee) {
    if (typeof employee[key] !== "function") { 
        alert(key.charAt(0).toUpperCase() + key.slice(1) + " is " + employee[key]);
    }
}
function main() {
    employee.nameLength();        
    employee.alertDetails();      
    employee.lastName();          
}

main();