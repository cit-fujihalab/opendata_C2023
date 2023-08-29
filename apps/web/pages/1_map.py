import streamlit.components.v1 as components

components.html("""
<html>
<head>
    
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    
        <script>
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        </script>
    
    <style>html, body {width: 100%;height: 100%;margin: 0;padding: 0;}</style>
    <style>#map {position:absolute;top:0;bottom:0;right:0;left:0;}</style>
    <script src="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js"></script>
    <script src="https://code.jquery.com/jquery-1.12.4.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css"/>
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css"/>
    
            <meta name="viewport" content="width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
            <style>
                #map_cb4b9187b0f1ee418263439a4cb3ef96 {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
                .leaflet-container { font-size: 1rem; }
            </style>
        
</head>
<body>
    
    
            <div class="folium-map" id="map_cb4b9187b0f1ee418263439a4cb3ef96" ></div>
        
</body>
<script>
    
    
            var map_cb4b9187b0f1ee418263439a4cb3ef96 = L.map(
                "map_cb4b9187b0f1ee418263439a4cb3ef96",
                {
                    center: [43.22878388888889, 141.83041465],
                    crs: L.CRS.EPSG3857,
                    zoom: 14,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );

            

        
    
            var tile_layer_6c90ac81fcb2892f165e27d348c20a0c = L.tileLayer(
                "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                {"attribution": "Data by &copy; <a target=\\"_blank\\" href=\\"http://openstreetmap.org> OpenStreetMap</a>, under <a target=\\"_blank\\" href=\\"http://www.openstreetmap.org/copyright\\">ODbL</a>.", "detectRetina": false, "maxNativeZoom": 18, "maxZoom": 18, "minZoom": 0, "noWrap": false, "opacity": 1, "subdomains": "abc", "tms": false}
            ).addTo(map_cb4b9187b0f1ee418263439a4cb3ef96);
        
    
            var marker_cd4f11d46eafb5acef0a9cc969b23af0 = L.marker(
                [43.22878388888889, 141.83041465],
                {}
            ).addTo(map_cb4b9187b0f1ee418263439a4cb3ef96);
        
    
        var popup_b40f62ae6f747af1ab86adccc7074b08 = L.popup({"maxWidth": "100%"});

        
            
                var html_549b26efc9e96c78824db7bb8c7d5def = $(`<div id="html_549b26efc9e96c78824db7bb8c7d5def" style="width: 100.0%; height: 100.0%;"><span style="white-space: nowrap;">東京タワー</span></div>`)[0];
                popup_b40f62ae6f747af1ab86adccc7074b08.setContent(html_549b26efc9e96c78824db7bb8c7d5def);
            
        

        marker_cd4f11d46eafb5acef0a9cc969b23af0.bindPopup(popup_b40f62ae6f747af1ab86adccc7074b08)
        ;

        
    
    
            marker_cd4f11d46eafb5acef0a9cc969b23af0.bindTooltip(
                `<div>
                     クリック！
                 </div>`,
                {"sticky": true}
            );
        
</script>
</html>
""", height=700, width=900)
