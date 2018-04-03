const applicationServerPublicKey = 'BPElgZJJOQ96Q70MPCKWth0Kh274NbBFNYoqCcHXo8X3VGw9mcUnGbC52-luDNWrSYKm14UHOqX7wsI6B4qZclc';
document.addEventListener('wheel', (evt) => {
    // ... do stuff with evt
  }, {
    capture: true,
    passive: true
  })
  function myFunction() {
    alert("Page is under construction!");
}
function validateForm(){
    var currentCity=document.getElementById("currentCity").value;
    var destinationCity=document.getElementById("destinationCity").value;
    //var currentCity=document.getElementById("currentCity").value;
    if (currentCity =='' | destinationCity==''){
        console.log("Please enter city");
        return false;
    }
    document.getElementById('buslist').style.display=block;
    // document.getElementById('container').style.height='auto';
    // alert("done");
}


function butRefresh(){
    location.reload();

}
var x;
function openNav() {
    console.log(x);
    if (x=="open" | x==undefined){
    document.getElementById("mySidenav").style.width = "250px";
    x="close";
    document.getElementById("nav").innerHTML="&times;";
    document.getElementById("Bus_title").style.marginLeft="6.28px";
    console.log(x);
    return x;
}
    else{
        document.getElementById("mySidenav").style.width="0";
        document.getElementById("Bus_title").style.marginLeft="0px";
        x="open";
        document.getElementById("nav").innerHTML="&#9776;";
        
    }
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}
Notification.requestPermission(function(status) {
    console.log('Notification permission status:', status);
});
function displayNotification() {
    if (Notification.permission == 'granted') {
      navigator.serviceWorker.getRegistration().then(function(reg) {
        reg.showNotification('Hello world!');
      });
    }
  }

window.addEventListener('load', async e =>{
    if('serviceWorker' in navigator){
        try{
            
            navigator.serviceWorker.register('/service-worker.js');
            console.log('Service Worker Registered!');
        }
        catch(error){
            console.log('Error with service worker');
        }
    }

});


function initMap() {
    var directionsService = new google.maps.DirectionsService;
    var directionsDisplay = new google.maps.DirectionsRenderer;
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 7,
      center: {lat: 28.6468931, lng: 76.9528361}
    });
    directionsDisplay.setMap(map);

    var onChangeHandler = function() {
      calculateAndDisplayRoute(directionsService, directionsDisplay);
    };
    document.getElementById('start').addEventListener('change', onChangeHandler);
    document.getElementById('end').addEventListener('change', onChangeHandler);
  }
  var start = '28.6468931,76.9528361';
  var end = '27.176157,77.9098013';
  function calculateAndDisplayRoute(directionsService, directionsDisplay) {
    directionsService.route({
      origin: start,
      destination: end,
      travelMode: 'DRIVING'
    }, function(response, status) {
      if (status === 'OK') {
        directionsDisplay.setDirections(response);
      } else {
        window.alert('Directions request failed due to ' + status);
      }
    });
  }
