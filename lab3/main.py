from PIL import Image
import streamlit as st

uploaded_file = st.file_uploader(label='Загрузите изображение', type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file).convert('RGB')
        
        r, g, b = image.split()
        
        red_image = Image.merge('RGB', (r, Image.new('L', image.size, 0), Image.new('L', image.size, 0)))
        green_image = Image.merge('RGB', (Image.new('L', image.size, 0), g, Image.new('L', image.size, 0)))
        blue_image = Image.merge('RGB', (Image.new('L', image.size, 0), Image.new('L', image.size, 0), b))
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.image(red_image, caption='Красная составляющая', use_container_width=True)
        with col2:
            st.image(green_image, caption='Зелёная составляющая', use_container_width=True)
        with col3:
            st.image(blue_image, caption='Синяя составляющая', use_container_width=True)
            
    except Exception as e:
        st.error(f"Ошибка при обработке: {e}")
else:
    st.info("Пожалуйста, загрузите изображение.")
