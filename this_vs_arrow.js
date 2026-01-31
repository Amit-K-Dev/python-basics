// this vs arrow functions example

const user = {
  name: "Amit",
  greet: function () {
    console.log(this.name);
  }
};

const userWrong = {
  name: "Amit",
  greet: () => {
    console.log(this.name);
  }
};

user.greet();       // Amit
userWrong.greet();  // undefined
