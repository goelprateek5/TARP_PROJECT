document.addEventListener('wheel', (evt) => {
    // ... do stuff with evt
  }, {
    capture: true,
    passive: true
  })
function validateForm(){
    var currentCity=document.getElementById("currentCity").value;
    var destinationCity=document.getElementById("destinationCity").value;
    //var currentCity=document.getElementById("currentCity").value;
    if (currentCity =='' | destinationCity==''){
        console.log("Please enter city");
        return false;
    }

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
    console.log(x);
    return x;
}
    else{
        document.getElementById("mySidenav").style.width="0";
        x="open";
        document.getElementById("nav").innerHTML="&#9776;";
    }
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}
function displayNotification() {
    if (Notification.permission == 'granted') {
      navigator.serviceWorker.getRegistration().then(function(reg) {
        reg.showNotification('Hello world!');
      });
    }
  }
//Notification.requestPermission(function(status) {
//    console.log('Notification permission status:', status);
//});
window.addEventListener('load', async e =>{
    if('serviceWorker' in navigator){
        try{
            navigator.serviceWorker.register('sw.js');
            console.log('Service Worker Registered!');
        }
        catch(error){
            console.log('Error with service worker');
        }
    }

});