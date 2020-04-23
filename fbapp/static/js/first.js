function initMap(lat,lon) {
    var map = null;
    map = new google.maps.Map(document.getElementById("map"), {
        center: new google.maps.LatLng(lat, lon), 
        zoom: 17, 
        mapTypeId: google.maps.MapTypeId.ROADMAP, 
        mapTypeControl: true,
        scrollwheel: true, 
        mapTypeControlOptions: {
            style: google.maps.MapTypeControlStyle.HORIZONTAL_BAR 
        },
        navigationControl: true, 
        navigationControlOptions: {
            style: google.maps.NavigationControlStyle.ZOOM_PAN 
        }
    });
    var marker = new google.maps.Marker({
        position: {lat: lat, lng: lon},
        map: map
    });
}

$(document).ready(function(){ 
      $('#my-question').submit(function(event){
                  event.preventDefault();
                  
                  $(".d-none").removeClass('d-none');
                  
                  var quest = $('#text-question').val();
                  $("#history_list").append($("<li>").text(quest));

                  $.post( "/api/all", {question: quest}, function(data){
                  var resp = $.parseJSON(data);
                  var summary_ans = $("#summary_ans");

                  if (resp.success){
                              summary_ans.html( resp.summary );
                              $("#url_ans").prop("href", resp.url);
                              $("#adress_ans" ).text( resp.adress_ans );
                              lat = resp.lat_ans;
                              lon = resp.lng_ans;
                              initMap(lat, lon);
                              $("#h2_answer").text( "Grandpapy a trouvé une réponse!" );
                              $(".h2").removeClass('text-warning').addClass('text-success');   
                              
                  } else {
                              $("#summary_ans" ).text( "Non, je plaisante, je n'ai pas grandi làbas." );
                              $("#url_ans").prop("href", "https://fr.wikipedia.org/wiki/Lune");
                              $("#adress_ans" ).text( "Nulpart sur Terre.<br/>Mais tu peux regarder sur la Lune!" );
                              var lat = 28.488677;
                              var lon = -80.5750128;
                              initMap(lat, lon);
                              $("#h2_answer").text("Grandpapy n'a pas trouvé de réponse!" );
                              $(".h2").removeClass('text-success').addClass('text-warning');        
                  }
                  $("#loading").addClass('d-none');
                  });
      });
})