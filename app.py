
import streamlit as st

st.set_page_config(page_title="Asistente Virtual IA - Juzgado N° 9", layout="centered")

st.title("Asistente Virtual IA")
st.subheader("Juzgado Civil y Comercial N° 9 - Departamento Judicial La Matanza")
st.markdown("""
**Bienvenido/a al Asistente Virtual IA del Juzgado Civil y Comercial N° 9 – Departamento Judicial La Matanza.**  
Puede evacuar sus consultas a través del menú guiado o escribiendo su duda en lenguaje natural.  
**Este servicio no implica asesoramiento jurídico ni constituye una vía de contacto procesal.**
""")

modo = st.radio("Seleccione un modo de consulta:", ["Menú guiado", "Consulta por texto libre"])

if modo == "Menú guiado":
    opciones = [
        "Preguntas frecuentes para abogados y partes",
        "Requisitos para inscribir declaratoria de herederos",
        "Visualización de expediente como e-book",
        "Uso de TICs en audiencias (BLSG)",
        "Redes sociales del juzgado",
        "Encuestas de satisfacción",
        "Contacto con SADyP (Zoom)"
    ]
    consulta = st.selectbox("Seleccione un tema:", opciones)

    if consulta == opciones[0]:
        st.markdown("### Preguntas frecuentes\n\n**¿Cómo consulto los saldos de una cuenta judicial?**\nA través del Portal de Presentaciones y Notificaciones Electrónicas, ingrese a la sección de sus causas y utilice el botón \"ver cuentas bancarias\".\n\n**¿Qué requisitos debe tener un Oficio Ley 22.172?**\nDebe contener: 1) Nombre del Juez, 2) Secretaria, 3) Dirección del juzgado, 4) Competencia, 5) Auto ordenatorio, 6) Finalidad del oficio.\n\n**¿En la Mesa de Entradas puedo consultar expedientes en papel?**\nNO. Somos un Juzgado Digitalizado, todos los expedientes se consultan online.\n\n**¿Cómo se realizan las subastas?**\nSon electrónicas. Más información:  [Subastas SCBA](https://www.scba.gov.ar/paginas.asp?id=50473)\n\n**¿Cómo abono la Tasa de Justicia?**  [Instructivo SCBA](https://www.scba.gov.ar/paginas.asp?id=46791)\n\n**¿Cómo busco un domicilio electrónico?**  [Buscar domicilio electrónico](https://www.scba.gov.ar/paginas.asp?id=46690)\n\n**¿Cuál es el valor actual del IUS?**\nLo publicamos en Instagram y también está en: [Valor del IUS](https://www.scba.gov.ar/paginas.asp?id=41320)\n\n**¿Cómo obtengo los códigos de materias para iniciar expediente?**  [Ver códigos de materias](https://www.scba.gov.ar/paginas.asp?id=41329)")

    elif consulta == opciones[1]:
        st.markdown("**Inscripción de declaratoria de herederos:**  [Ver instructivo (OneDrive)](https://scbagovar-my.sharepoint.com/:b:/g/personal/rcsdellaporta_scba_gov_ar/EajRyx2zlyJPiYR8jb1h2sABvpMp61o4XFOe1PO8jE3XTw?e=PA4Wcxv)")

    elif consulta == opciones[2]:
        st.markdown("**Visualización del expediente digital como e-book:**  [Guía paso a paso (OneDrive)](https://scbagovar-my.sharepoint.com/:b:/g/personal/rcsdellaporta_scba_gov_ar/EbL9wah_T_BEjdV8mPGDFQYBHdMX4V4xOhVtJK61Jf9dWQ?e=6FtcAG)")

    elif consulta == opciones[3]:
        st.markdown("**Uso de TICs para testimoniales en procesos BLSG:**  [Acceder a la guía (OneDrive)](https://scbagovar-my.sharepoint.com/:b:/g/personal/rcsdellaporta_scba_gov_ar/EZ8AXylbqQtPjMmQ_VBYJ9EB0Kkis9EPcmonM3ymYDVvTQ?e=WxhwAd)")

    elif consulta == opciones[4]:
        st.markdown("**Redes sociales activas del juzgado:**  Instagram: [@juzcivcom9lamatanza](https://www.instagram.com/juzcivcom9lamatanza/)")

    elif consulta == opciones[5]:
        st.markdown("**Encuestas de satisfacción:**  [Profesionales del Derecho](https://docs.google.com/forms/d/e/1FAIpQLSelQUyg_3rns4lk5lEhupU311yxPwfZDXspvreS-GwYnxrSWw/viewform)  [Público general](https://docs.google.com/forms/d/e/1FAIpQLSd3ILJSn6i2F-WXT85Ap_-3WWSyYZ6ULjqFFKgt0fc0dmqxiQ/viewform)")

    elif consulta == opciones[6]:
        st.markdown("**SADyP - Servicio de Atención Digital y Personalizada**  Zoom - Lunes a viernes de 9 a 13 hs  [Acceder a la sala](https://us05web.zoom.us/j/4715183830?pwd=KzZlVUtjWnZlYlJyWmx2ZGFKTHdmZz09)")

else:
    pregunta = st.text_input("Escriba su consulta:")
    if pregunta:
        if "saldo" in pregunta.lower():
            st.write("Puede consultar el saldo de la cuenta judicial desde el Portal de Presentaciones Electrónicas, botón 'ver cuentas bancarias'.")
        elif "ius" in pregunta.lower():
            st.write("El valor del IUS se publica en nuestro Instagram y también puede consultarlo en el sitio web de la SCBA.")
        elif "tasa" in pregunta.lower():
            st.write("La SCBA publicó un instructivo para el pago de la Tasa de Justicia: https://www.scba.gov.ar/paginas.asp?id=46791")
        elif "domicilio electrónico" in pregunta.lower():
            st.write("Puede buscar domicilios electrónicos en: https://www.scba.gov.ar/paginas.asp?id=46690")
        elif "audiencia" in pregunta.lower():
            st.write("El link de la audiencia se encuentra en la providencia que la fija. No se envía por mail.")
        else:
            st.write("Gracias por su consulta. Si su duda no fue respondida, puede comunicarse con el SADyP por Zoom de lunes a viernes de 9 a 13 hs.")

st.markdown("---\n✨ **Gracias por utilizar el Asistente Virtual IA del Juzgado Civil y Comercial N° 9.**  Este servicio está en desarrollo continuo. Sus comentarios son bienvenidos.")
