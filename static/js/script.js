ace.require("ace/ext/language_tools");
var editor = ace.edit("editor");

editor.setOptions({
    enableBasicAutocompletion: true,
    enableSnippets: true,
    enableLiveAutocompletion: true,
});


editor.setTheme("ace/theme/monokai");
editor.session.setMode("ace/mode/c_cpp");
editor.setFontSize(15);


editor.setOptions({
    enableBasicAutocompletion: true,
    enableSnippets: true,
    enableLiveAutocompletion: true,
});

function startup() {
    console.log("Starting Editor");
}

function changeLang(language) {
    editor.session.setMode("ace/mode/" + language.value);
}

function changeTheme(theme) {
    editor.setTheme("ace/theme/" + theme.value);
}

function submit() {

    $("#run").prop("disabled", true);
    $("#processing").css({"display": "block"});
    $('#output').empty();

    var code = editor.getSession().getValue();
    var language = document.getElementById('language').value;
    var input = document.getElementById('input').value;
    var csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value;


    $.ajax({
        method: 'POST',
        url: '/run/',
        data: {
            language: language,
            code: code,
            input: input,
            csrfmiddlewaretoken: csrf,
        }
    })
        .done(function (data, status) {
            $('#output').text(data.output);
            if(data.verdict === "success"){
                $('#message_success').text(data.message);
                $("#success").css({"display": "block"});
                $('#time').text("Time taken: " + data.time + " s. ");
                $('#mem').text("Memory used: " + data.time + " KB.");
            }else{
                $('#message_error').text(data.message);
                $("#error").css({"display": "block"});
            }

            $("#processing").css({"display": "none"});
        })
        .fail(function (data, status) {
            $('#message_error').text(data.message);
            $("#error").css({"display": "block"});
            $("#processing").css({"display": "none"});
        });

    $("#run").prop("disabled", false);
}