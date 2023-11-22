// function initMap() {
//   var map = new google.maps.Map(document.getElementById("map"), {
//     center: {
//       lat: 0,
//       lng: 0,
//     },
//     zoom: 10,
//   });

//   if (navigator.geolocation) {
//     navigator.geolocation.getCurrentPosition(
//       function (position) {
//         var userLatLng = {
//           lat: position.coords.latitude,
//           lng: position.coords.longitude,
//         };
//         map.setCenter(userLatLng);
//       },
//       function () {
//         handleLocationError(true, map.getCenter());
//       }
//     );
//   } else {
//     handleLocationError(false, map.getCenter());
//   }

//   function handleLocationError(browserHasGeolocation, pos) {
//     var infoWindow = new google.maps.InfoWindow();
//     infoWindow.setPosition(pos);
//     infoWindow.setContent(
//       browserHasGeolocation
//         ? "Error: The Geolocation service failed."
//         : "Error: Your browser doesn't support geolocation."
//     );
//     infoWindow.open(map);
//   }

//   var locations = [
//             {% for location in locations %}
//             {
//                 "name": "{{ supportlocations.name }}",
//                 "lat": {{ supportlocations.latitude }},
//                 "lng": {{ supportlocations.longitude }},
//                 "contact_number": {{ supportlocations.contact_number }},
//                 "contact_email": {{ supportlocations.contact_email }},
//             },
//             {% endfor %}
//         ];

//         for (var i = 0; i < events.length; i++) {
//             createMarker(events[i]);
//         }

//         function createMarker(event) {
//             var marker = new google.maps.Marker({
//                 position: {
//                     lat: event.lat,
//                     lng: event.lng
//                 },
//                 map: map,
//                 title: event.title
//             });

//             var infowindow = new google.maps.InfoWindow({
//                 content: `<div>
//                     <h2>${supportlocations.name}</h2>
//                     <p>Tel: ${supportlocations.contact_number}</p>
//                     <p>Email:: ${supportlocations.contact_email}</p>
//                 </div>`
//             });

//             marker.addListener('click', function () {
//                 infowindow.open(map, marker);
//             });
//         }









}
