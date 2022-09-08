function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 23.897, lng: 121.543},
    zoom: 17
    });
    
    var markers = new Array();

    downloadData("/poi/", function(request) {
        var data = JSON.parse(request.responseText);
        
        Array.prototype.forEach.call(data, function(element) {
            var position = {
                lat: element.latitude,
                lng: element.longitude,
            };
            var marker = new google.maps.Marker({
                position: position,
            });

            var infowindow = new google.maps.InfoWindow();
            var img = document.createElement('img');
            img.src = element.attachment;
            img.setAttribute('height', "200");
            var comment = document.createElement('p');
            comment.textContent = element.comment;
            var parentDiv = document.createElement('div');            

            parentDiv.appendChild(img);
            parentDiv.appendChild(comment);
            marker.addListener('click', function() {
                infowindow.setContent(parentDiv);
                infowindow.open(map, marker);
            })
            markers.push(marker);
        })
        
        markers.forEach(element => {
            return element.setMap(map);
        });
    })

    var filterControlDiv = document.createElement('div');
    var filterControl = new FilterControl(filterControlDiv, map, markers);
    map.controls[google.maps.ControlPosition.TOP_CENTER].push(filterControlDiv);
}

function downloadData(url, callback) {
    var request = new XMLHttpRequest();
    request.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            callback(request);
        }
    };
    request.open("GET", url, true);
    request.send();
}

function FilterControl(controlDiv, map, markers) {
    var controlUI = document.createElement('div');
    controlUI.style.backgroundColor = '#fff';
    controlUI.style.border = '2px solid #fff';
    controlUI.style.borderRadius = '3px';
    controlUI.style.boxShadow = '0 2px 6px rgba(0,0,0,.3)';
    controlUI.style.cursor = 'pointer';
    controlUI.style.marginBottom = '22px';
    controlUI.style.textAlign = 'center';
    controlDiv.appendChild(controlUI);

    var controlCheckBox1 = document.createElement('input');
    controlCheckBox1.type = 'checkbox'
    controlUI.appendChild(controlCheckBox1);

    var controlCheckBox2 = document.createElement('input');
    controlCheckBox2.type = 'checkbox'
    controlUI.appendChild(controlCheckBox2);

    var checkBox2Label = document.createElement('label');
    checkBox2Label.textContent = 'Show Tag2';
    controlUI.appendChild(checkBox2Label);

    controlCheckBox2.addEventListener('change', function() {
        if (this.checked) {
            markers.forEach(element => {
                if (element.hasTag2) {
                    element.setVisible(true);
                }
                else {
                    element.setVisible(false);
                }
            });
        }
        else {
            markers.forEach(element => element.setVisible(true));
        }
    });
}