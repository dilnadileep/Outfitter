$(document).ready(function () {

    const fields = [

        { id: "#fname", validate: validatefName },
        { id: "#lname", validate: validatesName },
        { id: "#email", validate: validateEmail },
        { id: "#password", validate: validatePassword },
        { id: "#confirm_password", validate: validateConfirmPassword }
    ];

    fields.forEach(field => {
        $(field.id).keyup(function () {
            field.validate();
        });

        validateFieldOnBlur(field.id, field.validate);
    });
    function checkFormValidity() {
        const isValid = fields.every(field => {
            const $field = $(field.id);
            const $errorSpan = $(`${field.id}span`);

            return $field.val().trim() !== "" && $errorSpan.html() === "";
        });

        $("#submitBtn").prop("disabled", !isValid);
    }



    function validateFieldOnBlur(fieldId, validationFunction) {
        $(fieldId).blur(function () {
            validationFunction();
            checkFormValidity();
        });
    }

    // Form submission
    $("#form").submit(function (event) {
        if (!$("#submitBtn").prop("disabled")) {
            // Form is valid, allow submission
            return true;
        } else {
            // Form is not valid, prevent submission
            event.preventDefault();
            return false;
        }
    });

    // Initial check for form validity
    checkFormValidity();


    function validatefName() {
        const name = $("#fname").val();
        const lettersWithSpaces = /^[A-Za-z\s]+$/;
        if (name.trim() === "") {
            $("#fnamespan").html("Enter the First Name").css("color", "#41586B");
        } else if (!lettersWithSpaces.test(name)) {
            $("#fnamespan").html("First Name field required only alphabet characters with spaces").css("color", "#41586B");
        } else {
            $("#fnamespan").html("");
        }
    }

    function validatesName() {
        const name = $("#lname").val();
        const lettersWithSpaces = /^[A-Za-z\s]+$/;
        if (name.trim() === "") {
            $("#lnamespan").html("Enter the Last Name").css("color", "#41586B");
        } else if (!lettersWithSpaces.test(name)) {
            $("#lnamespan").html("Last Name field required only alphabet characters with spaces").css("color", "#41586B");
        } else {
            $("#lnamespan").html("");
        }
    }


    function validateEmail() {
        const email = $("#email").val();
        const filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
        if (email === "") {
            $("#emailspan").html("Enter the Email Id").css("color", "#41586B");
        } else if (!filter.test(email)) {
            $("#emailspan").html("Use correct Email Id").css("color", "#41586B");
        } else {
            $("#emailspan").html("");
        }
    }



    function validatePassword() {
        const password = $("#password").val();
        const passwordSpan = $("#passwordspan");

        if (password.trim() === "") {
            passwordSpan.html("Password is required").css("color", "#FF0000"); // Red color for error
        } else if (password.length < 8) {
            passwordSpan.html("Password must be at least 8 characters long").css("color", "#FF0000");
        } else if (!/[A-Z]/.test(password)) {
            passwordSpan.html("Password must contain at least one uppercase letter").css("color", "#FF0000");
        } else if (!/[a-z]/.test(password)) {
            passwordSpan.html("Password must contain at least one lowercase letter").css("color", "#FF0000");
        } else if (!/[0-9]/.test(password)) {
            passwordSpan.html("Password must contain at least one digit").css("color", "#FF0000");
        } else if (!/[#?!@$%^&*-]/.test(password)) {
            passwordSpan.html("Password must contain at least one special character").css("color", "#FF0000");
        } else {
            passwordSpan.html(""); // Clear the error message
        }
    }


    function validateConfirmPassword() {
        const password = $("#password").val();
        const confirmPassword = $("#confirm_password").val();
        if (confirmPassword === "") {
            $("#confirm_passwordspan").html("Enter the Confirm Password").css("color", "#41586B");
        } else if (confirmPassword !== password) {
            $("#confirm_passwordspan").html("Password do not match").css("color", "#41586B");
        } else {
            $("#confirm_passwordspan").html("");
        }
    }
});