import streamlit as st
# import gmaps
# from ipywidgets import embed
# import streamlit.components.v1 as components
# from streamlit_folium import folium_static
# from folium import Map

# Set the website layouts
st.set_page_config(
    page_title='RAUL Y ZANYA',
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.title("Zanya y Raul 2024")



st.markdown(
    """
    <style>
        button[title^=Exit]+div [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
)

# Navigation Options
side_options = st.sidebar.radio(
    'Pages',
    options=[
        'Detalles del Evento',
        'Locación'
    ]
)

# %%

if side_options == 'Detalles del Evento':
    left_co, cent_co, last_co = st.columns([1, 8, 1])
    with cent_co:
        st.image('Inputs/Home.png')
        # streamlit_style = """
        # 			<style>
        # 			@import url('https://fonts.googleapis.com/css2?family=Hedvig+Letters+Serif:opsz@12..24&display=swap');
        #
        # 			html, body, [class*="css"]  {
        # 			font-family: 'Hedvig Letters Serif', serif;
        #
        # 			}
        # 			</style>
        #
        # 			"""

        # st.markdown(streamlit_style, unsafe_allow_html=True)
        original_title = '<h1 style="font-family:Hedvig Letters Serif; text-align: center; color:black; font-size: 60px;">Zanya y Raul</h1>'
        st.markdown(original_title, unsafe_allow_html=True)

        # st.markdown("<h1 style='text-align: center; color: black;'>Zanya y Raul</h1>", unsafe_allow_html=True)

        # st.markdown("*Streamlit* is **really** ***cool***.")
        # st.markdown('''
        #     :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
        #     :gray[pretty] :rainbow[colors].''')
        # st.markdown('RAUL Y ZANYA', unsafe_allow_html=True)

        st.markdown("""
        <p1 style='font-family:Hedvig Letters Serif; text-align: center; color:black; font-size: 24px;'>
            Tenemos el placer de invitarte a nuestra gran fiesta!
            Compartir este dia contigo nos llena de emoción, por lo que queremos invitarte
            Por favor confirma tu asistencia en:
            </p1>
        
        """, unsafe_allow_html=True)
        # st.markdown("<h1 style='text-align: center; color: black;'>Tenemos el placer de invitarte a nuestra gran fiesta!</h1>", unsafe_allow_html=True)
        # st.markdown("<h1 style='text-align: center; color: black;'> </h1>", unsafe_allow_html=True)
        # st.markdown("<h1 style='text-align: center; color: black;'>Por favor confirma tu asistencia en:</h1>", unsafe_allow_html=True)
        # # st.image('inputs/Home.png')
        st.image('Inputs/Invitacion.png')

if side_options == 'Locación':
    left_co, cent_co, last_co = st.columns([1, 8, 1])
    with cent_co:
        original_title = '<h1 style="font-family:Hedvig Letters Serif; text-align: center; color:black; font-size: 60px;">Zanya y Raul</h1>'


        st.markdown(original_title, unsafe_allow_html=True)

        # snippet = embed.embed_snippet(views=map)
        # html = embed.html_template.format(title="", snippet=snippet)
        # components.html(html, height=500, width=500)
        # m = Map(location=[40.7128, -74.0060], zoom_start=13)
        #
        # # Add your desired map features and markers
        #
        # # ...
        #
        # # Generate HTML representation
        # map = folium_static(m)
        # # st.write(map)



        def map_with_custom_size(height, width):
            map_height = height  # Set the desired height of the map
            map_width = width  # Set the desired width of the map

            # Replace 'YOUR_GOOGLE_MAPS_EMBED_LINK' with your actual Google Maps embed link
            google_maps_embed_link = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d50725.55361268366!2d-98.36340323724508!3d19.098909484285258!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x85cfcf5e5ca26c7b%3A0xc57320f8345a640!2sCali%20Coanatl%20Garden!5e0!3m2!1sen!2smx!4v1701978588992!5m2!1sen!2smx"

            # Generate the HTML to embed the Google Maps location
            map_html = f'<iframe width="{map_width}" height="{map_height}" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="{google_maps_embed_link}"></iframe>'

            # Apply CSS styling to resize the map container
            map_style = f"<style>div.stFrame.stIframe.sandboxRoot.ve-map-container{{ width: {map_width}px; height: {map_height}px; }}</style>"

            # map_style = f"""
            # <style>
            #     div.stFrame.stIframe.sandboxRoot.ve-map-container {{
            #         width: {map_width}px;
            #         height: {map_height}px;
            #     }}
            #
            #     @media only screen and (max-width: 600px) {{
            #         div.stFrame.stIframe.sandboxRoot.ve-map-container {{
            #             width: 100%;
            #             height: 300px; /* Adjust the height for smaller screens */
            #         }}
            #     }}
            # </style>
            # """
            # Render the map with custom size
            st.markdown(map_style, unsafe_allow_html=True)
            st.markdown(map_html, unsafe_allow_html=True)

        # Display the map
        map_with_custom_size(height=600, width=1200)

        st.markdown("""
        <p1 style='font-family:Hedvig Letters Serif; text-align: center; color:black; font-size: 24px;'>
            El Evento será en el Jardin Cali Coanatl, a 15 minutos del centro de Cholula y 20 de Explanada Puebla
            Dirección: Reforma 2, Cuanalá, 72640 Puebla, Pue., Mexico. 
            </p1>

        """, unsafe_allow_html=True)

        st.image('Inputs/Grecas.png')

# "# Center an image when in fullscreen"
# "Images (and most elements in general) are always aligned to the left"
# st.image('inputs/Home.png')

# !pip install gmaps