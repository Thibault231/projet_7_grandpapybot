function gif_loader() {
    var question = document.getElementsById('text-question').value;
    var li = document.createElement('li');
    li.innerHTML = question;
    document.getElementById('history_list').appendChild(li);
}


var lat_ans = 0.0000;
var lng_ans = 0.0000;

function initMap(lat_ans lng_ans) {
    var latlng = {lat: lat_ans, lng: lng_ans};
    var markername = "C'est ici mon petit";
    var map = new google.maps.Map($('#map'), {
    center: latlng, zoom: 17});
    var marker = new google.maps.Marker({
        position: latlng, map: map, title: markername
    });
}

function ajaxPost(url, data, callback){
    var req = new XMLHttpRequest();
    req.open("POST", url);
    req.addEventListener("load", function () {
        if (req.status >= 200 && req.status < 400) {
            callback(req.responseText);
        } else {
            console.error(req.status + " " + req.statusText + " " + url);
        }
    });
    req.addEventListener("error", function () {
        console.error("Erreur réseau avec l'URL " + url);
    });
    req.send(data);
}

function api_call(){
    var question = document.getElementsById('text-question').value;
    var form = document.querySelector("form");
    form.addEventListener("submit", function (e) {
        e.preventDefault();

        var data = new FormData();
       
        data.append("text-question", question);

        ajaxPost("/api/all", data, function (response) {
            var answers = JSON.parse(reponse);
            document.getElementsById('loading').classList.toggle("d-inline");
            alert('Tout est ok aussi');
        });
    });
}
