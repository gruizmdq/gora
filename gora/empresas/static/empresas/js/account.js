var message = ""
var len = 0
$(".new_password").on('keyup', this, function() {
    len = $("#new_password").val().length
    $(".password-len").text(len.toString() + "/8 caracteres mínimos")
    if (len >= 8){
        $(".password-len").css("display", "none")
        $("#new_password").removeClass("mb-2").addClass("mb-4")
    }
    else{
        $(".password-len").css("display", "block")
        $("#new_password").addClass("mb-2").removeClass("mb-4")
    }
    if ($("#new_password").val() == $("#new_password2").val()){
        $(".new_password").removeClass("input-error").addClass("input-success")
    }
    else{
        $(".new_password").addClass("input-error").removeClass("input-success")
        message = "Las nuevas contraseñas no coinciden"
    }
    console.log(message)
  });
