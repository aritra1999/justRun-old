ace.require("ace/ext/language_tools");
var editor = ace.edit("editor");

editor.setOptions({
    enableBasicAutocompletion: true,
    enableSnippets: true,
    enableLiveAutocompletion: true,
});


editor.setTheme("ace/theme/monokai");
editor.session.setMode("ace/mode/c_cpp");
editor.setFontSize(16);


editor.setOptions({
    enableBasicAutocompletion: true,
    enableSnippets: true,
    enableLiveAutocompletion: true,
});

editor.clearSelection();

function startup() {
    let code = localStorage.getItem("code");
    let language = localStorage.getItem("language");
    let input = localStorage.getItem("input")

    if (code != null) {
        editor.setValue(code)
        editor.session.setMode("ace/mode/" + get_ext(language))
        document.getElementById("input").innerHTML = input;
        document.getElementById("language").value = language;

    } else {
        fetch("static/code-template/template.cpp")
            .then(response => response.text())
            .then(
                data => {
                    editor.setValue(data);
                    editor.clearSelection();
                });
    }
}

function download(){
    var mimeType = document.getElementById('language').value;
    if(mimeType === "python"){
        mimeType = "py";
    }

    var filename = "code." + mimeType;
    var elHtml = editor.getSession().getValue();
    var link = document.createElement('a');
    mimeType = mimeType || 'text/plain';

    link.setAttribute('download', filename);
    link.setAttribute('href', 'data:' + mimeType  +  ';charset=utf-8,' + encodeURIComponent(elHtml));
    link.click();
}


function get_ext(lang) {
    if (lang === "c" || lang === "cpp") return "c_cpp";
    else return lang;
}

function changeLang(language) {
    fetch("static/code-template/template." + language.value)
        .then(response => response.text())
        .then(
            data => {
                editor.setValue(data);
                editor.clearSelection();
            });

    editor.session.setMode("ace/mode/" + get_ext(language.value));

}

function changeTheme(theme) {
    editor.setTheme("ace/theme/" + theme.value);
}

function submit() {
    $("#processing").css({"display": "block"});
    $('#output').empty();

    var code = editor.getSession().getValue();
    var language = get_ext(document.getElementById('language').value);
    var input = document.getElementById('input').value;
    var csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value;

    localStorage.setItem("code", code);
    localStorage.setItem("language", document.getElementById('language').value);
    localStorage.setItem("input", input);

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
        .done(function (data, statuyouts) {
            document.getElementById('output').innerText = data.output;
            if (data.verdict === "success") {
                $('#message_success').text(data.message);
                $("#success").css({"display": "block"});
                $('#time').text("Time taken: " + data.time + " s. ");
                $('#mem').text("Memory used: " + data.memory + " MB.");
            } else {
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
}