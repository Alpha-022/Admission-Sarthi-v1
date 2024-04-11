@import url("https://fonts.googleapis.com/css?family=Epilogue:400,600&display=swap");

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  align-items: center;
  background: #f4f4f4;
  color: #333;
  display: flex;
  font-family: 'Epilogue', sans-serif;
  font-size: 16px;
  font-weight: 400;
  height: 100vh;
  justify-content: center;
}

.signup-container {
  display: flex;
  flex-direction: column;
  max-width: 900px;
  border-radius: 0.5em;
}

.left-container {
  background: #6d5acf;
  padding: 2em;
  text-align: center;
  border-radius: 0.5em;
}

.left-container h1 {
  padding: 10px;
  color: #fff;
  font-size: 24px;
}

.left-container h1 a {
  text-decoration: none;
}

.left-container h1 i {
  background: #503b99;
  border-radius: 50%;
  color: #fff;
  font-size: 24px;
  margin-right: 5px;
  padding: 10px;
  transform: rotate(-30deg);
}

.left-container .puppy {
  text-align: center;
  padding: 10px;
  font-size: 20px;
  color: white;
}

.left-container a {
  color: white;
  text-decoration: underline;
}

.left-container a:hover {
  color: #eee;
  transition: 0.2s;
}

.right-container {
  background:#b16fd6;
  display: flex;
  flex-direction: column;
  width: 100%;
  border-radius: 0.5em;
  padding: 2em;
}

.right-container h1:nth-of-type(1) {
  color: #fff;
  font-size: 28px;
  font-weight: 600;
}

.right-container .set {
  margin: 15px 0;
}

.right-container input, select {
  border: 1px solid #ccc;
  border-radius: 4px;
  height: 38px;
  line-height: 38px;
  padding-left: 5px;
  outline: none;
}

.right-container input, .right-container label {
  color: #fff;
}

.right-container label, .right-container input {
  width: 176px;
}

.right-container .category .radio-container {
  display: flex;
  justify-content: space-between;
  width: 100%;
}

.right-container footer {
  align-items: center;
  justify-content: flex-end;
  padding: 2px 40px;
}

.right-container footer button {
  border: 1px solid #ccc;
  height: 38px;
  line-height: 38px;
  width: 100px;
  border-radius: 19px;
  font-family: "Montserrat", sans-serif;
  outline: none;
}

.right-container footer #next {
  background: #6d5acf;
  border: 1px solid transparent;
  color: #fff;
}

.right-container footer #next:hover {
  background: #503b99;
}

/* Add bold black color for labels */
.percentile label:not(.selected), 
.rank label:not(.selected), 
.university label:not(.selected), 
.gender label:not(.selected), 
.pwd label:not(.selected), 
.ews label:not(.selected), 
.category label:not(.selected), 
.sortby label:not(.selected) {
  color: #000;
  font-weight: bold;
}

/* Adjust the text color for input fields */
.right-container .rank input {
  color: #333; /* Dark gray color */
}

.radio-container input[type="radio"]:not(:checked) + label {
  background: #eee; /* Faint background color */
  border: 1px solid #ccc; /* Faint border color */
  color: #666; /* Faint text color */
}

.radio-container {
  background: #fff;
  border: 1px solid #ccc;
  border-radius: 4px;
  display: inline-block;
  padding: 5px;
}

.radio-container label {
  background: transparent;
  border: 1px solid transparent;
  border-radius: 2px;
  display: inline-block;
  height: 26px;
  line-height: 26px;
  margin: 0;
  padding: 0;
  text-align: center;
  transition: .3s all ease-in-out;
  width: 80px;
  cursor: pointer;
}

.radio-container input[type="radio"] {
  display: none;
}

.radio-container input[type="radio"]:checked + label {
  background: #6d5acf;
  border: 1px solid #ccc;
}

h3 {
  font-size: 16px;
  color: #333;
  align-self: center;
}

.made_with {
  font-size: 1.5em;
  text-align: center;
  color: #6d5acf;
  padding: 1px 0 1px 1px;
}

@media (max-width: 775px) {
  .signup-container {
    display: flex;
    flex-direction: column-reverse;
  }

  .right-container {
    width: 100%;
    max-width: 500px;
  }

  .left-container {
    height: auto;
    overflow: unset;
    max-width: 500px;
  }

  .left-container .puppy {
    position: relative;
  }

  .radio-container {
    display: flex;
  }

  .radio-container label {
    width: 50%;
  }
}

@media (max-width: 400px) {
  .right-container .set {
    display: flex;
    flex-direction: column;
    width: 100%;
    margin: 0;
  }

  .right-container .set>div {
    margin-bottom: 10px;
  }

  .right-container label, .right-container input, .right-container .radio-container, .right-container select {
    width: 100%;
    margin: 0;
  }

  .right-container footer {
    margin: 20px 12px;
    padding: 0;
  }

  .right-container footer #next {
    border-radius: 0;
  }

  footer {
    margin-right: 1em;
    margin-left: 1em;
    border-radius: 4px 4px 0 0;
  }
}
