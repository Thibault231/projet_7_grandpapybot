function initMap() {
    var latlng = {lat: 48.8748465, lng: 2.3504873};
    var markername = "ici";
    var map = new google.maps.Map(document.getElementById('map'), {
    center: latlng,
    zoom: 17
    });
    var marker = new google.maps.Marker({
        position: latlng,
        map: map,
        title: markername
    });
}

jQuery(document).ready(function() {
    initMap();
    $("#question").on("click", "#validate", function(){
        $("#loading").css("display", "block");
        var question = $("#papyquestion").val();
        $(".HistoryBox").append(question + '</br>');
        $(".MyQuestion")[0].reset();
        $("#loading").css("display", "none");
        $(".ExactAnswer").css("display", "block"); 
        $(".MapGoogle").css("display", "block"); 
        $(".AdditionalAnswer").css("display", "block");
    }); 

 });