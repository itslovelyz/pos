function validate() {
  document
    .getElementById("login-form")
    .addEventListener("submit", function (event) {
      event.preventDefault();
      // Get the username and password from the user.
      var username = document.getElementById("uname").value;
      var password = document.getElementById("psw").value;

      // Check if the username and password are correct.
      if (username === "I" && password === "pass1") {
        // Redirect the user to the first HTML page.
        window.location.href = "Inventory.html";
        return true;
      } else if (username === "DR" && password === "pass2") {
        // Redirect the user to the second HTML page.
        window.location.href = "Admin_DR.html";
        return true;
      } else if (username === "Admin" && password === "Admin") {
        // Redirect the user to the third HTML page.
        window.location.href = "Admin_main.html";
        return true;
      } else if (username === "Receive" && password === "pass3") {
        // Redirect the user to the third HTML page.
        window.location.href = "Receiving.html";
        return true;
      }
      // Display an error message.
      alert("Wrong Credentials");
      return false;
    });
}

validate();
