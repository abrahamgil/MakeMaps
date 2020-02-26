import folium
map = folium.Map(location=[29.770838, -95.400394], zoom_start=8, tiles="Stamen Terrain")

#adding feature group to keep code more organized later the FG can be edited easier then just adding child
fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[29.2, -95.1],popup="Hi I am a Marker", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Map1.html")