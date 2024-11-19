// creating a rectangle class

class Rectangle {
    constructor(width, height, color) {
        this.width = width;
        this.height = height;
        this.color = color;
    }

    calcArea() {
        let area = this.width * this.height;
        return area;
    }
}

let react = new Rectangle(5, 4, "Blue");
console.log(react.width);      
console.log(react.height);     
console.log(react.color);      
console.log(react.calcArea()); 
