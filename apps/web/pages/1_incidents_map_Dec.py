import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="事故発生地点(北海道)")

components.html(
"""
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
                #map_235d4c48bc5742b79af7cea034cebbef {
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
    
    
            <div class="folium-map" id="map_235d4c48bc5742b79af7cea034cebbef" ></div>
        
</body>
<script>
    
    
            var map_235d4c48bc5742b79af7cea034cebbef = L.map(
                "map_235d4c48bc5742b79af7cea034cebbef",
                {
                    center: [36.6408, 138.8233],
                    crs: L.CRS.EPSG3857,
                    zoom: 5,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );

            

        
    
            var tile_layer_b7588dd89092c9fce65f514eed7f8cef = L.tileLayer(
                "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                {"attribution": "Data by \u0026copy; \u003ca target=\"_blank\" href=\"http://openstreetmap.org\"\u003eOpenStreetMap\u003c/a\u003e, under \u003ca target=\"_blank\" href=\"http://www.openstreetmap.org/copyright\"\u003eODbL\u003c/a\u003e.", "detectRetina": false, "maxNativeZoom": 18, "maxZoom": 18, "minZoom": 0, "noWrap": false, "opacity": 1, "subdomains": "abc", "tms": false}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var marker_44f55f3f501872e4f9c11b78a0d65281 = L.marker(
                [42.84677138888889, 141.5803488888889],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_abc2e27fa9adb20dea306dbf6eaff9d9 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#ffffff", "markerColor": "red", "prefix": "glyphicon"}
            );
            marker_44f55f3f501872e4f9c11b78a0d65281.setIcon(icon_abc2e27fa9adb20dea306dbf6eaff9d9);
        
    
        var popup_9f38027f5b048281d82bd6b82642e006 = L.popup({"maxWidth": 200});

        
            
                var html_f94c16556f64d0a7a482d4ba658a2d11 = $(`<div id="html_f94c16556f64d0a7a482d4ba658a2d11" style="width: 100.0%; height: 100.0%;">事故1月29日10時頃発生 .                 天気：雪 &#x2744;(雪、みぞれ、ひょうが降っている状態をいう。)</div>`)[0];
                popup_9f38027f5b048281d82bd6b82642e006.setContent(html_f94c16556f64d0a7a482d4ba658a2d11);
            
        

        marker_44f55f3f501872e4f9c11b78a0d65281.bindPopup(popup_9f38027f5b048281d82bd6b82642e006)
        ;

        
    
    
            var marker_9349dc98190f9a3e9317fc5830469485 = L.marker(
                [43.10087861111111, 141.38555833333334],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_9e34b39076659a0a42240416bae629c5 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#ffffff", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_9349dc98190f9a3e9317fc5830469485.setIcon(icon_9e34b39076659a0a42240416bae629c5);
        
    
        var popup_82b725d1364a310bce6ea127571f59f6 = L.popup({"maxWidth": 200});

        
            
                var html_6c86067c7100caeec08faaa66cda45fc = $(`<div id="html_6c86067c7100caeec08faaa66cda45fc" style="width: 100.0%; height: 100.0%;">事故2月8日8時頃発生 .                 天気：雪 &#x2744;(雪、みぞれ、ひょうが降っている状態をいう。)</div>`)[0];
                popup_82b725d1364a310bce6ea127571f59f6.setContent(html_6c86067c7100caeec08faaa66cda45fc);
            
        

        marker_9349dc98190f9a3e9317fc5830469485.bindPopup(popup_82b725d1364a310bce6ea127571f59f6)
        ;

        
    
    
            var marker_4eb6083f4c2d4348a8ca6052d9ba2b78 = L.marker(
                [42.67661388888889, 141.6437361111111],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_1756b3e8fc07a9b88426eb04b8125240 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#000000", "markerColor": "red", "prefix": "glyphicon"}
            );
            marker_4eb6083f4c2d4348a8ca6052d9ba2b78.setIcon(icon_1756b3e8fc07a9b88426eb04b8125240);
        
    
        var popup_4f602552d18b0d3d47f074ad211e209b = L.popup({"maxWidth": 200});

        
            
                var html_50d13301a57ab0db4a8a4f9b1bf5dd00 = $(`<div id="html_50d13301a57ab0db4a8a4f9b1bf5dd00" style="width: 100.0%; height: 100.0%;">事故2月18日19時頃発生 .                 天気：雪 &#x2744;(雪、みぞれ、ひょうが降っている状態をいう。)</div>`)[0];
                popup_4f602552d18b0d3d47f074ad211e209b.setContent(html_50d13301a57ab0db4a8a4f9b1bf5dd00);
            
        

        marker_4eb6083f4c2d4348a8ca6052d9ba2b78.bindPopup(popup_4f602552d18b0d3d47f074ad211e209b)
        ;

        
    
    
            var marker_d8e859ec70d024d536ed31c849b77afe = L.marker(
                [42.8435475, 141.59062444444444],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_4d8edd5fa7d632e7fdf6665712a49397 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#ffa500", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_d8e859ec70d024d536ed31c849b77afe.setIcon(icon_4d8edd5fa7d632e7fdf6665712a49397);
        
    
        var popup_0412012e77b516cd08cb7637b0fb0fc1 = L.popup({"maxWidth": 200});

        
            
                var html_1ab95bec09da914094032648eba0942f = $(`<div id="html_1ab95bec09da914094032648eba0942f" style="width: 100.0%; height: 100.0%;">事故2月28日16時頃発生 .                 天気：晴 &#x2600;(雲量がおおむね80％以下の状態で、他の天候に該当しないものをいう。)</div>`)[0];
                popup_0412012e77b516cd08cb7637b0fb0fc1.setContent(html_1ab95bec09da914094032648eba0942f);
            
        

        marker_d8e859ec70d024d536ed31c849b77afe.bindPopup(popup_0412012e77b516cd08cb7637b0fb0fc1)
        ;

        
    
    
            var marker_8b93fc0858ca7cd3f8122bff5b7d2c2f = L.marker(
                [42.90718722222223, 142.01014083333334],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_c2cdb5a00c8388d14fa2baa95fb0cdc0 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#ffffff", "markerColor": "red", "prefix": "glyphicon"}
            );
            marker_8b93fc0858ca7cd3f8122bff5b7d2c2f.setIcon(icon_c2cdb5a00c8388d14fa2baa95fb0cdc0);
        
    
        var popup_c30cb2baf4fe7470018228419c4ac620 = L.popup({"maxWidth": 200});

        
            
                var html_1b7f9f0c65591e38e0c61cd59cd9f513 = $(`<div id="html_1b7f9f0c65591e38e0c61cd59cd9f513" style="width: 100.0%; height: 100.0%;">事故2月19日12時頃発生 .                 天気：曇 &#x2601;(雲量がおおむね80％以上の状態で、他の天候に該当しないものをいう。)</div>`)[0];
                popup_c30cb2baf4fe7470018228419c4ac620.setContent(html_1b7f9f0c65591e38e0c61cd59cd9f513);
            
        

        marker_8b93fc0858ca7cd3f8122bff5b7d2c2f.bindPopup(popup_c30cb2baf4fe7470018228419c4ac620)
        ;

        
    
    
            var marker_107ddb39ab9c6d4fa76dd2a920d0e7f4 = L.marker(
                [42.85357694444445, 141.59852194444446],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_8771196f28681be4023c762ed7af04d3 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#ffffff", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_107ddb39ab9c6d4fa76dd2a920d0e7f4.setIcon(icon_8771196f28681be4023c762ed7af04d3);
        
    
        var popup_e00eb9c381eb115e69080d338273da42 = L.popup({"maxWidth": 200});

        
            
                var html_0ec80e23921bfa548659e7544c044ea3 = $(`<div id="html_0ec80e23921bfa548659e7544c044ea3" style="width: 100.0%; height: 100.0%;">事故3月19日15時頃発生 .                 天気：晴 &#x2600;(雲量がおおむね80％以下の状態で、他の天候に該当しないものをいう。)</div>`)[0];
                popup_e00eb9c381eb115e69080d338273da42.setContent(html_0ec80e23921bfa548659e7544c044ea3);
            
        

        marker_107ddb39ab9c6d4fa76dd2a920d0e7f4.bindPopup(popup_e00eb9c381eb115e69080d338273da42)
        ;

        
    
    
            var marker_cfe05453999ca98dbac79934cb563869 = L.marker(
                [43.06169472222222, 141.42410916666668],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_3ae92372dcdec613f0d99395dcc09538 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#ffffff", "markerColor": "red", "prefix": "glyphicon"}
            );
            marker_cfe05453999ca98dbac79934cb563869.setIcon(icon_3ae92372dcdec613f0d99395dcc09538);
        
    
        var popup_a4c2b53de5934454144e4bd0a0c4a934 = L.popup({"maxWidth": 200});

        
            
                var html_a93ae75ac30f3fc4afc3a1b61214ebbf = $(`<div id="html_a93ae75ac30f3fc4afc3a1b61214ebbf" style="width: 100.0%; height: 100.0%;">事故3月24日16時頃発生 .                 天気：晴 &#x2600;(雲量がおおむね80％以下の状態で、他の天候に該当しないものをいう。)</div>`)[0];
                popup_a4c2b53de5934454144e4bd0a0c4a934.setContent(html_a93ae75ac30f3fc4afc3a1b61214ebbf);
            
        

        marker_cfe05453999ca98dbac79934cb563869.bindPopup(popup_a4c2b53de5934454144e4bd0a0c4a934)
        ;

        
    
    
            var marker_db2277599b0998f0c5597270846933d4 = L.marker(
                [43.374097222222225, 141.8874425],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_ebc3cbeb0c38467f578a2099f86f61d0 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#ffffff", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_db2277599b0998f0c5597270846933d4.setIcon(icon_ebc3cbeb0c38467f578a2099f86f61d0);
        
    
        var popup_5e71ec51fbfd60d630df1ba096b0ebe3 = L.popup({"maxWidth": 200});

        
            
                var html_0ed85145532b8534dda9afa72fc3f5ed = $(`<div id="html_0ed85145532b8534dda9afa72fc3f5ed" style="width: 100.0%; height: 100.0%;">事故4月17日16時頃発生 .                 天気：雨 &#x1f327;(雨が降っている状態をいう。)</div>`)[0];
                popup_5e71ec51fbfd60d630df1ba096b0ebe3.setContent(html_0ed85145532b8534dda9afa72fc3f5ed);
            
        

        marker_db2277599b0998f0c5597270846933d4.bindPopup(popup_5e71ec51fbfd60d630df1ba096b0ebe3)
        ;

        
    
    
            var marker_8110d23fab1970d0ea625f2217b5a6d1 = L.marker(
                [42.782988333333336, 141.6264277777778],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_617d07c70ecfa26a248fcab5769a0f19 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#0000ff", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_8110d23fab1970d0ea625f2217b5a6d1.setIcon(icon_617d07c70ecfa26a248fcab5769a0f19);
        
    
        var popup_b879261a6349c02b099867f7297ee4d8 = L.popup({"maxWidth": 200});

        
            
                var html_25a6eca1a19ff4cbbb27423a09de1027 = $(`<div id="html_25a6eca1a19ff4cbbb27423a09de1027" style="width: 100.0%; height: 100.0%;">事故4月4日18時頃発生 .                 天気：雨 &#x1f327;(雨が降っている状態をいう。)</div>`)[0];
                popup_b879261a6349c02b099867f7297ee4d8.setContent(html_25a6eca1a19ff4cbbb27423a09de1027);
            
        

        marker_8110d23fab1970d0ea625f2217b5a6d1.bindPopup(popup_b879261a6349c02b099867f7297ee4d8)
        ;

        
    
    
            var marker_897581f98bacae20a86ddfdcaa5aa2ba = L.marker(
                [43.103645, 141.59773083333334],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_32f26b22f38aea9748adc3e6839c207c = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#ffffff", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_897581f98bacae20a86ddfdcaa5aa2ba.setIcon(icon_32f26b22f38aea9748adc3e6839c207c);
        
    
        var popup_87b0a4590e804f44f5d3c216aa278bc6 = L.popup({"maxWidth": 200});

        
            
                var html_a68d543e2216515a22ab147344254e94 = $(`<div id="html_a68d543e2216515a22ab147344254e94" style="width: 100.0%; height: 100.0%;">事故4月18日15時頃発生 .                 天気：雨 &#x1f327;(雨が降っている状態をいう。)</div>`)[0];
                popup_87b0a4590e804f44f5d3c216aa278bc6.setContent(html_a68d543e2216515a22ab147344254e94);
            
        

        marker_897581f98bacae20a86ddfdcaa5aa2ba.bindPopup(popup_87b0a4590e804f44f5d3c216aa278bc6)
        ;

        
    
    
            var marker_8495afacead27267b14bfb260d56a8f0 = L.marker(
                [42.614718333333336, 141.46737944444445],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_18c6c88a79053755f33aac3b28cfcf01 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#ffffff", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_8495afacead27267b14bfb260d56a8f0.setIcon(icon_18c6c88a79053755f33aac3b28cfcf01);
        
    
        var popup_f57aa5280f6073beb1e7d647e3eaebef = L.popup({"maxWidth": 200});

        
            
                var html_ae67af889167d55d39b8b1491190d26d = $(`<div id="html_ae67af889167d55d39b8b1491190d26d" style="width: 100.0%; height: 100.0%;">事故5月12日7時頃発生 .                 天気：晴 &#x2600;(雲量がおおむね80％以下の状態で、他の天候に該当しないものをいう。)</div>`)[0];
                popup_f57aa5280f6073beb1e7d647e3eaebef.setContent(html_ae67af889167d55d39b8b1491190d26d);
            
        

        marker_8495afacead27267b14bfb260d56a8f0.bindPopup(popup_f57aa5280f6073beb1e7d647e3eaebef)
        ;

        
    
    
            var marker_58f23cb4aee1d34ec26d1ee30c917a55 = L.marker(
                [43.04070027777778, 141.43856694444446],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_7e945e2760cff0a3cb889a406a690ba2 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#ffffff", "markerColor": "red", "prefix": "glyphicon"}
            );
            marker_58f23cb4aee1d34ec26d1ee30c917a55.setIcon(icon_7e945e2760cff0a3cb889a406a690ba2);
        
    
        var popup_6943168e556249a34e4ce0b6b8bdf0a2 = L.popup({"maxWidth": 200});

        
            
                var html_d4f4fdf9cbd99c5836e1eb7dbb2611d4 = $(`<div id="html_d4f4fdf9cbd99c5836e1eb7dbb2611d4" style="width: 100.0%; height: 100.0%;">事故5月15日14時頃発生 .                 天気：曇 &#x2601;(雲量がおおむね80％以上の状態で、他の天候に該当しないものをいう。)</div>`)[0];
                popup_6943168e556249a34e4ce0b6b8bdf0a2.setContent(html_d4f4fdf9cbd99c5836e1eb7dbb2611d4);
            
        

        marker_58f23cb4aee1d34ec26d1ee30c917a55.bindPopup(popup_6943168e556249a34e4ce0b6b8bdf0a2)
        ;

        
    
    
            var marker_9ed7f425ec08a85a846f724ad55ffafe = L.marker(
                [43.07445805555555, 141.42120333333332],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_faa42e8cd1ad80340927663b7f585637 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#ffffff", "markerColor": "red", "prefix": "glyphicon"}
            );
            marker_9ed7f425ec08a85a846f724ad55ffafe.setIcon(icon_faa42e8cd1ad80340927663b7f585637);
        
    
        var popup_d2be23ee403236e096e0a96f9c93b45e = L.popup({"maxWidth": 200});

        
            
                var html_6d946c946a4b356511b4b13e17c724fa = $(`<div id="html_6d946c946a4b356511b4b13e17c724fa" style="width: 100.0%; height: 100.0%;">事故5月5日9時頃発生 .                 天気：曇 &#x2601;(雲量がおおむね80％以上の状態で、他の天候に該当しないものをいう。)</div>`)[0];
                popup_d2be23ee403236e096e0a96f9c93b45e.setContent(html_6d946c946a4b356511b4b13e17c724fa);
            
        

        marker_9ed7f425ec08a85a846f724ad55ffafe.bindPopup(popup_d2be23ee403236e096e0a96f9c93b45e)
        ;

        
    
    
            var marker_fa86c74b686a66fe217d483f042a5984 = L.marker(
                [42.43276888888889, 141.11317527777777],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_0d7e7d49612977476ae4d8c189f24979 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#ffffff", "markerColor": "red", "prefix": "glyphicon"}
            );
            marker_fa86c74b686a66fe217d483f042a5984.setIcon(icon_0d7e7d49612977476ae4d8c189f24979);
        
    
        var popup_6bf831ea97e96729599b4341b200c345 = L.popup({"maxWidth": 200});

        
            
                var html_8af9d2833800f29f30849ea904f41dba = $(`<div id="html_8af9d2833800f29f30849ea904f41dba" style="width: 100.0%; height: 100.0%;">事故6月20日13時頃発生 .                 天気：曇 &#x2601;(雲量がおおむね80％以上の状態で、他の天候に該当しないものをいう。)</div>`)[0];
                popup_6bf831ea97e96729599b4341b200c345.setContent(html_8af9d2833800f29f30849ea904f41dba);
            
        

        marker_fa86c74b686a66fe217d483f042a5984.bindPopup(popup_6bf831ea97e96729599b4341b200c345)
        ;

        
    
    
            var marker_dcbe365f713098dbd7213147fb300ee7 = L.marker(
                [42.924765, 142.03621194444446],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_29258ff9a42789013d4016b18a4ec565 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#ffffff", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_dcbe365f713098dbd7213147fb300ee7.setIcon(icon_29258ff9a42789013d4016b18a4ec565);
        
    
        var popup_56b52b8a041b6aaa2daf5a8dfc6bd8d9 = L.popup({"maxWidth": 200});

        
            
                var html_0a5ae106ddc5bf9e691b74f9fbb84b94 = $(`<div id="html_0a5ae106ddc5bf9e691b74f9fbb84b94" style="width: 100.0%; height: 100.0%;">事故6月27日14時頃発生 .                 天気：晴 &#x2600;(雲量がおおむね80％以下の状態で、他の天候に該当しないものをいう。)</div>`)[0];
                popup_56b52b8a041b6aaa2daf5a8dfc6bd8d9.setContent(html_0a5ae106ddc5bf9e691b74f9fbb84b94);
            
        

        marker_dcbe365f713098dbd7213147fb300ee7.bindPopup(popup_56b52b8a041b6aaa2daf5a8dfc6bd8d9)
        ;

        
    
    
            var marker_3d12dcebf95b13bae74c377af4e23c21 = L.marker(
                [42.55885833333334, 140.76687166666667],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_4dd9ffbe0374f69ba97d31661ff57a14 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#ffffff", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_3d12dcebf95b13bae74c377af4e23c21.setIcon(icon_4dd9ffbe0374f69ba97d31661ff57a14);
        
    
        var popup_a5928df0fed79ac032030fccb84a8954 = L.popup({"maxWidth": 200});

        
            
                var html_3fc64d41cf10858224fda101d0882a45 = $(`<div id="html_3fc64d41cf10858224fda101d0882a45" style="width: 100.0%; height: 100.0%;">事故7月24日12時頃発生 .                 天気：晴 &#x2600;(雲量がおおむね80％以下の状態で、他の天候に該当しないものをいう。)</div>`)[0];
                popup_a5928df0fed79ac032030fccb84a8954.setContent(html_3fc64d41cf10858224fda101d0882a45);
            
        

        marker_3d12dcebf95b13bae74c377af4e23c21.bindPopup(popup_a5928df0fed79ac032030fccb84a8954)
        ;

        
    
    
            var marker_248f0ca0758a9ebe395feb34df55e6b2 = L.marker(
                [42.90655027777778, 141.90071],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_3a8fd656d42d288126ebb4998e1c75f5 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#ffffff", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_248f0ca0758a9ebe395feb34df55e6b2.setIcon(icon_3a8fd656d42d288126ebb4998e1c75f5);
        
    
        var popup_8171e5a6fdffc0b6b0e95a3ab1c3315b = L.popup({"maxWidth": 200});

        
            
                var html_fec6721eb557931eb84fc442b5d530f4 = $(`<div id="html_fec6721eb557931eb84fc442b5d530f4" style="width: 100.0%; height: 100.0%;">事故8月1日17時頃発生 .                 天気：晴 &#x2600;(雲量がおおむね80％以下の状態で、他の天候に該当しないものをいう。)</div>`)[0];
                popup_8171e5a6fdffc0b6b0e95a3ab1c3315b.setContent(html_fec6721eb557931eb84fc442b5d530f4);
            
        

        marker_248f0ca0758a9ebe395feb34df55e6b2.bindPopup(popup_8171e5a6fdffc0b6b0e95a3ab1c3315b)
        ;

        
    
    
            var marker_3d54bea576ac1e31c61d4e49fd02795e = L.marker(
                [42.95759027777778, 141.50437694444443],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_9771eaeb8bc2376e137f82d15b82d96d = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#ffffff", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_3d54bea576ac1e31c61d4e49fd02795e.setIcon(icon_9771eaeb8bc2376e137f82d15b82d96d);
        
    
        var popup_885bd06bacaf8d9f0857320eeb14afc5 = L.popup({"maxWidth": 200});

        
            
                var html_4a1da2e7f80e4e4a6de6ba9dd700013f = $(`<div id="html_4a1da2e7f80e4e4a6de6ba9dd700013f" style="width: 100.0%; height: 100.0%;">事故8月6日9時頃発生 .                 天気：晴 &#x2600;(雲量がおおむね80％以下の状態で、他の天候に該当しないものをいう。)</div>`)[0];
                popup_885bd06bacaf8d9f0857320eeb14afc5.setContent(html_4a1da2e7f80e4e4a6de6ba9dd700013f);
            
        

        marker_3d54bea576ac1e31c61d4e49fd02795e.bindPopup(popup_885bd06bacaf8d9f0857320eeb14afc5)
        ;

        
    
    
            var marker_39e8d14334ae72fd1aec8222eb3b706b = L.marker(
                [43.10048194444444, 141.33831],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_e930ebbf4a27f505f6d58e748acd3b1b = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#ffffff", "markerColor": "red", "prefix": "glyphicon"}
            );
            marker_39e8d14334ae72fd1aec8222eb3b706b.setIcon(icon_e930ebbf4a27f505f6d58e748acd3b1b);
        
    
        var popup_588ed69bdb9ec624dda77dfe6faf000f = L.popup({"maxWidth": 200});

        
            
                var html_3e85336369cb1df3984111891fd17d3b = $(`<div id="html_3e85336369cb1df3984111891fd17d3b" style="width: 100.0%; height: 100.0%;">事故8月3日17時頃発生 .                 天気：晴 &#x2600;(雲量がおおむね80％以下の状態で、他の天候に該当しないものをいう。)</div>`)[0];
                popup_588ed69bdb9ec624dda77dfe6faf000f.setContent(html_3e85336369cb1df3984111891fd17d3b);
            
        

        marker_39e8d14334ae72fd1aec8222eb3b706b.bindPopup(popup_588ed69bdb9ec624dda77dfe6faf000f)
        ;

        
    
    
            var marker_d82d2e161a58805b2960627448e35625 = L.marker(
                [42.46688805555555, 141.18837666666667],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_3712eda2db0ea12b82eee47f6e6c1e0b = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#000000", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_d82d2e161a58805b2960627448e35625.setIcon(icon_3712eda2db0ea12b82eee47f6e6c1e0b);
        
    
        var popup_6df91585744f87c6fcd01724bf5b7ba7 = L.popup({"maxWidth": 200});

        
            
                var html_7ec55c9fa882ea5693594a44f5df5521 = $(`<div id="html_7ec55c9fa882ea5693594a44f5df5521" style="width: 100.0%; height: 100.0%;">事故8月1日21時頃発生 .                 天気：曇 &#x2601;(雲量がおおむね80％以上の状態で、他の天候に該当しないものをいう。)</div>`)[0];
                popup_6df91585744f87c6fcd01724bf5b7ba7.setContent(html_7ec55c9fa882ea5693594a44f5df5521);
            
        

        marker_d82d2e161a58805b2960627448e35625.bindPopup(popup_6df91585744f87c6fcd01724bf5b7ba7)
        ;

        
    
    
            var marker_bf71b573168f7a5c5f97f84626fc24f3 = L.marker(
                [42.61241583333333, 141.46561777777777],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_c0da0d312760d5d4d4644db65f445ab9 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#ffffff", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_bf71b573168f7a5c5f97f84626fc24f3.setIcon(icon_c0da0d312760d5d4d4644db65f445ab9);
        
    
        var popup_8df176fda112028abaf6d81683184169 = L.popup({"maxWidth": 200});

        
            
                var html_46b8d5325be6ecf7fe3c55a33413fefe = $(`<div id="html_46b8d5325be6ecf7fe3c55a33413fefe" style="width: 100.0%; height: 100.0%;">事故8月29日15時頃発生 .                 天気：晴 &#x2600;(雲量がおおむね80％以下の状態で、他の天候に該当しないものをいう。)</div>`)[0];
                popup_8df176fda112028abaf6d81683184169.setContent(html_46b8d5325be6ecf7fe3c55a33413fefe);
            
        

        marker_bf71b573168f7a5c5f97f84626fc24f3.bindPopup(popup_8df176fda112028abaf6d81683184169)
        ;

        
    
    
            var marker_5fa2e1855b76396c24cf2ee8d34c30e5 = L.marker(
                [43.0272, 141.44896472222223],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_36acfbafed0df465acc92737c875a9ad = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#ffffff", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_5fa2e1855b76396c24cf2ee8d34c30e5.setIcon(icon_36acfbafed0df465acc92737c875a9ad);
        
    
        var popup_2fe180da37776f5e8f2fba72076cec7f = L.popup({"maxWidth": 200});

        
            
                var html_b020a5f7d76cc338a27c14012adf7ab0 = $(`<div id="html_b020a5f7d76cc338a27c14012adf7ab0" style="width: 100.0%; height: 100.0%;">事故9月22日8時頃発生 .                 天気：晴 &#x2600;(雲量がおおむね80％以下の状態で、他の天候に該当しないものをいう。)</div>`)[0];
                popup_2fe180da37776f5e8f2fba72076cec7f.setContent(html_b020a5f7d76cc338a27c14012adf7ab0);
            
        

        marker_5fa2e1855b76396c24cf2ee8d34c30e5.bindPopup(popup_2fe180da37776f5e8f2fba72076cec7f)
        ;

        
    
    
            var marker_db162d1e59648e1c90ad0cd4239cc7b8 = L.marker(
                [42.847747777777776, 141.57749666666666],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_11017de95cc35fd4c4e4ebbc9f5a7ddb = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#ffffff", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_db162d1e59648e1c90ad0cd4239cc7b8.setIcon(icon_11017de95cc35fd4c4e4ebbc9f5a7ddb);
        
    
        var popup_bc1f9b350881a7220f690eba6af95855 = L.popup({"maxWidth": 200});

        
            
                var html_065fe5261aa040a5748c3660f0931fee = $(`<div id="html_065fe5261aa040a5748c3660f0931fee" style="width: 100.0%; height: 100.0%;">事故9月16日7時頃発生 .                 天気：晴 &#x2600;(雲量がおおむね80％以下の状態で、他の天候に該当しないものをいう。)</div>`)[0];
                popup_bc1f9b350881a7220f690eba6af95855.setContent(html_065fe5261aa040a5748c3660f0931fee);
            
        

        marker_db162d1e59648e1c90ad0cd4239cc7b8.bindPopup(popup_bc1f9b350881a7220f690eba6af95855)
        ;

        
    
    
            var marker_44b9a99159b666294105df271bde702f = L.marker(
                [42.92557361111111, 141.5386225],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_962eb24851afdf92f27e49aed89fd2cd = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#ffffff", "markerColor": "red", "prefix": "glyphicon"}
            );
            marker_44b9a99159b666294105df271bde702f.setIcon(icon_962eb24851afdf92f27e49aed89fd2cd);
        
    
        var popup_bf15c10bfd5f85f2d6b55c7c81ec29f3 = L.popup({"maxWidth": 200});

        
            
                var html_e3b4b5856d9b1d5308db75c5f8c08c79 = $(`<div id="html_e3b4b5856d9b1d5308db75c5f8c08c79" style="width: 100.0%; height: 100.0%;">事故9月21日6時頃発生 .                 天気：晴 &#x2600;(雲量がおおむね80％以下の状態で、他の天候に該当しないものをいう。)</div>`)[0];
                popup_bf15c10bfd5f85f2d6b55c7c81ec29f3.setContent(html_e3b4b5856d9b1d5308db75c5f8c08c79);
            
        

        marker_44b9a99159b666294105df271bde702f.bindPopup(popup_bf15c10bfd5f85f2d6b55c7c81ec29f3)
        ;

        
    
    
            var marker_42f411a3c36665751aa132f6fe4402eb = L.marker(
                [42.74596555555556, 141.64897055555556],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_dbdd373e69f1bdb6eeee1a8e6ae3ba20 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#a9a9a9", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_42f411a3c36665751aa132f6fe4402eb.setIcon(icon_dbdd373e69f1bdb6eeee1a8e6ae3ba20);
        
    
        var popup_25e9bece758a6069d72ad38c4c97d093 = L.popup({"maxWidth": 200});

        
            
                var html_afd5a131cc385c689e657fb7b8f4eecd = $(`<div id="html_afd5a131cc385c689e657fb7b8f4eecd" style="width: 100.0%; height: 100.0%;">事故9月12日5時頃発生 .                 天気：雨 &#x1f327;(雨が降っている状態をいう。)</div>`)[0];
                popup_25e9bece758a6069d72ad38c4c97d093.setContent(html_afd5a131cc385c689e657fb7b8f4eecd);
            
        

        marker_42f411a3c36665751aa132f6fe4402eb.bindPopup(popup_25e9bece758a6069d72ad38c4c97d093)
        ;

        
    
    
            var marker_6c89daf2909397b98925079986040b11 = L.marker(
                [42.95202416666667, 141.51200777777777],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_558ace87e6303df2ee449367cd00cb9b = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#ffffff", "markerColor": "black", "prefix": "glyphicon"}
            );
            marker_6c89daf2909397b98925079986040b11.setIcon(icon_558ace87e6303df2ee449367cd00cb9b);
        
    
        var popup_ecbe8c0a2c8202ebc5649688c6e540eb = L.popup({"maxWidth": 200});

        
            
                var html_781bb119936d7835d06fc7f9bddac44c = $(`<div id="html_781bb119936d7835d06fc7f9bddac44c" style="width: 100.0%; height: 100.0%;">事故10月19日8時頃発生 .                 天気：曇 &#x2601;(雲量がおおむね80％以上の状態で、他の天候に該当しないものをいう。)</div>`)[0];
                popup_ecbe8c0a2c8202ebc5649688c6e540eb.setContent(html_781bb119936d7835d06fc7f9bddac44c);
            
        

        marker_6c89daf2909397b98925079986040b11.bindPopup(popup_ecbe8c0a2c8202ebc5649688c6e540eb)
        ;

        
    
    
            var marker_8d51b2e8f6514e8631243c169946181f = L.marker(
                [43.01260027777778, 141.46488694444443],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_d3334b86d616e12ed98694791552e2e6 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#000000", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_8d51b2e8f6514e8631243c169946181f.setIcon(icon_d3334b86d616e12ed98694791552e2e6);
        
    
        var popup_a9a472d432257c048ee85b95743dd458 = L.popup({"maxWidth": 200});

        
            
                var html_e0216820ecf1772d5fa4b76f237a7e2f = $(`<div id="html_e0216820ecf1772d5fa4b76f237a7e2f" style="width: 100.0%; height: 100.0%;">事故11月15日17時頃発生 .                 天気：曇 &#x2601;(雲量がおおむね80％以上の状態で、他の天候に該当しないものをいう。)</div>`)[0];
                popup_a9a472d432257c048ee85b95743dd458.setContent(html_e0216820ecf1772d5fa4b76f237a7e2f);
            
        

        marker_8d51b2e8f6514e8631243c169946181f.bindPopup(popup_a9a472d432257c048ee85b95743dd458)
        ;

        
    
    
            var marker_ee86eda458ff8b9edc23fbd988df5482 = L.marker(
                [42.63494194444444, 141.49380250000002],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_508ecef6c710e2ba886583bca2feaa97 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#ffffff", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_ee86eda458ff8b9edc23fbd988df5482.setIcon(icon_508ecef6c710e2ba886583bca2feaa97);
        
    
        var popup_cc4880920fa0a92da484435ac76ab087 = L.popup({"maxWidth": 200});

        
            
                var html_411cc797c83e1606ee02ad425b822517 = $(`<div id="html_411cc797c83e1606ee02ad425b822517" style="width: 100.0%; height: 100.0%;">事故11月17日9時頃発生 .                 天気：晴 &#x2600;(雲量がおおむね80％以下の状態で、他の天候に該当しないものをいう。)</div>`)[0];
                popup_cc4880920fa0a92da484435ac76ab087.setContent(html_411cc797c83e1606ee02ad425b822517);
            
        

        marker_ee86eda458ff8b9edc23fbd988df5482.bindPopup(popup_cc4880920fa0a92da484435ac76ab087)
        ;

        
    
    
            var marker_1a1c258daddeb9215ae6f4712b1129cf = L.marker(
                [42.95088944444444, 141.51145083333333],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_97e3d78ef03d62132d2728dc4fcd6452 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#ffffff", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_1a1c258daddeb9215ae6f4712b1129cf.setIcon(icon_97e3d78ef03d62132d2728dc4fcd6452);
        
    
        var popup_1acdcd42179bce5b93d97f9dccf1259f = L.popup({"maxWidth": 200});

        
            
                var html_c62246c1f647212568802cf488bc19af = $(`<div id="html_c62246c1f647212568802cf488bc19af" style="width: 100.0%; height: 100.0%;">事故11月18日13時頃発生 .                 天気：晴 &#x2600;(雲量がおおむね80％以下の状態で、他の天候に該当しないものをいう。)</div>`)[0];
                popup_1acdcd42179bce5b93d97f9dccf1259f.setContent(html_c62246c1f647212568802cf488bc19af);
            
        

        marker_1a1c258daddeb9215ae6f4712b1129cf.bindPopup(popup_1acdcd42179bce5b93d97f9dccf1259f)
        ;

        
    
    
            var marker_688e069eca2f980d0d4abe5f281e1800 = L.marker(
                [42.81586777777778, 141.6191227777778],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_c9718daf12d0dbd42de18c23336d6059 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#000000", "markerColor": "red", "prefix": "glyphicon"}
            );
            marker_688e069eca2f980d0d4abe5f281e1800.setIcon(icon_c9718daf12d0dbd42de18c23336d6059);
        
    
        var popup_52a10b4f8a9de850458b31c09d7817a9 = L.popup({"maxWidth": 200});

        
            
                var html_b578df08662595f6c2c462bc61095d8f = $(`<div id="html_b578df08662595f6c2c462bc61095d8f" style="width: 100.0%; height: 100.0%;">事故12月28日20時頃発生 .                 天気：曇 &#x2601;(雲量がおおむね80％以上の状態で、他の天候に該当しないものをいう。)</div>`)[0];
                popup_52a10b4f8a9de850458b31c09d7817a9.setContent(html_b578df08662595f6c2c462bc61095d8f);
            
        

        marker_688e069eca2f980d0d4abe5f281e1800.bindPopup(popup_52a10b4f8a9de850458b31c09d7817a9)
        ;

        
    
    
            var marker_87b320d6a606150cc85c742baabf3347 = L.marker(
                [43.22878388888889, 141.83035388888888],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_15ce27cf64db41e6942560634394d4f2 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#ffffff", "markerColor": "red", "prefix": "glyphicon"}
            );
            marker_87b320d6a606150cc85c742baabf3347.setIcon(icon_15ce27cf64db41e6942560634394d4f2);
        
    
        var popup_2e2d67ed2139db9b89ad071481521162 = L.popup({"maxWidth": 200});

        
            
                var html_47a8bdb1e58593b66ae0764d871a4289 = $(`<div id="html_47a8bdb1e58593b66ae0764d871a4289" style="width: 100.0%; height: 100.0%;">事故12月26日14時頃発生 .                 天気：雪 &#x2744;(雪、みぞれ、ひょうが降っている状態をいう。)</div>`)[0];
                popup_2e2d67ed2139db9b89ad071481521162.setContent(html_47a8bdb1e58593b66ae0764d871a4289);
            
        

        marker_87b320d6a606150cc85c742baabf3347.bindPopup(popup_2e2d67ed2139db9b89ad071481521162)
        ;

        
    
    
            var marker_1aef211081ea1ffb4febde11515fa82e = L.marker(
                [43.24402305555556, 141.83032444444444],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_6de2805595578c1f3002228d100e8471 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#0000ff", "markerColor": "red", "prefix": "glyphicon"}
            );
            marker_1aef211081ea1ffb4febde11515fa82e.setIcon(icon_6de2805595578c1f3002228d100e8471);
        
    
        var popup_8797d3bc0bb0737776fcd9933084215e = L.popup({"maxWidth": 200});

        
            
                var html_20d9dad9f053638249489ab7b5f4cdee = $(`<div id="html_20d9dad9f053638249489ab7b5f4cdee" style="width: 100.0%; height: 100.0%;">事故12月2日16時頃発生 .                 天気：曇 &#x2601;(雲量がおおむね80％以上の状態で、他の天候に該当しないものをいう。)</div>`)[0];
                popup_8797d3bc0bb0737776fcd9933084215e.setContent(html_20d9dad9f053638249489ab7b5f4cdee);
            
        

        marker_1aef211081ea1ffb4febde11515fa82e.bindPopup(popup_8797d3bc0bb0737776fcd9933084215e)
        ;

        
    
    
            var marker_f3aa2d8d73c83d85f9b01fc7a0c00118 = L.marker(
                [42.94913833333333, 141.51435083333334],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_d2d9364c0798fec7b5667299a981ca0a = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#ffffff", "markerColor": "red", "prefix": "glyphicon"}
            );
            marker_f3aa2d8d73c83d85f9b01fc7a0c00118.setIcon(icon_d2d9364c0798fec7b5667299a981ca0a);
        
    
        var popup_9197f58b53e92382a227ba56b0005dae = L.popup({"maxWidth": 200});

        
            
                var html_753de32fcc0725cd50c895d840a0bf8a = $(`<div id="html_753de32fcc0725cd50c895d840a0bf8a" style="width: 100.0%; height: 100.0%;">事故12月18日13時頃発生 .                 天気：晴 &#x2600;(雲量がおおむね80％以下の状態で、他の天候に該当しないものをいう。)</div>`)[0];
                popup_9197f58b53e92382a227ba56b0005dae.setContent(html_753de32fcc0725cd50c895d840a0bf8a);
            
        

        marker_f3aa2d8d73c83d85f9b01fc7a0c00118.bindPopup(popup_9197f58b53e92382a227ba56b0005dae)
        ;

        
    
    
            var marker_c4596d2bf929ceae19b5140195418bf5 = L.marker(
                [43.637715, 141.9884722222222],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_98fa82107f150cf7b8a3a2ded2297c01 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#ffffff", "markerColor": "black", "prefix": "glyphicon"}
            );
            marker_c4596d2bf929ceae19b5140195418bf5.setIcon(icon_98fa82107f150cf7b8a3a2ded2297c01);
        
    
        var popup_210331dacae4f0a9ecd61c3eebb94282 = L.popup({"maxWidth": 200});

        
            
                var html_71e5551690ac6f9bb1ca099acac15f96 = $(`<div id="html_71e5551690ac6f9bb1ca099acac15f96" style="width: 100.0%; height: 100.0%;">事故12月1日13時頃発生 .                 天気：雨 &#x1f327;(雨が降っている状態をいう。)</div>`)[0];
                popup_210331dacae4f0a9ecd61c3eebb94282.setContent(html_71e5551690ac6f9bb1ca099acac15f96);
            
        

        marker_c4596d2bf929ceae19b5140195418bf5.bindPopup(popup_210331dacae4f0a9ecd61c3eebb94282)
        ;

        
    
    
            var marker_fb7768f3dcedf44dbd10c3eb05e48daa = L.marker(
                [43.102376388888885, 141.2457752777778],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_7e008c3f0802d0e596dce29cfdfe7efd = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#ffffff", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_fb7768f3dcedf44dbd10c3eb05e48daa.setIcon(icon_7e008c3f0802d0e596dce29cfdfe7efd);
        
    
        var popup_f2b343107e2bd7e0638a8e8dd80e9f96 = L.popup({"maxWidth": 200});

        
            
                var html_59ecf2103e3147c2a5345843c26a2045 = $(`<div id="html_59ecf2103e3147c2a5345843c26a2045" style="width: 100.0%; height: 100.0%;">事故12月17日9時頃発生 .                 天気：雪 &#x2744;(雪、みぞれ、ひょうが降っている状態をいう。)</div>`)[0];
                popup_f2b343107e2bd7e0638a8e8dd80e9f96.setContent(html_59ecf2103e3147c2a5345843c26a2045);
            
        

        marker_fb7768f3dcedf44dbd10c3eb05e48daa.bindPopup(popup_f2b343107e2bd7e0638a8e8dd80e9f96)
        ;

        
    
    
            var marker_4da86d8204db9627191065f4a2e4507f = L.marker(
                [42.56156722222222, 140.75886888888888],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_77096bc0c900ae5e0bd9dd88218a4e92 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#ffffff", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_4da86d8204db9627191065f4a2e4507f.setIcon(icon_77096bc0c900ae5e0bd9dd88218a4e92);
        
    
        var popup_7c3df09c342f40d744089e934d74c7db = L.popup({"maxWidth": 200});

        
            
                var html_55f3690a91b99f1db5bbbaa38df34c68 = $(`<div id="html_55f3690a91b99f1db5bbbaa38df34c68" style="width: 100.0%; height: 100.0%;">事故12月8日12時頃発生 .                 天気：曇 &#x2601;(雲量がおおむね80％以上の状態で、他の天候に該当しないものをいう。)</div>`)[0];
                popup_7c3df09c342f40d744089e934d74c7db.setContent(html_55f3690a91b99f1db5bbbaa38df34c68);
            
        

        marker_4da86d8204db9627191065f4a2e4507f.bindPopup(popup_7c3df09c342f40d744089e934d74c7db)
        ;

        
    
    
            var marker_ea023312c2c0875845a7f5bbdf25474b = L.marker(
                [43.19490166666667, 141.801265],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_42fabac9e425ff2c5fa3bb60ea13429a = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#000000", "markerColor": "red", "prefix": "glyphicon"}
            );
            marker_ea023312c2c0875845a7f5bbdf25474b.setIcon(icon_42fabac9e425ff2c5fa3bb60ea13429a);
        
    
        var popup_b07d5d9ac09c8b5587f91cd9a04d2a39 = L.popup({"maxWidth": 200});

        
            
                var html_c4bd8b8764047b2db0e6279ea5d650dc = $(`<div id="html_c4bd8b8764047b2db0e6279ea5d650dc" style="width: 100.0%; height: 100.0%;">事故12月28日5時頃発生 .                 天気：雪 &#x2744;(雪、みぞれ、ひょうが降っている状態をいう。)</div>`)[0];
                popup_b07d5d9ac09c8b5587f91cd9a04d2a39.setContent(html_c4bd8b8764047b2db0e6279ea5d650dc);
            
        

        marker_ea023312c2c0875845a7f5bbdf25474b.bindPopup(popup_b07d5d9ac09c8b5587f91cd9a04d2a39)
        ;

        
    
    
            var marker_027ac10dcd73b97add77c32bab2b56b1 = L.marker(
                [43.06355833333333, 142.54560083333334],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_44460f358e033ff0dc4b2afd96263e12 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#ffffff", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_027ac10dcd73b97add77c32bab2b56b1.setIcon(icon_44460f358e033ff0dc4b2afd96263e12);
        
    
        var popup_407fda0b2d5d332f2477cbf9c79308e4 = L.popup({"maxWidth": 200});

        
            
                var html_e1c5158be2f875b5d35a6948a91bd375 = $(`<div id="html_e1c5158be2f875b5d35a6948a91bd375" style="width: 100.0%; height: 100.0%;">事故1月15日14時頃発生 .                 天気：曇 &#x2601;(雲量がおおむね80％以上の状態で、他の天候に該当しないものをいう。)</div>`)[0];
                popup_407fda0b2d5d332f2477cbf9c79308e4.setContent(html_e1c5158be2f875b5d35a6948a91bd375);
            
        

        marker_027ac10dcd73b97add77c32bab2b56b1.bindPopup(popup_407fda0b2d5d332f2477cbf9c79308e4)
        ;

        
    
    
            var marker_39ca469f78b8060be9bfd2004650c331 = L.marker(
                [43.79215583333333, 142.26018694444446],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_4046166c345347038c2de711d400d777 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#ffa500", "markerColor": "red", "prefix": "glyphicon"}
            );
            marker_39ca469f78b8060be9bfd2004650c331.setIcon(icon_4046166c345347038c2de711d400d777);
        
    
        var popup_3406242b0c89788a62d6dd366b68ec71 = L.popup({"maxWidth": 200});

        
            
                var html_9bdb89b43a78d66e586851a8553b057c = $(`<div id="html_9bdb89b43a78d66e586851a8553b057c" style="width: 100.0%; height: 100.0%;">事故2月9日16時頃発生 .                 天気：雪 &#x2744;(雪、みぞれ、ひょうが降っている状態をいう。)</div>`)[0];
                popup_3406242b0c89788a62d6dd366b68ec71.setContent(html_9bdb89b43a78d66e586851a8553b057c);
            
        

        marker_39ca469f78b8060be9bfd2004650c331.bindPopup(popup_3406242b0c89788a62d6dd366b68ec71)
        ;

        
    
    
            var marker_b9d284a30df6fbeb4a15bc07e9093861 = L.marker(
                [43.05415222222222, 142.60003],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_726de171c3639290d77832082fcb37af = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#ffffff", "markerColor": "black", "prefix": "glyphicon"}
            );
            marker_b9d284a30df6fbeb4a15bc07e9093861.setIcon(icon_726de171c3639290d77832082fcb37af);
        
    
        var popup_489b81d31e28edbec082e021b8ab3b34 = L.popup({"maxWidth": 200});

        
            
                var html_d66a065eba5606c3fa706e07158447cd = $(`<div id="html_d66a065eba5606c3fa706e07158447cd" style="width: 100.0%; height: 100.0%;">事故2月17日12時頃発生 .                 天気：曇 &#x2601;(雲量がおおむね80％以上の状態で、他の天候に該当しないものをいう。)</div>`)[0];
                popup_489b81d31e28edbec082e021b8ab3b34.setContent(html_d66a065eba5606c3fa706e07158447cd);
            
        

        marker_b9d284a30df6fbeb4a15bc07e9093861.bindPopup(popup_489b81d31e28edbec082e021b8ab3b34)
        ;

        
    
    
            var marker_6ae9ed5d4306c17fab095c07dc70b17b = L.marker(
                [43.04507, 142.6765127777778],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_8c01f07663abaed3e15f2e23008abf6e = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#ffffff", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_6ae9ed5d4306c17fab095c07dc70b17b.setIcon(icon_8c01f07663abaed3e15f2e23008abf6e);
        
    
        var popup_3adf8a069f062450ba10fef7fc0d1e42 = L.popup({"maxWidth": 200});

        
            
                var html_b2b75654cda08c14aed55e4d7cd34375 = $(`<div id="html_b2b75654cda08c14aed55e4d7cd34375" style="width: 100.0%; height: 100.0%;">事故3月22日10時頃発生 .                 天気：曇 &#x2601;(雲量がおおむね80％以上の状態で、他の天候に該当しないものをいう。)</div>`)[0];
                popup_3adf8a069f062450ba10fef7fc0d1e42.setContent(html_b2b75654cda08c14aed55e4d7cd34375);
            
        

        marker_6ae9ed5d4306c17fab095c07dc70b17b.bindPopup(popup_3adf8a069f062450ba10fef7fc0d1e42)
        ;

        
    
    
            var marker_34a746fc6b2512ceccf3ae0b01c03bb7 = L.marker(
                [43.060698611111114, 142.7164363888889],
                {}
            ).addTo(map_235d4c48bc5742b79af7cea034cebbef);
        
    
            var icon_b3877cc5febcb5b30bfd58e3dbb76231 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "info-sign", "iconColor": "#000000", "markerColor": "blue", "prefix": "glyphicon"}
            );
            marker_34a746fc6b2512ceccf3ae0b01c03bb7.setIcon(icon_b3877cc5febcb5b30bfd58e3dbb76231);
        
    
        var popup_af798634f51ca37a9d88e28506a820ba = L.popup({"maxWidth": 200});

        
            
                var html_0f6735af298cc02dee868347ba1eddd7 = $(`<div id="html_0f6735af298cc02dee868347ba1eddd7" style="width: 100.0%; height: 100.0%;">事故12月17日18時頃発生 .                 天気：雪 &#x2744;(雪、みぞれ、ひょうが降っている状態をいう。)</div>`)[0];
                popup_af798634f51ca37a9d88e28506a820ba.setContent(html_0f6735af298cc02dee868347ba1eddd7);
            
        

        marker_34a746fc6b2512ceccf3ae0b01c03bb7.bindPopup(popup_af798634f51ca37a9d88e28506a820ba)
        ;

        
    
</script>
</html>
""",
    height=700,
    width=900,
)
